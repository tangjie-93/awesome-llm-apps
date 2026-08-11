import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


@dataclass(frozen=True)
class ApiSettings:
    """项目运行所需的 API 配置。"""

    deepseek_api_key: str
    openai_api_key: str
    openai_base_url: str


def load_api_settings(env_path: Path | None = None) -> ApiSettings:
    """从 `.env` 和进程环境变量加载 API 配置。"""
    if env_path is None:
        env_path = Path(__file__).with_name(".env")

    load_dotenv(dotenv_path=env_path)

    return ApiSettings(
        deepseek_api_key=os.getenv("DEEPSEEK_API_KEY", "").strip(),
        openai_api_key=os.getenv("OPENAI_API_KEY", "").strip(),
        openai_base_url=os.getenv("OPENAI_BASE_URL", "").strip(),
    )
