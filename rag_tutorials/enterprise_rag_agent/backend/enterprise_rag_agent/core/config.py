from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os


@dataclass(frozen=True, slots=True)
class EnterpriseRAGConfig:
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


def load_config() -> EnterpriseRAGConfig:
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
    )


def _read_bool(name: str, default: str) -> bool:
    return os.getenv(name, default).strip().lower() in {"1", "true", "yes", "on"}


def _llm_defaults(provider: str) -> tuple[str, str]:
    if provider == "deepseek":
        return "deepseek-chat", "https://api.deepseek.com"
    return "gpt-4o-mini", "https://api.openai.com/v1"
