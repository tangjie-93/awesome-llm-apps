from __future__ import annotations

from collections.abc import Sequence
import re

from ..core.models import AnswerResult, RetrievedChunk
from ..llm.openai_compat import LLMMessage, OpenAIAnswerGenerator
from ..retrieval.hybrid import expand_query


class EnterpriseRAGAgent:
    def __init__(self, service: "EnterpriseRAGService") -> None:
        self.service = service

    def answer(
        self,
        question: str,
        knowledge_base: str | None = None,
        user_groups: list[str] | None = None,
        top_k: int | None = None,
    ) -> AnswerResult:
        retrieved = self.service.search(question, knowledge_base=knowledge_base, user_groups=user_groups, top_k=top_k)
        if not retrieved:
            external_sources = self.service.web_search(question)
            if external_sources:
                result = AnswerResult(
                    question=question,
                    answer="知识库未返回足够证据。以下是外部检索补充信息，请在使用前核验来源：\n"
                    + "\n".join(f"- {item['title']}: {item['snippet']}" for item in external_sources),
                    confidence=0.2,
                    external_sources=external_sources,
                    tool_trace=["knowledge_base_route", "retrieval", "web_fallback"],
                    sources_consulted=len(external_sources),
                )
                self._log_answer(result, knowledge_base, user_groups)
                return result
            result = AnswerResult(
                question=question,
                answer="未检索到足够证据，建议先补充知识库或缩小问题范围。",
                confidence=0.0,
                clarifying_question="你想查哪个知识库、制度域或业务流程？",
                tool_trace=["knowledge_base_route", "retrieval"],
            )
            self._log_answer(result, knowledge_base, user_groups)
            return result

        confidence = min(1.0, retrieved[0].score / 4.0)
        if confidence < self.service.config.low_confidence_threshold:
            result = self._low_confidence_result(question, retrieved, confidence)
            self._log_answer(result, knowledge_base, user_groups)
            return result

        answer = self._compose_answer(question, retrieved)
        result = AnswerResult(
            question=question,
            answer=answer,
            confidence=confidence,
            knowledge_bases=sorted({item.chunk.knowledge_base for item in retrieved}),
            citations=self._citations(retrieved),
            evidence_snippets=self._snippets(retrieved),
            tool_trace=["knowledge_base_route", "retrieval", "answer_composition"],
            sources_consulted=len(retrieved),
        )
        self._log_answer(result, knowledge_base, user_groups)
        return result

    def _compose_answer(self, question: str, retrieved: list[RetrievedChunk]) -> str:
        if self.service.config.enable_llm:
            generator = OpenAIAnswerGenerator(
                self.service.config.llm_model,
                api_key=self.service.config.llm_api_key,
                base_url=self.service.config.llm_base_url,
            )
            prompt = self._build_prompt(question, retrieved)
            return generator.generate(
                [
                    LLMMessage(
                        role="system",
                        content=(
                            f"You are the enterprise knowledge assistant for {self.service.config.company_name}. "
                            "Answer only from the provided evidence. Keep the answer concise, actionable, and cite the evidence labels."
                        ),
                    ),
                    LLMMessage(role="user", content=prompt),
                ]
            ).strip()

        lines = []
        for item in retrieved[:3]:
            text = self._compress_chunk(question, item, 900)
            lines.append(f"- {text[:260].rstrip()}" + ("..." if len(text) > 260 else ""))
        labels = ", ".join(self._citation_label(item) for item in retrieved[:3])
        return "根据当前证据，可归纳为：\n" + "\n".join(lines) + f"\n\n参考：{labels}"

    def _build_prompt(self, question: str, retrieved: list[RetrievedChunk]) -> str:
        blocks = []
        for index, item in enumerate(retrieved, start=1):
            compressed = self._compress_chunk(question, item, self.service.config.context_max_chars)
            blocks.append(f"[{index}] {self._citation_label(item)}\n{compressed}")
        return f"Question: {question}\n\nEvidence:\n" + "\n\n".join(blocks)

    def _low_confidence_result(self, question: str, retrieved: list[RetrievedChunk], confidence: float) -> AnswerResult:
        return AnswerResult(
            question=question,
            answer="当前证据更像是相关背景，不足以直接下结论。",
            confidence=confidence,
            knowledge_bases=sorted({item.chunk.knowledge_base for item in retrieved}),
            citations=self._citations(retrieved),
            evidence_snippets=self._snippets(retrieved),
            tool_trace=["knowledge_base_route", "retrieval"],
            clarifying_question="你要我优先查制度、流程、权限，还是某个知识库？",
            sources_consulted=len(retrieved),
        )

    def _citations(self, retrieved: list[RetrievedChunk]) -> list[dict[str, object]]:
        citations: list[dict[str, object]] = []
        for item in retrieved:
            citations.append(
                {
                    "knowledge_base": item.chunk.knowledge_base,
                    "source": item.chunk.path,
                    "title": item.chunk.title,
                    "section_path": item.chunk.section_path,
                    "chunk_index": item.chunk.chunk_index,
                    "risk_level": item.chunk.risk_level,
                    "score": round(item.score, 4),
                    "matched_terms": item.matched_terms,
                }
            )
        return citations

    def _snippets(self, retrieved: list[RetrievedChunk]) -> list[dict[str, object]]:
        return [
            {
                "knowledge_base": item.chunk.knowledge_base,
                "source": item.chunk.path,
                "section_path": item.chunk.section_path,
                "risk_level": item.chunk.risk_level,
                "snippet": self._compress_chunk(item.chunk.title, item, 320),
            }
            for item in retrieved[:3]
        ]

    def _compress_chunk(self, question: str, item: RetrievedChunk, budget: int) -> str:
        """保留与问题最相关的句子，并在固定字符预算内压缩证据上下文。"""
        text = re.sub(r"\s+", " ", item.chunk.text).strip()
        if len(text) <= budget:
            return text

        query_terms = set(expand_query(question))
        sentences = [part.strip() for part in re.split(r"(?<=[。！？.!?])\s+", text) if part.strip()]
        ranked = sorted(
            enumerate(sentences),
            key=lambda pair: (
                sum(term in pair[1].lower() for term in query_terms),
                -pair[0],
            ),
            reverse=True,
        )
        selected: list[tuple[int, str]] = []
        used = 0
        for index, sentence in ranked:
            if used + len(sentence) + 1 > budget:
                continue
            selected.append((index, sentence))
            used += len(sentence) + 1
        if not selected:
            return text[:budget].rstrip()
        selected.sort(key=lambda pair: pair[0])
        return " ".join(sentence for _, sentence in selected)

    def _citation_label(self, item: RetrievedChunk) -> str:
        return f"{item.chunk.knowledge_base} / {item.chunk.title} / {item.chunk.section_path} / chunk {item.chunk.chunk_index}"

    def _log_answer(self, result: AnswerResult, knowledge_base: str | None, user_groups: Sequence[str] | None) -> None:
        self.service.store.log_answer(
            result.question,
            result.answer,
            result.confidence,
            result.citations,
            {
                "knowledge_base": knowledge_base,
                "user_groups": list(user_groups or []),
                "requires_human_review": any(citation.get("risk_level") == "high" for citation in result.citations),
                "high_risk_policy": self.service.config.high_risk_policy,
            },
        )
