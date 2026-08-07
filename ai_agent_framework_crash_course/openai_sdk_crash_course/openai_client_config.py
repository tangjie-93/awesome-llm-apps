"""OpenAI SDK 课程示例共用的客户端配置。"""

import os
from dataclasses import dataclass

from agents import set_default_openai_api, set_default_openai_client, set_tracing_disabled
from dotenv import load_dotenv
from openai import AsyncOpenAI


@dataclass(frozen=True)
class OpenAIClientSettings:
    """保存 OpenAI 兼容接口运行时需要的配置项。"""

    api_key: str | None
    base_url: str | None
    timeout: float
    max_retries: int
    api_type: str
    model: str
    tracing_disabled: bool


def _env_flag(name: str, default: bool) -> bool:
    """读取布尔类型环境变量，支持 false、no、off 等常见写法。"""
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() not in {"0", "false", "no", "off"}


def load_openai_settings() -> OpenAIClientSettings:
    """从 .env 和系统环境变量中加载 OpenAI 兼容接口配置。"""
    load_dotenv(override=True)
    return OpenAIClientSettings(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL") or None,
        timeout=float(os.getenv("OPENAI_TIMEOUT", "120")),
        max_retries=int(os.getenv("OPENAI_MAX_RETRIES", "2")),
        api_type=os.getenv("OPENAI_API_TYPE", "chat_completions"),
        model=os.getenv("OPENAI_MODEL", "gpt-5.6-sol"),
        tracing_disabled=_env_flag("OPENAI_TRACING_DISABLED", True),
    )


def configure_openai_client() -> OpenAIClientSettings:
    """配置 Agents SDK，让所有示例共用 .env 中声明的客户端设置。"""
    settings = load_openai_settings()
    os.environ.setdefault("OPENAI_DEFAULT_MODEL", settings.model)

    # 中转站通常使用 Chat Completions 兼容接口；官方 Responses 接口也保留支持。
    if settings.api_type in {"responses", "chat_completions"}:
        set_default_openai_api(settings.api_type)

    set_tracing_disabled(settings.tracing_disabled)
    if settings.api_key:
        # 注册自定义 AsyncOpenAI 客户端，统一处理 api_key、base_url、超时和重试。
        set_default_openai_client(
            AsyncOpenAI(
                api_key=settings.api_key,
                base_url=settings.base_url,
                timeout=settings.timeout,
                max_retries=settings.max_retries,
            ),
            use_for_tracing=False,
        )
    return settings


def get_openai_model() -> str:
    """获取当前配置的模型名称，优先使用 OPENAI_MODEL。"""
    return os.getenv("OPENAI_MODEL", os.getenv("OPENAI_DEFAULT_MODEL", "gpt-5.6-sol"))
