from __future__ import annotations

import math
import re
from collections import Counter

from ..core.models import ChunkRecord, RetrievedChunk
from ..security.permissions import can_access
from ..storage.sqlite_store import SQLiteRAGStore

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
    def __init__(self, store: SQLiteRAGStore) -> None:
        self.store = store

    def retrieve(
        self,
        question: str,
        top_k: int,
        knowledge_bases: list[str] | None = None,
        user_groups: list[str] | None = None,
        rerank_top_k: int = 12,
    ) -> list[RetrievedChunk]:
        query_tokens = expand_query(question)
        if not query_tokens:
            return []

        query_counts = Counter(query_tokens)
        candidates: list[RetrievedChunk] = []
        for chunk in self.store.load_chunks(knowledge_bases):
            if not can_access(chunk.allowed_groups, user_groups):
                continue
            lexical_score, matched_terms = self._score_chunk(chunk, query_counts)
            if lexical_score <= 0:
                continue
            rerank_score = self._rerank(chunk, query_counts, lexical_score)
            final_score = lexical_score * 0.65 + rerank_score * 0.35
            candidates.append(
                RetrievedChunk(
                    chunk=chunk,
                    score=final_score,
                    lexical_score=lexical_score,
                    rerank_score=rerank_score,
                    matched_terms=matched_terms,
                )
            )

        candidates.sort(key=lambda item: item.score, reverse=True)
        return candidates[: max(top_k, rerank_top_k)][:top_k]

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

    def _rerank(self, chunk: ChunkRecord, query_counts: Counter[str], lexical_score: float) -> float:
        chunk_tokens = set(tokenize(chunk.text))
        heading_tokens = set(tokenize(chunk.section_path))
        query_terms = set(query_counts.keys())
        overlap_ratio = len(chunk_tokens & query_terms) / max(1, len(query_terms))
        heading_ratio = len(heading_tokens & query_terms) / max(1, len(query_terms))
        compactness = min(1.0, 2000 / max(200, len(chunk.text)))
        return lexical_score + overlap_ratio * 0.6 + heading_ratio * 0.4 + compactness * 0.1
