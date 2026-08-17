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

                operation_logs = client.get("/api/operation-logs")
                self.assertEqual(operation_logs.status_code, 200)
                successful_log = operation_logs.json()["operation_logs"][0]
                self.assertEqual(successful_log["operation"], "ingest")
                self.assertEqual(successful_log["status"], "succeeded")
                self.assertEqual(successful_log["detail"]["documents_indexed"], 1)

                failed_ingest = client.post("/api/ingest", json={"path": str(tmp_path / "missing")})
                self.assertEqual(failed_ingest.status_code, 404)
                failed_log = client.get("/api/operation-logs").json()["operation_logs"][0]
                self.assertEqual(failed_log["status"], "failed")


if __name__ == "__main__":
    unittest.main()
