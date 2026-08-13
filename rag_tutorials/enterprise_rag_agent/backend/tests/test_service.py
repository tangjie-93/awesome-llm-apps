from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from enterprise_rag_agent.core.config import EnterpriseRAGConfig
from enterprise_rag_agent.application.service import EnterpriseRAGService


class EnterpriseRAGServiceTest(unittest.TestCase):
    def test_ingest_and_answer(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            kb_root = tmp_path / "kb"
            (kb_root / "security").mkdir(parents=True)
            (kb_root / "hr").mkdir(parents=True)
            (kb_root / "security" / "incident.md").write_text(
                "# Incident Response\n\nAcknowledge the incident within 15 minutes.\n",
                encoding="utf-8",
            )
            (kb_root / "hr" / "onboarding.md").write_text(
                "# Onboarding\n\nNew hires must complete security training on day one.\n",
                encoding="utf-8",
            )

            config = EnterpriseRAGConfig(
                company_name="TestCo",
                db_path=tmp_path / "rag.sqlite3",
                default_knowledge_base="general",
                chunk_size=200,
                chunk_overlap=40,
                top_k=3,
                rerank_top_k=6,
                enable_llm=False,
                llm_model="gpt-4o-mini",
                llm_provider="chatgpt",
                llm_base_url="https://api.openai.com/v1",
                llm_api_key=None,
                default_groups=("public", "security", "hr", "it", "ops"),
                default_risk_levels=("low", "medium", "high"),
            )
            service = EnterpriseRAGService(config)
            ingest_result = service.ingest_path(kb_root)
            self.assertEqual(ingest_result.documents_indexed, 2)
            self.assertGreaterEqual(ingest_result.chunks_indexed, 2)

            answer = service.agent.answer("How fast should we acknowledge the incident?")
            self.assertGreater(answer.confidence, 0)
            self.assertTrue(answer.citations)


if __name__ == "__main__":
    unittest.main()
