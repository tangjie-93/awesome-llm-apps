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
    embedding_provider: str
    embedding_model: str
    embedding_base_url: str | None
    embedding_api_key: str | None
    default_groups: tuple[str, ...]
    default_risk_levels: tuple[str, ...]
    risk_by_group: dict[str, str]
    business_domains: tuple[dict[str, str], ...]
    supported_document_types: tuple[str, ...]
    excluded_scopes: tuple[str, ...]
    permission_summary: tuple[str, ...]
    high_risk_policy: str
    context_max_chars: int = 6000
    low_confidence_threshold: float = 0.35
    auth_mode: str = "off"
    jwt_issuer: str | None = None
    jwt_audience: str | None = None
    jwt_jwks_url: str = ""
    jwt_algorithm: str = "RS256"
    jwt_groups_claim: str = "groups"
    jwt_roles_claim: str = "roles"
    jwt_tenant_claim: str = "tenant_id"
    default_tenant_id: str = "default"
    admin_groups: tuple[str, ...] = ("rag-admin",)
    dev_user_id: str = "local-admin"
    dev_user_groups: tuple[str, ...] = ("public", "security", "hr", "it", "ops")
    audit_retention_days: int = 30
    audit_approval_token: str | None = None
    rerank_provider: str = "heuristic"
    rerank_url: str | None = None
    rerank_api_key: str | None = None
    web_fallback_enabled: bool = False
    web_fallback_url: str | None = None
    web_fallback_api_key: str | None = None
    web_fallback_timeout_seconds: int = 8


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
        embedding_provider=os.getenv("ENTERPRISE_RAG_EMBEDDING_PROVIDER", "openai").strip().lower() or "openai",
        embedding_model=os.getenv("ENTERPRISE_RAG_EMBEDDING_MODEL", "text-embedding-3-small").strip(),
        embedding_base_url=os.getenv("ENTERPRISE_RAG_EMBEDDING_BASE_URL", llm_base_url or "").strip() or None,
        embedding_api_key=os.getenv("ENTERPRISE_RAG_EMBEDDING_API_KEY", llm_api_key or "").strip() or None,
        default_groups=_read_csv("ENTERPRISE_RAG_DEFAULT_GROUPS", ("public", "security", "hr", "it", "ops")),
        default_risk_levels=_read_csv("ENTERPRISE_RAG_RISK_LEVELS", ("low", "medium", "high")),
        risk_by_group=_read_risk_map(),
        business_domains=_read_business_domains(),
        supported_document_types=_read_csv("ENTERPRISE_RAG_DOCUMENT_TYPES", ("Markdown", "Text", "FAQ")),
        excluded_scopes=_read_csv(
            "ENTERPRISE_RAG_EXCLUDED_SCOPES",
            ("多租户隔离", "细粒度段权限", "自动执行动作", "多模态输入", "知识图谱"),
        ),
        permission_summary=(
            "文档默认归属 public。",
            "敏感文档必须显式指定权限组。",
            "检索结果必须先过滤权限，再进入最终回答。",
            "high 风险内容可生成候选答案，但必须人工复核和审批后才可对外使用。",
        ),
        high_risk_policy="允许模型生成答案候选，但必须人工复核和审批后才可对外使用。",
        context_max_chars=int(os.getenv("ENTERPRISE_RAG_CONTEXT_MAX_CHARS", "6000")),
        low_confidence_threshold=float(os.getenv("ENTERPRISE_RAG_LOW_CONFIDENCE_THRESHOLD", "0.35")),
        auth_mode=os.getenv("ENTERPRISE_RAG_AUTH_MODE", "off").strip().lower(),
        jwt_issuer=os.getenv("ENTERPRISE_RAG_JWT_ISSUER", "").strip() or None,
        jwt_audience=os.getenv("ENTERPRISE_RAG_JWT_AUDIENCE", "").strip() or None,
        jwt_jwks_url=os.getenv("ENTERPRISE_RAG_JWT_JWKS_URL", "").strip(),
        jwt_algorithm=os.getenv("ENTERPRISE_RAG_JWT_ALGORITHM", "RS256").strip(),
        jwt_groups_claim=os.getenv("ENTERPRISE_RAG_JWT_GROUPS_CLAIM", "groups").strip(),
        jwt_roles_claim=os.getenv("ENTERPRISE_RAG_JWT_ROLES_CLAIM", "roles").strip(),
        jwt_tenant_claim=os.getenv("ENTERPRISE_RAG_JWT_TENANT_CLAIM", "tenant_id").strip(),
        default_tenant_id=os.getenv("ENTERPRISE_RAG_DEFAULT_TENANT_ID", "default").strip() or "default",
        admin_groups=_read_csv("ENTERPRISE_RAG_ADMIN_GROUPS", ("rag-admin",)),
        dev_user_id=os.getenv("ENTERPRISE_RAG_DEV_USER_ID", "local-admin").strip(),
        dev_user_groups=_read_csv("ENTERPRISE_RAG_DEV_USER_GROUPS", ("public", "security", "hr", "it", "ops")),
        audit_retention_days=int(os.getenv("ENTERPRISE_RAG_AUDIT_RETENTION_DAYS", "30")),
        audit_approval_token=os.getenv("ENTERPRISE_RAG_AUDIT_APPROVAL_TOKEN", "").strip() or None,
        rerank_provider=os.getenv("ENTERPRISE_RAG_RERANK_PROVIDER", "heuristic").strip().lower(),
        rerank_url=os.getenv("ENTERPRISE_RAG_RERANK_URL", "").strip() or None,
        rerank_api_key=os.getenv("ENTERPRISE_RAG_RERANK_API_KEY", "").strip() or None,
        web_fallback_enabled=_read_bool("ENTERPRISE_RAG_WEB_FALLBACK_ENABLED", "false"),
        web_fallback_url=os.getenv("ENTERPRISE_RAG_WEB_FALLBACK_URL", "").strip() or None,
        web_fallback_api_key=os.getenv("ENTERPRISE_RAG_WEB_FALLBACK_API_KEY", "").strip() or None,
        web_fallback_timeout_seconds=int(os.getenv("ENTERPRISE_RAG_WEB_FALLBACK_TIMEOUT_SECONDS", "8")),
    )


