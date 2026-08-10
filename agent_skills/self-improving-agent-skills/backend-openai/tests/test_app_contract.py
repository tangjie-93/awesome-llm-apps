import os
import sys
import unittest


BACKEND_DIR = os.path.dirname(os.path.dirname(__file__))
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

from fastapi.testclient import TestClient

import app as app_module


class AppContractTests(unittest.TestCase):
    def setUp(self):
        app_module.sessions.clear()
        self.client = TestClient(app_module.app)

    def test_health_endpoint(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "healthy", "provider": "openai"})

    def test_create_session_from_skill_files_requires_skill_md_and_metadata(self):
        result = app_module.create_session_from_files(
            {"demo/SKILL.md": "---\nname: demo\n---\n# Demo"},
            ["demo/SKILL.md"],
        )

        self.assertIn("session_id", result)
        self.assertEqual(result["metadata"]["name"], "demo")
        self.assertIn(result["session_id"], app_module.sessions)

    def test_api_key_request_accepts_openai_and_legacy_key_names(self):
        openai_request = app_module.AnalyzeRequest(session_id="s1", api_key="openai-key")
        legacy_request = app_module.AnalyzeRequest(session_id="s2", gemini_api_key="legacy-key")
        explicit_request = app_module.StartRequest(openai_api_key="explicit-key", model="gpt-5")

        self.assertEqual(openai_request.api_key_value, "openai-key")
        self.assertEqual(legacy_request.api_key_value, "legacy-key")
        self.assertEqual(explicit_request.api_key_value, "explicit-key")
        self.assertEqual(explicit_request.model, "gpt-5")

    def test_update_config_and_status_contract(self):
        created = app_module.create_session_from_files(
            {"SKILL.md": "---\nname: demo\n---\n# Demo"},
            ["SKILL.md"],
        )

        response = self.client.post(
            "/api/update-config",
            json={
                "session_id": created["session_id"],
                "scenarios": [{"id": 1, "input": "Use it"}],
                "evals": [{"id": 1, "question": "Good?"}],
            },
        )
        status = self.client.get(f"/api/status/{created['session_id']}")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})
        self.assertEqual(status.status_code, 200)
        self.assertEqual(status.json()["status"], "configured")


if __name__ == "__main__":
    unittest.main()
