from __future__ import annotations

from pathlib import Path
from uuid import NAMESPACE_URL, uuid5

from ..core.config import EnterpriseRAGConfig
from ..core.models import ChunkRecord, IngestResult, RetrievedChunk, SourceDocument
from ..ingestion.chunking import SectionBlock, chunk_text, split_sections
from ..ingestion.loaders import load_sources
from ..retrieval.embeddings import create_embedding_generator
from ..retrieval.hybrid import HybridRetriever
from ..retrieval.router import KnowledgeBaseRouter
from ..security.permissions import normalize_groups
from ..storage.sqlite_store import SQLiteRAGStore
from .agent import EnterpriseRAGAgent


class EnterpriseRAGService:
    def __init__(self, config: EnterpriseRAGConfig) -> None:
        self.config = config
        self.store = SQLiteRAGStore(config.db_path)
        self.router = KnowledgeBaseRouter(self.store)
        self.embedding_generator = create_embedding_generator(
            config.embedding_provider,
            config.embedding_model,
            config.embedding_api_key,
            config.embedding_base_url,
        )
        self.retriever = HybridRetriever(self.store, self.embedding_generator)
        self.agent = EnterpriseRAGAgent(self)

    def ingest_path(
        self,
        target: Path,
        knowledge_base: str | None = None,
        allowed_groups: list[str] | None = None,
    ) -> IngestResult:
        documents = load_sources(target, self.config.default_knowledge_base)
        final_kbs: list[str] = []
        total_chunks = 0
        skipped = 0
        removed = 0
        duplicate_paths: list[str] = []
        indexed_paths: list[str] = []
        active_source_ids: set[str] = set()

        for document in documents:
            doc = self._apply_overrides(document, knowledge_base, allowed_groups)
            current = self.store.get_document(doc.source_id)
            duplicate = self.store.find_duplicate_document(doc.content_hash, doc.source_id)
            if duplicate:
                skipped += 1
                duplicate_paths.append(doc.path)
                if self.store.delete_document(doc.source_id):
                    removed += 1
                continue

            if (
                current
                and current["content_hash"] == doc.content_hash
                and current["knowledge_base"] == doc.knowledge_base
                and tuple(current["allowed_groups"]) == doc.allowed_groups
            ):
                skipped += 1
                active_source_ids.add(doc.source_id)
                continue

            chunks = self._build_chunks(doc)
            self.store.replace_document(doc, chunks)
            final_kbs.append(doc.knowledge_base)
            total_chunks += len(chunks)
            indexed_paths.append(doc.path)
            active_source_ids.add(doc.source_id)

        if target.is_dir():
            removed += self.store.prune_documents_under_path(
                target,
                active_source_ids,
                knowledge_base=knowledge_base,
            )

        return IngestResult(
            documents_indexed=len(indexed_paths),
            chunks_indexed=total_chunks,
            documents_skipped=skipped,
            documents_removed=removed,
            duplicate_paths=duplicate_paths,
            knowledge_bases=sorted(set(final_kbs)),
            paths=indexed_paths,
        )

    def search(
        self,
        question: str,
        knowledge_base: str | None = None,
        user_groups: list[str] | None = None,
        top_k: int | None = None,
    ) -> list[RetrievedChunk]:
        routed = self.router.route(question, requested_kb=knowledge_base, limit=3)
        return self.retriever.retrieve(
            question,
            top_k=top_k or self.config.top_k,
            knowledge_bases=routed,
            user_groups=user_groups,
            rerank_top_k=self.config.rerank_top_k,
        )

    def stats(self) -> dict[str, object]:
        stats = self.store.stats()
        stats["knowledge_bases"] = self.store.list_knowledge_bases()
        stats["company_name"] = self.config.company_name
        stats["db_path"] = str(self.config.db_path)
        return stats

    def list_documents(self, knowledge_base: str | None = None) -> list[dict[str, object]]:
        return self.store.list_documents(knowledge_base)

    def list_answer_logs(self) -> list[dict[str, object]]:
        return self.store.list_answer_logs()

    def list_evaluation_logs(self) -> list[dict[str, object]]:
        return self.store.list_evaluation_logs()

    def evaluate_answer(self, question: str, expected_answer: str | None, actual_answer: str) -> dict[str, object]:
        from ..evaluation.scorer import score_answer

        score, notes = score_answer(expected_answer, actual_answer)
        self.store.log_evaluation(question, expected_answer, actual_answer, score, notes)
        return {"question": question, "expected_answer": expected_answer, "actual_answer": actual_answer, "score": score, "notes": notes}

    def _apply_overrides(
        self,
        document: SourceDocument,
        knowledge_base: str | None,
        allowed_groups: list[str] | None,
    ) -> SourceDocument:
        final_groups = normalize_groups(allowed_groups) if allowed_groups else document.allowed_groups
        risk_level = self._infer_risk_level(final_groups, knowledge_base or document.knowledge_base)
        return SourceDocument(
            source_id=document.source_id,
            knowledge_base=knowledge_base or document.knowledge_base,
            path=document.path,
            title=document.title,
            content=document.content,
            content_type=document.content_type,
            content_hash=document.content_hash,
            version=document.version,
            allowed_groups=final_groups,
            risk_level=risk_level,
            metadata={**document.metadata, "risk_level": risk_level},
        )

    def _build_chunks(self, document: SourceDocument) -> list[ChunkRecord]:
        pending: list[tuple[int, int, str, SectionBlock]] = []
        sections = split_sections(document.content, document.content_type)
        for section_index, section in enumerate(sections):
            parts = chunk_text(section.text, self.config.chunk_size, self.config.chunk_overlap)
            for part_index, part in enumerate(parts):
                pending.append((section_index, part_index, part, section))

        embeddings = self.embedding_generator.embed_texts([part for _, _, part, _ in pending])
        records: list[ChunkRecord] = []
        for global_index, ((section_index, part_index, part, section), embedding) in enumerate(
            zip(pending, embeddings, strict=True)
        ):
            chunk_id = str(uuid5(NAMESPACE_URL, f"{document.source_id}:{section_index}:{part_index}:{part[:80]}"))
            records.append(
                ChunkRecord(
                    chunk_id=chunk_id,
                    source_id=document.source_id,
                    knowledge_base=document.knowledge_base,
                    path=document.path,
                    title=document.title,
                    section_path=section.section_path,
                    chunk_index=global_index,
                    text=part,
                    token_count=len(part.split()),
                    embedding=embedding,
                    allowed_groups=document.allowed_groups,
                    risk_level=document.risk_level,
                    metadata={
                        "version": document.version,
                        "section_index": section_index,
                        "content_type": document.content_type,
                        "risk_level": document.risk_level,
                    },
                )
            )
        return records

    def _infer_risk_level(self, allowed_groups: tuple[str, ...], knowledge_base: str) -> str:
        """根据权限组和知识库推断阶段 0 文档风险等级。"""
        candidates = [self.config.risk_by_group.get(group, "") for group in allowed_groups]
        candidates.append(self.config.risk_by_group.get(knowledge_base, ""))
        for risk_level in ("high", "medium", "low"):
            if risk_level in candidates:
                return risk_level
        return "low"
