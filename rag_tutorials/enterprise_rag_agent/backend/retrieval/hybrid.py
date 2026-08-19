from __future__ import annotations

import math
import re
import json
from urllib import request as urlrequest
from collections import Counter

from core.models import ChunkRecord, RetrievedChunk
from security.permissions import can_access
from storage.sqlite_store import SQLiteRAGStore
from .embeddings import EmbeddingGenerator, cosine_similarity

TOKEN_PATTERN = re.compile(r"[\w\u4e00-\u9fff]+", re.UNICODE)

QUERY_EXPANSIONS = {
    "incident": {"incident", "outage", "failure", "security", "security incident"},
    "access": {"access", "permission", "permissioning", "authorization"},
    "onboarding": {"onboarding", "joiner", "new hire"},
    "backup": {"backup", "restore", "retention"},
    "escalation": {"escalation", "escalate", "severity", "priority"},
}


def tokenize(text: str) -> list[str]:
    return [token.lower() for token in TOKEN_PATTERN.findall(text)]


def expand_query(question: str) -> list[str]:
    tokens = tokenize(question)
    expanded = list(tokens)
    for token in tokens:
        expanded.extend(QUERY_EXPANSIONS.get(token, []))
    return expanded


class HybridRetriever:
    def __init__(
        self,
        store: SQLiteRAGStore,
        embedding_generator: EmbeddingGenerator,
        rerank_provider: str = "heuristic",
        rerank_url: str | None = None,
        rerank_api_key: str | None = None,
    ) -> None:
        self.store = store
        self.embedding_generator = embedding_generator
        self.rerank_provider = rerank_provider
        self.rerank_url = rerank_url
        self.rerank_api_key = rerank_api_key

    def retrieve(
        self,
        question: str,
        top_k: int,
        knowledge_bases: list[str] | None = None,
        user_groups: list[str] | None = None,
        rerank_top_k: int = 12,
        tenant_id: str = "default",
    ) -> list[RetrievedChunk]:
        query_tokens = expand_query(question)
        if not query_tokens:
            return []

        query_counts = Counter(query_tokens)
        query_embedding = self.embedding_generator.embed_texts([question])[0]
        candidates: list[RetrievedChunk] = []
        for chunk in self.store.load_chunks(knowledge_bases, tenant_id=tenant_id):
            if not can_access(chunk.allowed_groups, user_groups):
                continue
            lexical_score, matched_terms = self._score_chunk(chunk, query_counts)
            vector_score = max(0.0, cosine_similarity(query_embedding, chunk.embedding))
            if lexical_score <= 0 and vector_score <= 0.2:
                continue
            rerank_score, rerank_reasons = self._rerank(chunk, query_counts, lexical_score)
            final_score = lexical_score * 0.45 + vector_score * 0.35 + rerank_score * 0.20
            candidates.append(
                RetrievedChunk(
                    chunk=chunk,
                    score=final_score,
                    lexical_score=lexical_score,
                    vector_score=vector_score,
                    rerank_score=rerank_score,
                    matched_terms=matched_terms,
                    rerank_reasons=rerank_reasons,
                )
            )

        if self.rerank_provider == "http" and self.rerank_url:
            self._apply_external_rerank(question, candidates[:rerank_top_k])
        candidates.sort(key=lambda item: item.score, reverse=True)
        return candidates[: max(top_k, rerank_top_k)][:top_k]

    def _apply_external_rerank(self, question: str, candidates: list[RetrievedChunk]) -> None:
        """调用可配置 HTTP rerank 服务，失败时保留本地启发式排序。"""
        payload = json.dumps(
            {"query": question, "documents": [item.chunk.text for item in candidates]}
        ).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        if self.rerank_api_key:
            headers["Authorization"] = f"Bearer {self.rerank_api_key}"
        try:
            http_request = urlrequest.Request(self.rerank_url, data=payload, headers=headers, method="POST")
            with urlrequest.urlopen(http_request, timeout=8) as response:
                result = json.loads(response.read().decode("utf-8"))
            scores = result.get("scores", [])
            if len(scores) != len(candidates):
                return
            for item, score in zip(candidates, scores, strict=True):
                item.rerank_score = float(score)
                item.score = item.lexical_score * 0.45 + item.vector_score * 0.35 + item.rerank_score * 0.20
                item.rerank_reasons = [*item.rerank_reasons, "外部 HTTP rerank"]
        except (OSError, ValueError, TypeError, KeyError):
            return

    def _score_chunk(self, chunk: ChunkRecord, query_counts: Counter[str]) -> tuple[float, list[str]]:
        chunk_tokens = tokenize(chunk.text)
        if not chunk_tokens:
            return 0.0, []

        chunk_counts = Counter(chunk_tokens)
        matched_terms = [term for term in query_counts if term in chunk_counts]
        if not matched_terms:
            return 0.0, []

        overlap = sum(min(query_counts[term], chunk_counts[term]) for term in matched_terms)
        density = overlap / math.sqrt(len(chunk_tokens))
        title_boost = 0.4 if any(term in chunk.title.lower() for term in query_counts) else 0.0
        section_boost = 0.2 if any(term in chunk.section_path.lower() for term in query_counts) else 0.0
        phrase = " ".join(query_counts.keys())
        phrase_boost = 0.5 if phrase and phrase in chunk.text.lower() else 0.0
        score = density + title_boost + section_boost + phrase_boost
        return score, matched_terms

    def _rerank(
        self,
        chunk: ChunkRecord,
        query_counts: Counter[str],
        lexical_score: float,
    ) -> tuple[float, list[str]]:
        chunk_tokens = set(tokenize(chunk.text))
        heading_tokens = set(tokenize(chunk.section_path))
        query_terms = set(query_counts.keys())
        overlap_ratio = len(chunk_tokens & query_terms) / max(1, len(query_terms))
        heading_ratio = len(heading_tokens & query_terms) / max(1, len(query_terms))
        compactness = min(1.0, 2000 / max(200, len(chunk.text)))
        reasons: list[str] = []
        if overlap_ratio > 0:
            reasons.append(f"内容覆盖 {overlap_ratio:.0%}")
        if heading_ratio > 0:
            reasons.append(f"标题/章节命中 {heading_ratio:.0%}")
        if compactness >= 0.9:
            reasons.append("片段长度适中")
        return lexical_score + overlap_ratio * 0.6 + heading_ratio * 0.4 + compactness * 0.1, reasons
