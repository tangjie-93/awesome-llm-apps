from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(slots=True)
class SourceDocument:
    """原始接入文档的标准化表示。"""
    source_id: str
    knowledge_base: str
    path: str
    title: str
    content: str
    content_type: str
    content_hash: str
    tenant_id: str = "default"
    version: str = "1"
    allowed_groups: tuple[str, ...] = ("public",)
    risk_level: str = "low"
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class ChunkRecord:
    """切块后的最小检索单元。"""
    chunk_id: str
    source_id: str
    knowledge_base: str
    path: str
    title: str
    section_path: str
    chunk_index: int
    text: str
    token_count: int
    tenant_id: str = "default"
    embedding: list[float] = field(default_factory=list)
    allowed_groups: tuple[str, ...] = ("public",)
    risk_level: str = "low"
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class RetrievedChunk:
    """检索阶段返回的候选切块及其打分信息。"""
    chunk: ChunkRecord
    score: float
    lexical_score: float
    vector_score: float
    rerank_score: float
    matched_terms: list[str] = field(default_factory=list)
    rerank_reasons: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """把检索结果展开为可序列化字典。"""
        payload = asdict(self)
        payload["chunk"] = asdict(self.chunk)
        return payload


@dataclass(slots=True)
class IngestResult:
    """文档接入完成后的汇总结果。"""
    documents_indexed: int
    chunks_indexed: int
    documents_skipped: int
    documents_removed: int
    duplicate_paths: list[str]
    knowledge_bases: list[str]
    paths: list[str]

    def to_dict(self) -> dict[str, Any]:
        """把接入结果转成接口返回结构。"""
        return asdict(self)


@dataclass(slots=True)
class AnswerResult:
    """问答结果，包含答案、证据和置信度。"""
    question: str
    answer: str
    confidence: float
    knowledge_bases: list[str] = field(default_factory=list)
    citations: list[dict[str, Any]] = field(default_factory=list)
    evidence_snippets: list[dict[str, Any]] = field(default_factory=list)
    external_sources: list[dict[str, str]] = field(default_factory=list)
    tool_trace: list[str] = field(default_factory=list)
    clarifying_question: str | None = None
    sources_consulted: int = 0

    def to_dict(self) -> dict[str, Any]:
        """把问答结果转成接口返回结构。"""
        return asdict(self)


@dataclass(slots=True)
class EvaluationResult:
    """答案评估结果。"""
    question: str
    expected_answer: str | None
    actual_answer: str
    score: float
    notes: str

    def to_dict(self) -> dict[str, Any]:
        """把评估结果转成接口返回结构。"""
        return asdict(self)