def _read_bool(name: str, default: str) -> bool:
    """把常见布尔型环境变量统一解析为 True / False。"""
    return os.getenv(name, default).strip().lower() in {"1", "true", "yes", "on"}


def _read_csv(name: str, default: tuple[str, ...]) -> tuple[str, ...]:
    """读取逗号分隔的环境变量，空值时回退到默认列表。"""
    raw_value = os.getenv(name, "").strip()
    if not raw_value:
        return default
    values = tuple(item.strip() for item in raw_value.split(",") if item.strip())
    return values or default


def _read_risk_map() -> dict[str, str]:
    """读取权限组到风险等级的映射，支持用 group:level 逗号分隔覆盖。"""
    default = {
        "public": "low",
        "security": "high",
        "hr": "medium",
        "it": "medium",
        "ops": "high",
    }
    raw_value = os.getenv("ENTERPRISE_RAG_RISK_BY_GROUP", "").strip()
    if not raw_value:
        return default
    parsed: dict[str, str] = {}
    for item in raw_value.split(","):
        if ":" not in item:
            continue
        group, risk_level = item.split(":", 1)
        group = group.strip().lower()
        risk_level = risk_level.strip().lower()
        if group and risk_level:
            parsed[group] = risk_level
    return parsed or default


def _read_business_domains() -> tuple[dict[str, str], ...]:
    """读取首批业务域说明，格式为 code:description，空值时使用阶段 0 默认域。"""
    raw_value = os.getenv("ENTERPRISE_RAG_BUSINESS_DOMAINS", "").strip()
    if not raw_value:
        return (
            {"code": "security", "description": "安全制度、事件响应、访问控制"},
            {"code": "hr", "description": "入职、培训、员工手册"},
            {"code": "it", "description": "备份、运维、核心 IT 标准"},
        )
    domains: list[dict[str, str]] = []
    for item in raw_value.split(","):
        if ":" not in item:
            continue
        code, description = item.split(":", 1)
        code = code.strip()
        description = description.strip()
        if code and description:
            domains.append({"code": code, "description": description})
    return tuple(domains) or (
        {"code": "security", "description": "安全制度、事件响应、访问控制"},
        {"code": "hr", "description": "入职、培训、员工手册"},
        {"code": "it", "description": "备份、运维、核心 IT 标准"},
    )


def _llm_defaults(provider: str) -> tuple[str, str]:
    """按模型供应商返回默认模型名和兼容接口地址。"""
    if provider == "deepseek":
        return "deepseek-chat", "https://api.deepseek.com"
    return "gpt-5.5", "https://api.openai.com/v1"
