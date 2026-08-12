from __future__ import annotations

from pathlib import Path
from uuid import NAMESPACE_URL, uuid5

from ..core.config import EnterpriseRAGConfig
from ..core.models import ChunkRecord, IngestResult, RetrievedChunk, SourceDocument
from ..ingestion.chunking import chunk_text, split_sections
from ..ingestion.loaders import load_sources
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
        self.retriever = HybridRetriever(self.store)
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

        for document in documents:
            doc = self._apply_overrides(document, knowledge_base, allowed_groups)
            chunks = self._build_chunks(doc)
            self.store.replace_document(doc, chunks)
            final_kbs.append(doc.knowledge_base)
            total_chunks += len(chunks)

        return IngestResult(
            documents_indexed=len(documents),
            chunks_indexed=total_chunks,
            knowledge_bases=sorted(set(final_kbs)),
            paths=[doc.path for doc in documents],
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
        return SourceDocument(
            source_id=document.source_id,
            knowledge_base=knowledge_base or document.knowledge_base,
            path=document.path,
            title=document.title,
            content=document.content,
            content_type=document.content_type,
            version=document.version,
            allowed_groups=normalize_groups(allowed_groups) if allowed_groups else document.allowed_groups,
            metadata=document.metadata,
        )

    def _build_chunks(self, document: SourceDocument) -> list[ChunkRecord]:
        records: list[ChunkRecord] = []
        sections = split_sections(document.content, document.content_type)
        for section_index, section in enumerate(sections):
            parts = chunk_text(section.text, self.config.chunk_size, self.config.chunk_overlap)
            for part_index, part in enumerate(parts):
                global_index = len(records)
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
                        allowed_groups=document.allowed_groups,
                        metadata={
                            "version": document.version,
                            "section_index": section_index,
                            "content_type": document.content_type,
                        },
                    )
                )
        return records
