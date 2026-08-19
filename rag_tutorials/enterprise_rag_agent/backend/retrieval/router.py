from __future__ import annotations

from collections import Counter

from .hybrid import tokenize
from storage.sqlite_store import SQLiteRAGStore


class KnowledgeBaseRouter:
    def __init__(self, store: SQLiteRAGStore) -> None:
        self.store = store

    def route(
        self,
        question: str,
        requested_kb: str | None = None,
        limit: int = 3,
        tenant_id: str = "default",
    ) -> list[str]:
        if requested_kb:
            return [requested_kb]

        knowledge_bases = self.store.list_knowledge_bases(tenant_id=tenant_id)
        if len(knowledge_bases) <= 1:
            return knowledge_bases

        query_tokens = set(tokenize(question))
        scores: list[tuple[float, str]] = []
        for kb in knowledge_bases:
            score = 0.0
            docs = self.store.list_documents(kb, tenant_id=tenant_id)
            for doc in docs[:5]:
                title_tokens = set(tokenize(str(doc["title"])))
                score += len(title_tokens & query_tokens) * 2
            if kb.lower() in question.lower():
                score += 2.0
            scores.append((score, kb))

        scores.sort(key=lambda item: item[0], reverse=True)
        routed = [kb for score, kb in scores if score > 0][:limit]
        return routed or knowledge_bases[:limit]
