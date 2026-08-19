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
from ..retrieval.web_fallback import search_web
from ..security.permissions import can_access, normalize_groups
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
        self.retriever = HybridRetriever(
            self.store,
            self.embedding_generator,
            rerank_provider=config.rerank_provider,
            rerank_url=config.rerank_url,
            rerank_api_key=config.rerank_api_key,
        )
        self.agent = EnterpriseRAGAgent(self)

    def ingest_path(
        self,
        target: Path,
        knowledge_base: str | None = None,
        allowed_groups: list[str] | None = None,
        tenant_id: str = "default",
    ) -> IngestResult:
        documents = load_sources(target, self.config.default_knowledge_base, tenant_id=tenant_id)
        final_kbs: list[str] = []
        total_chunks = 0
        skipped = 0
        removed = 0
        duplicate_paths: list[str] = []
        indexed_paths: list[str] = []
        active_source_ids: set[str] = set()

        for document in documents:
            doc = self._apply_overrides(document, knowledge_base, allowed_groups)
            current = self.store.get_document(doc.source_id, tenant_id=tenant_id)
            duplicate = self.store.find_duplicate_document(doc.content_hash, doc.source_id, tenant_id=tenant_id)
            if duplicate:
                skipped += 1
                duplicate_paths.append(doc.path)
                if self.store.delete_document(doc.source_id, tenant_id=tenant_id):
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
                tenant_id=tenant_id,
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
        tenant_id: str = "default",
    ) -> list[RetrievedChunk]:
        routed = self.router.route(question, requested_kb=knowledge_base, limit=3, tenant_id=tenant_id)
        retrieved = self.retriever.retrieve(
            question,
            top_k=top_k or self.config.top_k,
            knowledge_bases=routed,
            user_groups=user_groups,
            rerank_top_k=self.config.rerank_top_k,
            tenant_id=tenant_id,
        )
        visible = [
            item
            for item in retrieved
            if can_access(item.chunk.allowed_groups, user_groups)
        ]
        visible_chunk_ids = {
            chunk.chunk_id
            for chunk in self.store.load_chunks(routed, tenant_id)
            if can_access(chunk.allowed_groups, user_groups)
        }
        graph_chunks, graph_entities = self.store.graph_candidates(
            question,
            routed,
            tenant_id,
            allowed_chunk_ids=visible_chunk_ids,
        )
        existing_ids = {item.chunk.chunk_id for item in visible}
        for chunk in graph_chunks:
            if chunk.chunk_id in existing_ids or not can_access(chunk.allowed_groups, user_groups):
                continue
            visible.append(
                RetrievedChunk(
                    chunk=chunk,
                    score=0.4,
                    lexical_score=0.0,
                    vector_score=0.0,
                    rerank_score=0.4,
                    matched_terms=graph_entities,
                    rerank_reasons=["轻量知识图谱多跳关联"],
                )
            )
        visible.sort(key=lambda item: item.score, reverse=True)
        return visible[: top_k or self.config.top_k]

    def stats(self, tenant_id: str = "default") -> dict[str, object]:
        stats = self.store.stats_for_tenant(tenant_id)
        stats["knowledge_bases"] = self.store.list_knowledge_bases(tenant_id=tenant_id)
        stats["company_name"] = self.config.company_name
        stats["db_path"] = str(self.config.db_path)
        return stats

    def list_documents(self, knowledge_base: str | None = None, tenant_id: str = "default") -> list[dict[str, object]]:
        return self.store.list_documents(knowledge_base, tenant_id=tenant_id)

    def list_answer_logs(self, tenant_id: str = "default") -> list[dict[str, object]]:
        return self.store.list_answer_logs(tenant_id=tenant_id)

    def list_evaluation_logs(self, tenant_id: str = "default") -> list[dict[str, object]]:
        return self.store.list_evaluation_logs(tenant_id=tenant_id)

    def list_operation_logs(self, tenant_id: str = "default") -> list[dict[str, object]]:
        return self.store.list_operation_logs(tenant_id=tenant_id)

    def evaluate_answer(self, question: str, expected_answer: str | None, actual_answer: str) -> dict[str, object]:
        from ..evaluation.scorer import score_answer

        score, notes = score_answer(expected_answer, actual_answer)
        self.store.log_evaluation(question, expected_answer, actual_answer, score, notes)
        return {"question": question, "expected_answer": expected_answer, "actual_answer": actual_answer, "score": score, "notes": notes}

    def evaluate_retrieval(self, cases: list[dict[str, object]] | None = None) -> dict[str, object]:
        """运行稳定的召回样例，返回命中率、MRR 和每条样例的解释结果。"""
        from ..evaluation.benchmark import DEFAULT_RETRIEVAL_CASES, RetrievalCase

        selected = [
            RetrievalCase(
                question=str(item["question"]),
                expected_terms=tuple(str(term) for term in item.get("expected_terms", [])),
                expected_sources=tuple(str(source) for source in item.get("expected_sources", [])),
            )
            for item in (cases or [])
        ] or list(DEFAULT_RETRIEVAL_CASES)
        results: list[dict[str, object]] = []
        reciprocal_ranks: list[float] = []
        for case in selected:
            retrieved = self.search(case.question, top_k=self.config.top_k)
            matched = [
                item for item in retrieved
                if any(term.lower() in item.chunk.text.lower() for term in case.expected_terms)
                or any(source.lower() in item.chunk.path.lower() for source in case.expected_sources)
            ]
            rank = next((index + 1 for index, item in enumerate(retrieved) if item in matched), 0)
            reciprocal_ranks.append(1 / rank if rank else 0.0)
            results.append({
                "question": case.question,
                "expected_terms": list(case.expected_terms),
                "expected_sources": list(case.expected_sources),
                "hit": bool(matched),
                "rank": rank,
                "results": [item.to_dict() for item in retrieved],
            })
        hits = sum(bool(item["hit"]) for item in results)
        total = len(results)
        return {
            "total": total,
            "hit_rate": round(hits / total, 4) if total else 0.0,
            "mrr": round(sum(reciprocal_ranks) / total, 4) if total else 0.0,
            "results": results,
        }

    def web_search(self, question: str, limit: int = 3) -> list[dict[str, str]]:
        """通过受控的外部检索 provider 补充低置信度回答。"""
        return search_web(question, self.config, limit)

    def knowledge_graph(
        self,
        knowledge_base: str | None = None,
        user_groups: list[str] | None = None,
        tenant_id: str = "default",
    ) -> dict[str, object]:
        """返回通过当前权限过滤后的轻量知识图谱只读视图。"""
        knowledge_bases = [knowledge_base] if knowledge_base else None
        visible_chunk_ids = {
            chunk.chunk_id
            for chunk in self.store.load_chunks(knowledge_bases, tenant_id)
            if can_access(chunk.allowed_groups, user_groups)
        }
        overview = self.store.graph_overview(
            knowledge_bases,
            tenant_id,
            allowed_chunk_ids=visible_chunk_ids,
        )
        if not visible_chunk_ids:
            return {"entities": [], "relations": [], "entity_count": 0, "relation_count": 0}
        return overview

    def query_knowledge_graph(
        self,
        question: str,
        knowledge_base: str | None = None,
        user_groups: list[str] | None = None,
        max_hops: int = 2,
        limit: int = 50,
        tenant_id: str = "default",
    ) -> dict[str, object]:
        """执行当前用户可见范围内的图谱多跳查询。"""
        knowledge_bases = [knowledge_base] if knowledge_base else None
        visible_chunk_ids = {
            chunk.chunk_id
            for chunk in self.store.load_chunks(knowledge_bases, tenant_id)
            if can_access(chunk.allowed_groups, user_groups)
        }
        result = self.store.graph_query(
            question,
            knowledge_bases,
            tenant_id,
            max_hops=max_hops,
            limit=limit,
            allowed_chunk_ids=visible_chunk_ids,
        )
        result["query"] = question
        result["max_hops"] = min(max(max_hops, 1), 3)
        return result

    def diagnostics(self, tenant_id: str = "default") -> dict[str, object]:
        """汇总租户诊断指标，并生成只读、可解释的运行建议。"""
        stats = self.stats(tenant_id)
        low_confidence_answers = self.store.count_low_confidence_answers(
            self.config.low_confidence_threshold,
            tenant_id,
        )
        feedback = self.store.feedback_summary(tenant_id)
        return {
            "documents": stats["documents"],
            "chunks": stats["chunks"],
            "knowledge_bases": stats["knowledge_bases"],
            "low_confidence_answers": low_confidence_answers,
            "feedback": feedback,
            "web_fallback_enabled": self.config.web_fallback_enabled,
            "suggestions": self._build_diagnostic_suggestions(
                chunks=int(stats["chunks"]),
                low_confidence_answers=low_confidence_answers,
                negative_feedback=int(feedback["negative_count"]),
                web_fallback_enabled=self.config.web_fallback_enabled,
            ),
        }

    def _build_diagnostic_suggestions(
        self,
        chunks: int,
        low_confidence_answers: int,
        negative_feedback: int,
        web_fallback_enabled: bool,
    ) -> list[dict[str, str]]:
        """根据运行指标生成稳定的只读诊断建议，不触发自动调参或自动改写数据。"""
        suggestions: list[dict[str, str]] = []
        if chunks == 0:
            suggestions.append({
                "code": "empty_index",
                "severity": "critical",
                "title": "知识库没有可检索切块",
                "detail": "当前租户没有已索引切块，问答无法获得本地知识库证据。",
                "action": "先导入文档并确认切块数量大于 0，再进行问答验证。",
            })
        if low_confidence_answers > 0:
            suggestions.append({
                "code": "low_confidence_answers",
                "severity": "warning",
                "title": "存在低置信度回答",
                "detail": f"当前租户有 {low_confidence_answers} 条回答低于置信度阈值。",
                "action": "检查文档切块质量、召回结果和问题改写记录。",
            })
        if negative_feedback > 0:
            suggestions.append({
                "code": "negative_feedback",
                "severity": "warning",
                "title": "存在负向反馈",
                "detail": f"当前租户有 {negative_feedback} 条评分不高于 2 分的反馈。",
                "action": "回放对应问答并核对证据，不自动调整排序或模型参数。",
            })
        if not web_fallback_enabled:
            suggestions.append({
                "code": "web_fallback_disabled",
                "severity": "info",
                "title": "Web 回退未启用",
                "detail": "当前问答只使用本地知识库，未配置受控的外部检索补充。",
                "action": "仅在完成外部服务配置、访问控制和审计评估后启用。",
            })
        if not suggestions:
            suggestions.append({
                "code": "healthy",
                "severity": "info",
                "title": "当前没有发现明显诊断信号",
                "detail": "索引、置信度和反馈指标暂未触发预设诊断规则。",
                "action": "继续观察线上反馈和低置信度回答趋势。",
            })
        return suggestions

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
            tenant_id=document.tenant_id,
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
                    tenant_id=document.tenant_id,
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
