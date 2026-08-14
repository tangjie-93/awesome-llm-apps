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
                embedding_provider="local",
                embedding_model="local-hashing",
                embedding_base_url=None,
                embedding_api_key=None,
                default_groups=("public", "security", "hr", "it", "ops"),
                default_risk_levels=("low", "medium", "high"),
            )
            service = EnterpriseRAGService(config)
            ingest_result = service.ingest_path(kb_root)
            self.assertEqual(ingest_result.documents_indexed, 2)
            self.assertGreaterEqual(ingest_result.chunks_indexed, 2)
            self.assertEqual(ingest_result.documents_skipped, 0)
            self.assertEqual(ingest_result.documents_removed, 0)

            answer = service.agent.answer("How fast should we acknowledge the incident?")
            self.assertGreater(answer.confidence, 0)
            self.assertTrue(answer.citations)

            obsolete_path = kb_root / "security" / "obsolete.md"
            obsolete_path.write_text(
                "# Obsolete\n\nThis temporary document should be pruned.\n",
                encoding="utf-8",
            )
            obsolete_result = service.ingest_path(obsolete_path, knowledge_base="security")
            self.assertEqual(obsolete_result.documents_indexed, 1)

            obsolete_path.unlink()
            single_file_result = service.ingest_path(kb_root / "security" / "incident.md")
            self.assertEqual(single_file_result.documents_removed, 0)
            self.assertTrue(
                any(document["path"] == str(obsolete_path.resolve()) for document in service.list_documents("security"))
            )

            pruned_result = service.ingest_path(kb_root)
            self.assertEqual(pruned_result.documents_removed, 1)

            repeated_result = service.ingest_path(kb_root)
            self.assertEqual(repeated_result.documents_indexed, 0)
            self.assertEqual(repeated_result.documents_skipped, 2)

            duplicate_path = kb_root / "security" / "incident-copy.md"
            duplicate_path.write_text(
                "# Incident Response\n\nAcknowledge the incident within 15 minutes.\n",
                encoding="utf-8",
            )
            duplicate_result = service.ingest_path(duplicate_path, knowledge_base="security")
            self.assertEqual(duplicate_result.documents_indexed, 0)
            self.assertEqual(duplicate_result.documents_skipped, 1)
            self.assertEqual(duplicate_result.duplicate_paths, [str(duplicate_path.resolve())])

            cross_kb_duplicate_path = kb_root / "hr" / "incident-copy.md"
            cross_kb_duplicate_path.write_text(
                "# Incident Response\n\nAcknowledge the incident within 15 minutes.\n",
                encoding="utf-8",
            )
            cross_kb_result = service.ingest_path(cross_kb_duplicate_path, knowledge_base="hr")
            self.assertEqual(cross_kb_result.documents_indexed, 0)
            self.assertEqual(cross_kb_result.documents_skipped, 1)
            self.assertEqual(cross_kb_result.duplicate_paths, [str(cross_kb_duplicate_path.resolve())])

            chunks = service.store.load_chunks(["security"])
            self.assertTrue(chunks)
            self.assertTrue(all(chunk.embedding for chunk in chunks))


if __name__ == "__main__":
    unittest.main()
