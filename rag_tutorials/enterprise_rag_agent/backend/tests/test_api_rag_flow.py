from __future__ import annotations

from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from enterprise_rag_agent.api.app import create_app


class ApiRagFlowTest(unittest.TestCase):
    def test_ingest_search_ask_and_operation_logs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            documents_path = tmp_path / "documents"
            documents_path.mkdir()
            (documents_path / "incident.md").write_text(
                "# Incident Response\n\nAcknowledge the incident within 15 minutes.\n",
                encoding="utf-8",
            )

            with patch.dict(
                "os.environ",
                {
                    "ENTERPRISE_RAG_DB_PATH": str(tmp_path / "rag.sqlite3"),
                    "ENTERPRISE_RAG_ENABLE_LLM": "false",
                    "ENTERPRISE_RAG_EMBEDDING_PROVIDER": "local",
                    "ENTERPRISE_RAG_EMBEDDING_MODEL": "local-hashing",
                },
            ):
                client = TestClient(create_app())
                ingest = client.post(
                    "/api/ingest",
                    json={
                        "path": str(documents_path),
                        "knowledge_base": "security",
                        "allowed_groups": ["public"],
                    },
                )
                self.assertEqual(ingest.status_code, 200)
                self.assertEqual(ingest.json()["documents_indexed"], 1)

                documents = client.get("/api/documents")
                self.assertEqual(documents.status_code, 200)
                self.assertEqual(documents.json()["documents"][0]["knowledge_base"], "security")

                search = client.post(
                    "/api/search",
                    json={"question": "How fast should we acknowledge the incident?", "user_groups": ["public"]},
                )
                self.assertEqual(search.status_code, 200)
                self.assertTrue(search.json()["results"])

                answer = client.post(
                    "/api/ask",
                    json={"question": "How fast should we acknowledge the incident?", "user_groups": ["public"]},
                )
                self.assertEqual(answer.status_code, 200)
                self.assertTrue(answer.json()["citations"])
                self.assertTrue(answer.json()["evidence_snippets"])
                self.assertTrue(answer.json()["tool_trace"])

                feedback = client.post("/api/feedback", json={"rating": 5, "comment": "Helpful"})
                self.assertEqual(feedback.status_code, 200)
                diagnostics = client.get("/api/diagnostics")
                self.assertEqual(diagnostics.status_code, 200)
                self.assertEqual(diagnostics.json()["feedback"]["count"], 1)
                self.assertFalse(diagnostics.json()["web_fallback_enabled"])
                web_search = client.post("/api/web-search", json={"question": "What is the incident policy?"})
                self.assertEqual(web_search.status_code, 200)
                self.assertFalse(web_search.json()["enabled"])

                operation_logs = client.get("/api/operation-logs")
                self.assertEqual(operation_logs.status_code, 200)
                successful_log = operation_logs.json()["operation_logs"][0]
                self.assertEqual(successful_log["operation"], "ingest")
                self.assertEqual(successful_log["status"], "succeeded")
                self.assertEqual(successful_log["detail"]["documents_indexed"], 1)

                replay = client.post(f"/api/operation-logs/{successful_log['id']}/replay")
                self.assertEqual(replay.status_code, 200)
                self.assertEqual(replay.json()["documents_skipped"], 1)

                retrieval_evaluation = client.post(
                    "/api/evaluate-retrieval",
                    json={
                        "cases": [
                            {
                                "question": "How fast should we acknowledge the incident?",
                                "expected_terms": ["15 minutes"],
                                "expected_sources": ["incident.md"],
                            }
                        ]
                    },
                )
                self.assertEqual(retrieval_evaluation.status_code, 200)
                self.assertEqual(retrieval_evaluation.json()["hit_rate"], 1.0)
                self.assertEqual(retrieval_evaluation.json()["mrr"], 1.0)

                failed_ingest = client.post("/api/ingest", json={"path": str(tmp_path / "missing")})
                self.assertEqual(failed_ingest.status_code, 404)
                failed_log = client.get("/api/operation-logs").json()["operation_logs"][0]
                self.assertEqual(failed_log["status"], "failed")

                missing_replay = client.post("/api/operation-logs/999/replay")
                self.assertEqual(missing_replay.status_code, 404)


if __name__ == "__main__":
    unittest.main()
