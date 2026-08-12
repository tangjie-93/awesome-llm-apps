from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(slots=True)
class SourceDocument:
    source_id: str
    knowledge_base: str
    path: str
    title: str
    content: str
    content_type: str
    version: str = "1"
    allowed_groups: tuple[str, ...] = ("public",)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class ChunkRecord:
    chunk_id: str
    source_id: str
    knowledge_base: str
    path: str
    title: str
    section_path: str
    chunk_index: int
    text: str
    token_count: int
    allowed_groups: tuple[str, ...] = ("public",)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class RetrievedChunk:
    chunk: ChunkRecord
    score: float
    lexical_score: float
    rerank_score: float
    matched_terms: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["chunk"] = asdict(self.chunk)
        return payload


@dataclass(slots=True)
class IngestResult:
    documents_indexed: int
    chunks_indexed: int
    knowledge_bases: list[str]
    paths: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class AnswerResult:
    question: str
    answer: str
    confidence: float
    knowledge_bases: list[str] = field(default_factory=list)
    citations: list[dict[str, Any]] = field(default_factory=list)
    evidence_snippets: list[dict[str, Any]] = field(default_factory=list)
    clarifying_question: str | None = None
    sources_consulted: int = 0

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class EvaluationResult:
    question: str
    expected_answer: str | None
    actual_answer: str
    score: float
    notes: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

