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

    def test_graph_isolated_by_tenant_and_document_group(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            public_document = root / "public.md"
            public_document.write_text(
                "# Public Incident\nThe public incident process uses PagerDuty.",
                encoding="utf-8",
            )
            restricted_document = root / "restricted.md"
            restricted_document.write_text(
                "# Restricted Incident\nThe restricted incident process uses SecretVault.",
                encoding="utf-8",
            )
            config = EnterpriseRAGConfig(
                company_name="TestCo",
                db_path=root / "rag.sqlite3",
                default_knowledge_base="general",
                chunk_size=200,
                chunk_overlap=40,
                top_k=5,
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
                default_groups=("public", "security"),
                default_risk_levels=("low", "high"),
                risk_by_group={"public": "low", "security": "high"},
                business_domains=(),
                supported_document_types=("Markdown",),
                excluded_scopes=(),
                permission_summary=(),
                high_risk_policy="review",
            )
            service = EnterpriseRAGService(config)
            service.ingest_path(public_document, tenant_id="tenant-a")
            service.ingest_path(restricted_document, allowed_groups=["security"], tenant_id="tenant-a")
            service.ingest_path(public_document, tenant_id="tenant-b")

            tenant_a_graph = service.knowledge_graph(user_groups=["public"], tenant_id="tenant-a")
            tenant_b_graph = service.knowledge_graph(user_groups=["public"], tenant_id="tenant-b")
            tenant_a_names = {str(item["name"]) for item in tenant_a_graph["entities"]}
            tenant_b_names = {str(item["name"]) for item in tenant_b_graph["entities"]}
            self.assertIn("PagerDuty", tenant_a_names)
            self.assertNotIn("SecretVault", tenant_a_names)
            self.assertIn("PagerDuty", tenant_b_names)
            self.assertNotIn("SecretVault", tenant_b_names)

            restricted_graph = service.knowledge_graph(user_groups=["security"], tenant_id="tenant-a")
            restricted_names = {str(item["name"]) for item in restricted_graph["entities"]}
            self.assertIn("SecretVault", restricted_names)

    def test_graph_query_respects_hops_tenant_and_document_permissions(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            first = root / "first.md"
            first.write_text("# PagerDuty\nPagerDuty routes alerts to ServiceNow.", encoding="utf-8")
            second = root / "second.md"
            second.write_text("# ServiceNow\nServiceNow records incidents in VaultDesk.", encoding="utf-8")
            restricted = root / "restricted.md"
            restricted.write_text("# ServiceNow\nServiceNow also uses SecretVault.", encoding="utf-8")
            config = EnterpriseRAGConfig(
                company_name="TestCo",
                db_path=root / "rag.sqlite3",
                default_knowledge_base="general",
                chunk_size=200,
                chunk_overlap=40,
                top_k=5,
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
                default_groups=("public", "security"),
                default_risk_levels=("low", "high"),
                risk_by_group={"public": "low", "security": "high"},
                business_domains=(),
                supported_document_types=("Markdown",),
                excluded_scopes=(),
                permission_summary=(),
                high_risk_policy="review",
            )
            service = EnterpriseRAGService(config)
            service.ingest_path(first, tenant_id="tenant-a")
            service.ingest_path(second, tenant_id="tenant-a")
            service.ingest_path(restricted, allowed_groups=["security"], tenant_id="tenant-a")
            service.ingest_path(first, tenant_id="tenant-b")

            public_result = service.query_knowledge_graph(
                "PagerDuty",
                user_groups=["public"],
                max_hops=2,
                tenant_id="tenant-a",
            )
            public_names = {str(item["name"]) for item in public_result["entities"]}
            self.assertIn("VaultDesk", public_names)
            self.assertNotIn("SecretVault", public_names)
            self.assertTrue(any(int(item["hops"]) == 2 for item in public_result["paths"]))

            tenant_b_result = service.query_knowledge_graph(
                "PagerDuty",
                user_groups=["public"],
                max_hops=3,
                tenant_id="tenant-b",
            )
            tenant_b_names = {str(item["name"]) for item in tenant_b_result["entities"]}
            self.assertIn("PagerDuty", tenant_b_names)
            self.assertIn("ServiceNow", tenant_b_names)
            self.assertNotIn("VaultDesk", tenant_b_names)


if __name__ == "__main__":
    unittest.main()
