from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RetrievalCase:
    """一条用于离线验证召回命中的问题样例。"""

    question: str
    expected_terms: tuple[str, ...]
    expected_sources: tuple[str, ...] = ()


DEFAULT_RETRIEVAL_CASES: tuple[RetrievalCase, ...] = (
    RetrievalCase(
        question="How fast should we acknowledge the incident?",
        expected_terms=("incident", "15 minutes"),
        expected_sources=("incident.md",),
    ),
    RetrievalCase(
        question="What must new hires complete on day one?",
        expected_terms=("security training", "day one"),
        expected_sources=("onboarding.md",),
    ),
    RetrievalCase(
        question="What is the backup retention policy?",
        expected_terms=("backup", "retention"),
        expected_sources=("backup_policy.md",),
    ),
)
