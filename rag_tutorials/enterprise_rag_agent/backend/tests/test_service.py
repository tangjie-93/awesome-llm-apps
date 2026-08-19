from __future__ import annotations

from pathlib import Path
import struct
import tempfile
import unittest

from core.config import EnterpriseRAGConfig
from application.service import EnterpriseRAGService


class EnterpriseRAGServiceTest(unittest.TestCase):
    def test_ingest_image_with_sidecar_caption_and_retrieve_it(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            image = tmp_path / "vpn_network_map.png"
            image.write_bytes(
                b"\x89PNG\r\n\x1a\n" + b"\x00\x00\x00\rIHDR" + struct.pack(">II", 640, 480) + b"\x08\x02\x00\x00\x00"
            )
            image.with_name("vpn_network_map.caption.txt").write_text(
                "VPN network map showing the production gateway and backup tunnel.",
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
                supported_document_types=("Image",),
                excluded_scopes=(),
                permission_summary=(),
                high_risk_policy="review",
            )
            service = EnterpriseRAGService(config)
            result = service.ingest_path(image)
            self.assertEqual(result.documents_indexed, 1)
            document = service.list_documents()[0]
            self.assertEqual(document["content_type"], "image")
            search_results = service.search("production VPN backup tunnel")
            self.assertTrue(search_results)
            self.assertEqual(search_results[0].chunk.path, str(image.resolve()))

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
                risk_by_group={"public": "low", "security": "high", "hr": "medium", "it": "medium", "ops": "high"},
                business_domains=(
                    {"code": "security", "description": "安全制度、事件响应、访问控制"},
                    {"code": "hr", "description": "入职、培训、员工手册"},
                    {"code": "it", "description": "备份、运维、核心 IT 标准"},
                ),
                supported_document_types=("Markdown", "Text", "FAQ"),
                excluded_scopes=("多租户隔离", "细粒度段权限", "自动执行动作", "多模态输入", "知识图谱"),
                permission_summary=(
                    "文档默认归属 public。",
                    "敏感文档必须显式指定权限组。",
                    "检索结果必须先过滤权限，再进入最终回答。",
                    "high 风险内容可生成候选答案，但必须人工复核和审批后才可对外使用。",
                ),
                high_risk_policy="允许模型生成答案候选，但必须人工复核和审批后才可对外使用。",
                rerank_provider="http",
                rerank_url="http://127.0.0.1:9/rerank",
                rerank_api_key=None,
            )
            service = EnterpriseRAGService(config)
            ingest_result = service.ingest_path(kb_root)
            self.assertEqual(ingest_result.documents_indexed, 2)
            self.assertGreaterEqual(ingest_result.chunks_indexed, 2)
            self.assertEqual(ingest_result.documents_skipped, 0)
            self.assertEqual(ingest_result.documents_removed, 0)
            document_summaries = service.list_documents()
            self.assertTrue(all(document["content_hash"] for document in document_summaries))
            self.assertTrue(all(document["risk_level"] in {"high", "medium"} for document in document_summaries))
            self.assertTrue(all("indexed_at" in document for document in document_summaries))

            answer = service.agent.answer("How fast should we acknowledge the incident?")
            self.assertGreater(answer.confidence, 0)
            self.assertTrue(answer.citations)
            graph = service.knowledge_graph()
            self.assertGreater(graph["entity_count"], 0)

            service.ingest_path(
                kb_root / "security" / "incident.md",
                knowledge_base="security",
                allowed_groups=["security"],
            )
            denied_results = service.search(
                "How fast should we acknowledge the incident?",
                user_groups=["hr"],
            )
            self.assertFalse(denied_results)

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
            self.assertTrue(all(chunk.risk_level == "high" for chunk in chunks))
            logged_answer = service.list_answer_logs()[0]
            self.assertTrue(logged_answer["metadata"]["requires_human_review"])


if __name__ == "__main__":
    unittest.main()
