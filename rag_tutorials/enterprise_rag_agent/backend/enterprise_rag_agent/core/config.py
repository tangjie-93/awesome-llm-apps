from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv


@dataclass(frozen=True, slots=True)
class EnterpriseRAGConfig:
    """后端运行配置，集中承载知识库、检索和模型默认值。"""
    company_name: str
    db_path: Path
    default_knowledge_base: str
    chunk_size: int
    chunk_overlap: int
    top_k: int
    rerank_top_k: int
    enable_llm: bool
    llm_provider: str
    llm_model: str
    llm_base_url: str | None
    llm_api_key: str | None
    default_groups: tuple[str, ...]
    default_risk_levels: tuple[str, ...]


def load_config() -> EnterpriseRAGConfig:
    """从环境变量读取配置，并补齐一组可落地的默认值。"""
    load_dotenv()
    llm_provider = os.getenv("ENTERPRISE_RAG_LLM_PROVIDER", "chatgpt").strip().lower() or "chatgpt"
    default_model, default_base_url = _llm_defaults(llm_provider)
    llm_base_url = os.getenv("ENTERPRISE_RAG_LLM_BASE_URL", default_base_url).strip() or None
    llm_api_key = os.getenv("ENTERPRISE_RAG_LLM_API_KEY", os.getenv("OPENAI_API_KEY", "")).strip() or None

    return EnterpriseRAGConfig(
        company_name=os.getenv("ENTERPRISE_RAG_COMPANY", "Acme Corp"),
        db_path=Path(os.getenv("ENTERPRISE_RAG_DB_PATH", "data/enterprise_rag.sqlite3")),
        default_knowledge_base=os.getenv("ENTERPRISE_RAG_DEFAULT_KB", "general"),
        chunk_size=int(os.getenv("ENTERPRISE_RAG_CHUNK_SIZE", "900")),
        chunk_overlap=int(os.getenv("ENTERPRISE_RAG_CHUNK_OVERLAP", "120")),
        top_k=int(os.getenv("ENTERPRISE_RAG_TOP_K", "5")),
        rerank_top_k=int(os.getenv("ENTERPRISE_RAG_RERANK_TOP_K", "12")),
        enable_llm=_read_bool("ENTERPRISE_RAG_ENABLE_LLM", "false"),
        llm_provider=llm_provider,
        llm_model=os.getenv("ENTERPRISE_RAG_MODEL", default_model),
        llm_base_url=llm_base_url,
        llm_api_key=llm_api_key,
        default_groups=("public", "security", "hr", "it", "ops"),
        default_risk_levels=("low", "medium", "high"),
    )


def _read_bool(name: str, default: str) -> bool:
    """把常见布尔型环境变量统一解析为 True / False。"""
    return os.getenv(name, default).strip().lower() in {"1", "true", "yes", "on"}


def _llm_defaults(provider: str) -> tuple[str, str]:
    """按模型供应商返回默认模型名和兼容接口地址。"""
    if provider == "deepseek":
        return "deepseek-chat", "https://api.deepseek.com"
    return "gpt-5.5", "https://api.openai.com/v1"
