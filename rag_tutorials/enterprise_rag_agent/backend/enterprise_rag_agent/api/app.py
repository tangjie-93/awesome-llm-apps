from __future__ import annotations

import os
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from ..application.service import EnterpriseRAGService
from ..core.config import load_config


class IngestRequest(BaseModel):
    path: str
    knowledge_base: str | None = None
    allowed_groups: list[str] | None = None


class AskRequest(BaseModel):
    question: str = Field(min_length=1)
    knowledge_base: str | None = None
    user_groups: list[str] | None = None
    top_k: int | None = Field(default=None, ge=1, le=20)


class EvaluateRequest(BaseModel):
    question: str = Field(min_length=1)
    expected_answer: str | None = None
    actual_answer: str = Field(min_length=1)


def create_app() -> FastAPI:
    app_config = load_config()
    service = EnterpriseRAGService(app_config)
    app = FastAPI(title="Enterprise RAG Agent", version="1.0.0")

    # 本地联调时允许前端开发服务器直接访问后端接口。
    app.add_middleware(
        CORSMiddleware,
        allow_origins=_cors_origins(),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    @app.get("/stats")
    def stats() -> dict[str, Any]:
        return service.stats()

    @app.get("/config")
    def config_view() -> dict[str, Any]:
        return {
            "company_name": app_config.company_name,
            "default_knowledge_base": app_config.default_knowledge_base,
            "default_groups": list(app_config.default_groups),
            "default_risk_levels": list(app_config.default_risk_levels),
            "chunk_size": app_config.chunk_size,
            "chunk_overlap": app_config.chunk_overlap,
            "top_k": app_config.top_k,
            "rerank_top_k": app_config.rerank_top_k,
            "enable_llm": app_config.enable_llm,
            "llm_provider": app_config.llm_provider,
            "llm_model": app_config.llm_model,
        }

    @app.get("/knowledge-bases")
    def knowledge_bases() -> dict[str, Any]:
        return {"knowledge_bases": service.store.list_knowledge_bases()}

    @app.get("/documents")
    def documents(knowledge_base: str | None = None) -> dict[str, Any]:
        return {"documents": service.list_documents(knowledge_base)}

    @app.post("/ingest")
    def ingest(payload: IngestRequest) -> dict[str, Any]:
        target = _resolve_path(payload.path)
        if not target.exists():
            raise HTTPException(status_code=404, detail=f"Path not found: {payload.path}")
        return service.ingest_path(target, knowledge_base=payload.knowledge_base, allowed_groups=payload.allowed_groups).to_dict()

    @app.post("/search")
    def search(payload: AskRequest) -> dict[str, Any]:
        results = service.search(
            payload.question,
            knowledge_base=payload.knowledge_base,
            user_groups=payload.user_groups,
            top_k=payload.top_k,
        )
        return {"results": [item.to_dict() for item in results]}

    @app.post("/ask")
    def ask(payload: AskRequest) -> dict[str, Any]:
        return service.agent.answer(
            payload.question,
            knowledge_base=payload.knowledge_base,
            user_groups=payload.user_groups,
            top_k=payload.top_k,
        ).to_dict()

    @app.post("/evaluate")
    def evaluate(payload: EvaluateRequest) -> dict[str, Any]:
        return service.evaluate_answer(payload.question, payload.expected_answer, payload.actual_answer)

    @app.get("/answer-logs")
    def answer_logs() -> dict[str, Any]:
        return {"answer_logs": service.list_answer_logs()}

    @app.get("/evaluation-logs")
    def evaluation_logs() -> dict[str, Any]:
        return {"evaluation_logs": service.list_evaluation_logs()}

    return app


def _resolve_path(value: str):
    from pathlib import Path

    return Path(value)


def _cors_origins() -> list[str]:
    """返回本地开发阶段允许的前端来源。"""
    raw_value = os.getenv("ENTERPRISE_RAG_CORS_ORIGINS", "").strip()
    if raw_value:
        return [origin.strip() for origin in raw_value.split(",") if origin.strip()]
    return [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
        "http://localhost:4173",
        "http://127.0.0.1:4173",
    ]
