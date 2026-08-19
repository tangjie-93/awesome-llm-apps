from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from enterprise_rag_agent.application.service import EnterpriseRAGService
from enterprise_rag_agent.core.config import EnterpriseRAGConfig


class TenantIsolationTest(unittest.TestCase):
    def test_documents_and_search_results_are_isolated_by_tenant(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            document = root / "incident.md"
            document.write_text("# Incident\nAcknowledge the incident within 15 minutes.", encoding="utf-8")
            config = EnterpriseRAGConfig(
                company_name="TestCo",
                db_path=root / "rag.sqlite3",
                default_knowledge_base="general",
                chunk_size=200,
                chunk_overlap=40,
                top_k=3,
                rerank_top_k=6,
                enable_llm=False,
                llm_provider="chatgpt",
                llm_model="gpt-4o-mini",
                llm_base_url=None,
                llm_api_key=None,
                embedding_provider="local",
                embedding_model="local-hashing",
                embedding_base_url=None,
                embedding_api_key=None,
                default_groups=("public",),
                default_risk_levels=("low",),
                risk_by_group={"public": "low"},
                business_domains=(),
                supported_document_types=("Markdown",),
                excluded_scopes=(),
                permission_summary=(),
                high_risk_policy="review",
            )
            service = EnterpriseRAGService(config)
            service.ingest_path(document, tenant_id="tenant-a")

            self.assertEqual(len(service.list_documents(tenant_id="tenant-a")), 1)
            self.assertEqual(service.list_documents(tenant_id="tenant-b"), [])
            self.assertTrue(service.search("acknowledge incident", tenant_id="tenant-a"))
            self.assertEqual(service.search("acknowledge incident", tenant_id="tenant-b"), [])


if __name__ == "__main__":
    unittest.main()
