from __future__ import annotations

import unittest

from fastapi.testclient import TestClient

from enterprise_rag_agent.api.app import create_app


class ApiConfigTest(unittest.TestCase):
    def test_config_endpoint(self) -> None:
        client = TestClient(create_app())
        response = client.get("/config")
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload["default_knowledge_base"], "general")
        self.assertIn("security", payload["default_groups"])
        self.assertIn("high", payload["default_risk_levels"])


if __name__ == "__main__":
    unittest.main()
