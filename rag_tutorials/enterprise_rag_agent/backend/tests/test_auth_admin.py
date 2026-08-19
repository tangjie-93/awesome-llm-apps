from __future__ import annotations

from datetime import datetime, timedelta, timezone
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import jwt
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from fastapi.testclient import TestClient

from api.app import create_app


class AuthAdminTest(unittest.TestCase):
    def test_admin_endpoints_require_jwt_and_support_audit_cleanup(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
            public_key = private_key.public_key()
            token = jwt.encode(
                {
                    "sub": "alice",
                    "groups": ["rag-admin"],
                    "iss": "https://issuer.example.com",
                    "aud": "enterprise-rag",
                    "tenant_id": "tenant-a",
                    "exp": datetime.now(timezone.utc) + timedelta(minutes=10),
                },
                private_key,
                algorithm="RS256",
                headers={"kid": "test-key"},
            )
            auditor_token = jwt.encode(
                {
                    "sub": "bob",
                    "groups": ["security"],
                    "iss": "https://issuer.example.com",
                    "aud": "enterprise-rag",
                    "tenant_id": "tenant-a",
                    "exp": datetime.now(timezone.utc) + timedelta(minutes=10),
                },
                private_key,
                algorithm="RS256",
                headers={"kid": "test-key"},
            )

            class FakeJwkClient:
                def __init__(self, _: str) -> None:
                    pass

                def get_signing_key_from_jwt(self, _: str):
                    return type("SigningKey", (), {"key": public_key})()

            with patch.dict(
                "os.environ",
                {
                    "ENTERPRISE_RAG_DB_PATH": str(tmp_path / "rag.sqlite3"),
                    "ENTERPRISE_RAG_ENABLE_LLM": "false",
                    "ENTERPRISE_RAG_EMBEDDING_PROVIDER": "local",
                    "ENTERPRISE_RAG_AUTH_MODE": "jwt",
                    "ENTERPRISE_RAG_JWT_JWKS_URL": "https://issuer.example.com/.well-known/jwks.json",
                    "ENTERPRISE_RAG_JWT_ISSUER": "https://issuer.example.com",
                    "ENTERPRISE_RAG_JWT_AUDIENCE": "enterprise-rag",
                    "ENTERPRISE_RAG_ADMIN_GROUPS": "rag-admin",
                    "ENTERPRISE_RAG_AUDIT_APPROVAL_TOKEN": "approved-by-security",
                },
            ):
                with patch("security.auth.PyJWKClient", FakeJwkClient):
                    client = TestClient(create_app())
                    unauthorized = client.get("/api/admin/usage")
                    self.assertEqual(unauthorized.status_code, 401)
                    usage = client.get("/api/admin/usage", headers={"Authorization": f"Bearer {token}"})
                    self.assertEqual(usage.status_code, 200)
                    self.assertIn("usage", usage.json())
                    self.assertEqual(usage.json()["rerank_provider"], "heuristic")

                    request = client.get("/api/config", headers={"Authorization": f"Bearer {token}"})
                    self.assertEqual(request.status_code, 200)
                    self.assertEqual(request.json()["auth_mode"], "jwt")

                    session = client.get("/api/session", headers={"Authorization": f"Bearer {token}"})
                    self.assertEqual(session.status_code, 200)
                    self.assertEqual(session.json()["tenant_id"], "tenant-a")

                    audit_logs = client.get("/api/admin/audit-logs", headers={"Authorization": f"Bearer {token}"})
                    self.assertEqual(audit_logs.status_code, 200)
                    self.assertEqual(audit_logs.json()["audit_logs"], [])

                    roles = client.get("/api/admin/roles", headers={"Authorization": f"Bearer {token}"}).json()["roles"]
                    auditor_role = next(role for role in roles if role["name"] == "auditor")
                    create_auditor = client.post(
                        "/api/admin/users",
                        headers={"Authorization": f"Bearer {token}"},
                        json={
                            "external_id": "bob",
                            "display_name": "Bob",
                            "groups": ["security"],
                            "role_ids": [auditor_role["id"]],
                        },
                    )
                    self.assertEqual(create_auditor.status_code, 200)
                    auditor_audit_logs = client.get(
                        "/api/admin/audit-logs",
                        headers={"Authorization": f"Bearer {auditor_token}"},
                    )
                    self.assertEqual(auditor_audit_logs.status_code, 200)
                    auditor_users = client.get(
                        "/api/admin/users",
                        headers={"Authorization": f"Bearer {auditor_token}"},
                    )
                    self.assertEqual(auditor_users.status_code, 403)

                    missing_approval = client.post("/api/admin/audit-logs/purge", headers={"Authorization": f"Bearer {token}"})
                    self.assertEqual(missing_approval.status_code, 422)
                    invalid_approval = client.post(
                        "/api/admin/audit-logs/purge",
                        headers={"Authorization": f"Bearer {token}"},
                        json={"approval_token": "wrong"},
                    )
                    self.assertEqual(invalid_approval.status_code, 403)
                    purge = client.post(
                        "/api/admin/audit-logs/purge",
                        headers={"Authorization": f"Bearer {token}"},
                        json={"approval_token": "approved-by-security"},
                    )
                    self.assertEqual(purge.status_code, 200)


if __name__ == "__main__":
    unittest.main()
