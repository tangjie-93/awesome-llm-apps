from __future__ import annotations

import json
from urllib import request as urlrequest

from core.config import EnterpriseRAGConfig


def search_web(question: str, config: EnterpriseRAGConfig, limit: int = 3) -> list[dict[str, str]]:
    """调用受配置约束的外部检索服务，并标准化返回结果。"""
    if not config.web_fallback_enabled or not config.web_fallback_url:
        return []

    payload = json.dumps({"query": question, "limit": limit}).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    if config.web_fallback_api_key:
        headers["Authorization"] = f"Bearer {config.web_fallback_api_key}"
    try:
        request = urlrequest.Request(config.web_fallback_url, data=payload, headers=headers, method="POST")
        with urlrequest.urlopen(request, timeout=config.web_fallback_timeout_seconds) as response:
            raw_results = json.loads(response.read().decode("utf-8")).get("results", [])
    except (OSError, ValueError, TypeError):
        return []

    results: list[dict[str, str]] = []
    for item in raw_results[:limit]:
        if not isinstance(item, dict):
            continue
        title = str(item.get("title", "")).strip()
        url = str(item.get("url", "")).strip()
        snippet = str(item.get("snippet", "")).strip()
        if title and url and snippet:
            results.append({"title": title, "url": url, "snippet": snippet})
    return results
