from __future__ import annotations

import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from enterprise_rag_agent.api.app import create_app


class ApiConfigTest(unittest.TestCase):
    def test_config_endpoint(self) -> None:
        client = TestClient(create_app())
        response = client.get("/api/config")
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload["default_knowledge_base"], "general")
        self.assertIn("security", payload["default_groups"])
        self.assertIn("high", payload["default_risk_levels"])
        self.assertEqual(payload["risk_by_group"]["security"], "high")

    def test_scope_endpoint(self) -> None:
        client = TestClient(create_app())
        response = client.get("/api/scope")
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertTrue(payload["business_domains"])
        self.assertIn("多租户隔离", payload["excluded_scopes"])
        self.assertEqual(payload["risk_by_group"]["ops"], "high")

    def test_config_env_overrides_phase_zero_lists(self) -> None:
        with patch.dict(
            "os.environ",
            {
                "ENTERPRISE_RAG_DEFAULT_GROUPS": "public,legal",
                "ENTERPRISE_RAG_RISK_LEVELS": "low,critical",
                "ENTERPRISE_RAG_RISK_BY_GROUP": "public:low,legal:critical",
                "ENTERPRISE_RAG_BUSINESS_DOMAINS": "legal:合同和合规知识",
                "ENTERPRISE_RAG_EXCLUDED_SCOPES": "自动合同审批",
            },
        ):
            client = TestClient(create_app())
            config_payload = client.get("/api/config").json()
            scope_payload = client.get("/api/scope").json()
        self.assertEqual(config_payload["default_groups"], ["public", "legal"])
        self.assertEqual(config_payload["default_risk_levels"], ["low", "critical"])
        self.assertEqual(config_payload["risk_by_group"]["legal"], "critical")
        self.assertEqual(scope_payload["business_domains"][0]["code"], "legal")
        self.assertEqual(scope_payload["excluded_scopes"], ["自动合同审批"])


if __name__ == "__main__":
    unittest.main()
