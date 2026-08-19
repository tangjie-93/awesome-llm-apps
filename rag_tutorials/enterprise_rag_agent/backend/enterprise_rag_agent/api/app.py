from __future__ import annotations

import os
import csv
import io
import hmac
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse, StreamingResponse

from ..application.service import EnterpriseRAGService
from ..core.config import load_config
from ..retrieval.embeddings import EmbeddingServiceUnavailable
from ..security.auth import AuthContext, authenticate_request, require_admin


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


class RetrievalEvaluateRequest(BaseModel):
    cases: list[dict[str, object]] | None = None


class FeedbackRequest(BaseModel):
    answer_log_id: int | None = Field(default=None, ge=1)
    rating: int = Field(ge=1, le=5)
    comment: str = Field(default="", max_length=1000)


class WebSearchRequest(BaseModel):
    question: str = Field(min_length=1, max_length=1000)
    limit: int = Field(default=3, ge=1, le=10)


class UserCreateRequest(BaseModel):
    external_id: str = Field(min_length=1, max_length=200)
    display_name: str = Field(min_length=1, max_length=200)
    email: str | None = Field(default=None, max_length=320)
    groups: list[str] = Field(default_factory=list)
    role_ids: list[int] = Field(default_factory=list)


class UserUpdateRequest(BaseModel):
    display_name: str = Field(min_length=1, max_length=200)
    email: str | None = Field(default=None, max_length=320)
    groups: list[str] = Field(default_factory=list)
    is_active: bool = True
    role_ids: list[int] = Field(default_factory=list)


class RoleRequest(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)
    permissions: list[str] = Field(default_factory=list)


class AuditActionRequest(BaseModel):
    approval_token: str = Field(min_length=1, max_length=500)


def create_app() -> FastAPI:
    app_config = load_config()
    service = EnterpriseRAGService(app_config)

    app = FastAPI(title='Enterprise RAG Agent', version='1.0.0')
    api = FastAPI(title='Enterprise RAG Agent API', version='1.0.0')

    @api.exception_handler(EmbeddingServiceUnavailable)
    async def embedding_service_unavailable(
        request: Request,
        exc: EmbeddingServiceUnavailable,
    ) -> JSONResponse:
        return JSONResponse(status_code=503, content={'detail': str(exc)})
     
    api.add_middleware(
        CORSMiddleware,
        allow_origins=_cors_origins(),
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    @api.middleware("http")
    async def authenticate_and_measure(request: Request, call_next: Any) -> JSONResponse:
        if request.url.path == "/health":
            response = await call_next(request)
            return response
        try:
            context = authenticate_request(request, app_config)
        except HTTPException as exc:
            return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})
        profile = service.store.upsert_user_profile(
            context.user_id,
            context.display_name,
            context.email,
            list(context.groups),
            tenant_id=context.tenant_id,
        )
        if not profile["is_active"]:
            return JSONResponse(status_code=403, content={"detail": "User is disabled"})
        local_admin = "admin" in service.store.user_role_names(int(profile["id"]))
        if local_admin and not context.is_admin:
            context = AuthContext(
                context.user_id,
                context.display_name,
                context.email,
                context.groups,
                context.tenant_id,
                True,
                context.claims,
            )
        request.state.auth = context
        request.state.permissions = service.store.user_permissions(int(profile["id"]))
        response = await call_next(request)
        service.store.log_usage(
            context.user_id,
            "request",
            request.url.path,
            input_tokens=0,
            output_tokens=0,
            model_calls=0,
            tenant_id=context.tenant_id,
        )
        return response

    def auth_context(request: Request) -> AuthContext:
        return request.state.auth

    def require_permission(request: Request, permission: str) -> AuthContext:
        context = auth_context(request)
        if context.is_admin or permission in request.state.permissions:
            return context
        raise HTTPException(status_code=403, detail=f"Permission required: {permission}")

    @api.get('/health')
    def health() -> dict[str, str]:
        return {'status': 'ok'}

    @api.get('/stats')
    def stats(request: Request) -> dict[str, Any]:
        context = auth_context(request)
        result = service.stats(context.tenant_id)
        result["usage"] = service.store.usage_stats(context.tenant_id)
        return result

    @api.get('/config')
    def config_view() -> dict[str, Any]:
        return {
            'company_name': app_config.company_name,
            'default_knowledge_base': app_config.default_knowledge_base,
            'default_groups': list(app_config.default_groups),
            'default_risk_levels': list(app_config.default_risk_levels),
            'risk_by_group': app_config.risk_by_group,
            'chunk_size': app_config.chunk_size,
            'chunk_overlap': app_config.chunk_overlap,
            'top_k': app_config.top_k,
            'rerank_top_k': app_config.rerank_top_k,
            'enable_llm': app_config.enable_llm,
            'llm_provider': app_config.llm_provider,
            'llm_model': app_config.llm_model,
            'auth_mode': app_config.auth_mode,
            'rerank_provider': app_config.rerank_provider,
            'audit_retention_days': app_config.audit_retention_days,
            'web_fallback_enabled': app_config.web_fallback_enabled,
            'jwt_tenant_claim': app_config.jwt_tenant_claim,
        }

    @api.get('/session')
    def session(request: Request) -> dict[str, Any]:
        context = auth_context(request)
        return {
            "user_id": context.user_id,
            "display_name": context.display_name,
            "email": context.email,
            "groups": list(context.groups),
            "tenant_id": context.tenant_id,
            "is_admin": context.is_admin,
            "permissions": sorted(request.state.permissions),
        }

    @api.get('/scope')
    def scope_view() -> dict[str, Any]:
        return {
            'business_domains': list(app_config.business_domains),
            'supported_document_types': list(app_config.supported_document_types),
            'excluded_scopes': list(app_config.excluded_scopes),
            'permission_summary': list(app_config.permission_summary),
            'risk_by_group': app_config.risk_by_group,
            'high_risk_policy': app_config.high_risk_policy,
        }

    @api.get('/knowledge-bases')
    def knowledge_bases(request: Request) -> dict[str, Any]:
        return {'knowledge_bases': service.store.list_knowledge_bases(auth_context(request).tenant_id)}

    @api.get('/documents')
    def documents(request: Request, knowledge_base: str | None = None) -> dict[str, Any]:
        return {'documents': service.list_documents(knowledge_base, auth_context(request).tenant_id)}

    @api.post('/ingest')
    def ingest(payload: IngestRequest, request: Request) -> dict[str, Any]:
        context = require_permission(request, "run_ingest")
        target = _resolve_path(payload.path)
        if not target.exists():
            service.store.log_operation(
                "ingest",
                "failed",
                payload.path,
                payload.knowledge_base,
                payload.allowed_groups,
                {"error": f"Path not found: {payload.path}"},
                tenant_id=context.tenant_id,
            )
            service.store.log_audit(context.user_id, "ingest_failed", payload.path, {"error": f"Path not found: {payload.path}"}, context.tenant_id)
            raise HTTPException(status_code=404, detail=f'Path not found: {payload.path}')
        try:
            result = service.ingest_path(
                target,
                knowledge_base=payload.knowledge_base,
                allowed_groups=payload.allowed_groups,
                tenant_id=context.tenant_id,
            )
        except Exception as exc:
            service.store.log_operation(
                "ingest",
                "failed",
                str(target),
                payload.knowledge_base,
                payload.allowed_groups,
                {"error": str(exc)},
                tenant_id=context.tenant_id,
            )
            raise
        result_payload = result.to_dict()
        service.store.log_operation(
            "ingest",
            "succeeded",
            str(target),
            payload.knowledge_base,
            payload.allowed_groups,
            result_payload,
            tenant_id=context.tenant_id,
        )
        service.store.log_audit(context.user_id, "ingest", str(target), result_payload, context.tenant_id)
        service.store.log_usage(
            context.user_id,
            "model_call",
            "/ingest",
            input_tokens=_estimate_tokens(str(target)),
            output_tokens=0,
            model_calls=1 if result_payload.get("chunks_indexed", 0) else 0,
            tenant_id=context.tenant_id,
        )
        return result_payload

    @api.post('/search')
    def search(payload: AskRequest, request: Request) -> dict[str, Any]:
        context = auth_context(request)
        results = service.search(
            payload.question,
            knowledge_base=payload.knowledge_base,
            user_groups=list(context.groups),
            top_k=payload.top_k,
            tenant_id=context.tenant_id,
        )
        service.store.log_audit(
            context.user_id,
            "search",
            payload.knowledge_base or "all",
            {"question": payload.question, "result_count": len(results)},
            context.tenant_id,
        )
        service.store.log_usage(
            context.user_id,
            "model_call",
            "/search",
            input_tokens=_estimate_tokens(payload.question),
            output_tokens=0,
            model_calls=1,
            tenant_id=context.tenant_id,
        )
        return {'results': [item.to_dict() for item in results]}

    @api.post('/ask')
    def ask(payload: AskRequest, request: Request) -> dict[str, Any]:
        context = auth_context(request)
        result = service.agent.answer(
            payload.question,
            knowledge_base=payload.knowledge_base,
            user_groups=list(context.groups),
            top_k=payload.top_k,
            tenant_id=context.tenant_id,
        ).to_dict()
        service.store.log_audit(
            context.user_id,
            "ask",
            payload.knowledge_base or "all",
            {"question": payload.question, "result_count": len(result.get("citations", []))},
            context.tenant_id,
        )
        service.store.log_usage(
            context.user_id,
            "model_call",
            "/ask",
            input_tokens=_estimate_tokens(payload.question),
            output_tokens=_estimate_tokens(str(result.get("answer", ""))),
            model_calls=1 if app_config.enable_llm else 0,
            tenant_id=context.tenant_id,
        )
        return result

    @api.post('/evaluate')
    def evaluate(payload: EvaluateRequest) -> dict[str, Any]:
        result = service.evaluate_answer(payload.question, payload.expected_answer, payload.actual_answer)
        service.store.log_audit(
            "system",
            "evaluate",
            "answers",
            {"question": payload.question, "score": result["score"]},
        )
        return result

    @api.post('/evaluate-retrieval')
    def evaluate_retrieval(payload: RetrievalEvaluateRequest) -> dict[str, Any]:
        return service.evaluate_retrieval(payload.cases)

    @api.post('/web-search')
    def web_search(payload: WebSearchRequest, request: Request) -> dict[str, Any]:
        context = auth_context(request)
        results = service.web_search(payload.question, payload.limit)
        service.store.log_audit(
            context.user_id,
            "web_search",
            "external_search",
            {"question": payload.question, "result_count": len(results)},
        )
        return {"results": results, "enabled": app_config.web_fallback_enabled}

    @api.get('/diagnostics')
    def diagnostics(request: Request) -> dict[str, Any]:
        context = auth_context(request)
        result = service.diagnostics(context.tenant_id)
        service.store.log_audit(context.user_id, "diagnostics_read", "system", {}, context.tenant_id)
        return result

    @api.post('/feedback')
    def feedback(payload: FeedbackRequest, request: Request) -> dict[str, Any]:
        context = auth_context(request)
        result = service.store.log_feedback(
            context.user_id,
            payload.answer_log_id,
            payload.rating,
            payload.comment.strip(),
            tenant_id=context.tenant_id,
        )
        service.store.log_audit(context.user_id, "feedback_submit", str(payload.answer_log_id or ""), {"rating": payload.rating}, context.tenant_id)
        return {"feedback": result}

    @api.get('/answer-logs')
    def answer_logs(request: Request) -> dict[str, Any]:
        return {'answer_logs': service.list_answer_logs(auth_context(request).tenant_id)}

    @api.get('/evaluation-logs')
    def evaluation_logs(request: Request) -> dict[str, Any]:
        return {'evaluation_logs': service.list_evaluation_logs(auth_context(request).tenant_id)}

    @api.get('/operation-logs')
    def operation_logs(request: Request) -> dict[str, Any]:
        return {'operation_logs': service.list_operation_logs(auth_context(request).tenant_id)}

    @api.post('/operation-logs/{operation_id}/replay')
    def replay_operation(operation_id: int, request: Request) -> dict[str, Any]:
        context = require_permission(request, "run_ingest")
        log = service.store.get_operation_log(operation_id, context.tenant_id)
        if not log:
            raise HTTPException(status_code=404, detail=f'Operation log not found: {operation_id}')
        if log['operation'] != 'ingest':
            raise HTTPException(status_code=400, detail='Only ingest operations can be replayed')
        if not log['path']:
            raise HTTPException(status_code=400, detail='Operation log has no replayable path')

        replay_path = Path(str(log['path']))
        if not replay_path.exists():
            raise HTTPException(status_code=404, detail=f'Path not found: {replay_path}')

        allowed_groups = [str(group) for group in log['allowed_groups']]
        knowledge_base = str(log['knowledge_base']) if log['knowledge_base'] else None
        try:
            result = service.ingest_path(
                replay_path,
                knowledge_base=knowledge_base,
                allowed_groups=allowed_groups,
                tenant_id=context.tenant_id,
            )
        except Exception as exc:
            service.store.log_operation(
                "ingest_replay",
                "failed",
                str(replay_path),
                knowledge_base,
                allowed_groups,
                {"replay_of": operation_id, "error": str(exc)},
                tenant_id=context.tenant_id,
            )
            raise

        result_payload = result.to_dict()
        service.store.log_operation(
            "ingest_replay",
            "succeeded",
            str(replay_path),
            knowledge_base,
            allowed_groups,
            {"replay_of": operation_id, **result_payload},
            tenant_id=context.tenant_id,
        )
        return result_payload

    @api.get('/admin/audit-logs')
    def audit_logs(request: Request, limit: int = 500) -> dict[str, Any]:
        require_permission(request, "read_audit")
        return {"audit_logs": service.store.list_audit_logs(min(max(limit, 1), 2000), auth_context(request).tenant_id)}

    @api.get('/admin/audit-logs/export')
    def export_audit_logs(request: Request) -> StreamingResponse:
        require_permission(request, "read_audit")
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=["id", "actor_id", "action", "resource", "detail", "created_at"])
        writer.writeheader()
        for item in service.store.list_audit_logs(2000, auth_context(request).tenant_id):
            writer.writerow({key: item.get(key, "") for key in writer.fieldnames})
        return StreamingResponse(
            iter([output.getvalue()]),
            media_type="text/csv; charset=utf-8",
            headers={"Content-Disposition": "attachment; filename=audit-logs.csv"},
        )

    @api.delete('/admin/audit-logs')
    def delete_audit_logs(payload: AuditActionRequest, request: Request, before: str | None = None) -> dict[str, int]:
        context = require_permission(request, "manage_audit")
        _require_audit_approval(payload.approval_token, app_config)
        deleted = service.store.delete_audit_logs(before, context.tenant_id)
        service.store.log_audit(context.user_id, "audit_delete", "audit_logs", {"before": before, "deleted": deleted}, context.tenant_id)
        return {"deleted": deleted}

    @api.post('/admin/audit-logs/purge')
    def purge_audit_logs(payload: AuditActionRequest, request: Request) -> dict[str, int]:
        context = require_permission(request, "manage_audit")
        _require_audit_approval(payload.approval_token, app_config)
        deleted = service.store.purge_audit_logs(app_config.audit_retention_days, context.tenant_id)
        service.store.log_audit(context.user_id, "audit_purge", "audit_logs", {"retention_days": app_config.audit_retention_days, "deleted": deleted}, context.tenant_id)
        return {"deleted": deleted, "retention_days": app_config.audit_retention_days}

    @api.get('/admin/usage')
    def usage(request: Request) -> dict[str, Any]:
        require_permission(request, "read_audit")
        return {"usage": service.store.usage_stats(auth_context(request).tenant_id), "rerank_provider": app_config.rerank_provider}

    @api.get('/admin/users')
    def users(request: Request) -> dict[str, Any]:
        require_permission(request, "manage_users")
        return {"users": service.store.list_users(auth_context(request).tenant_id)}

    @api.post('/admin/users')
    def create_user(payload: UserCreateRequest, request: Request) -> dict[str, Any]:
        context = require_permission(request, "manage_users")
        try:
            user = service.store.create_user(
                payload.external_id,
                payload.display_name,
                payload.email,
                payload.groups,
                payload.role_ids,
                tenant_id=context.tenant_id,
            )
        except Exception as exc:
            raise HTTPException(status_code=400, detail=f"Unable to create user: {exc}") from exc
        service.store.log_audit(context.user_id, "user_create", payload.external_id, {"roles": payload.role_ids}, context.tenant_id)
        return {"user": user}

    @api.put('/admin/users/{user_id}')
    def update_user(user_id: int, payload: UserUpdateRequest, request: Request) -> dict[str, Any]:
        context = require_permission(request, "manage_users")
        user = service.store.update_user(
            user_id,
            payload.display_name,
            payload.email,
            payload.groups,
            payload.is_active,
            payload.role_ids,
            tenant_id=context.tenant_id,
        )
        if not user:
            raise HTTPException(status_code=404, detail=f"User not found: {user_id}")
        service.store.log_audit(context.user_id, "user_update", str(user_id), {"roles": payload.role_ids, "is_active": payload.is_active}, context.tenant_id)
        return {"user": user}

    @api.delete('/admin/users/{user_id}')
    def delete_user(user_id: int, request: Request) -> dict[str, bool]:
        context = require_permission(request, "manage_users")
        if not service.store.delete_user(user_id, auth_context(request).tenant_id):
            raise HTTPException(status_code=404, detail=f"User not found: {user_id}")
        service.store.log_audit(context.user_id, "user_delete", str(user_id), {}, context.tenant_id)
        return {"deleted": True}

    @api.get('/admin/roles')
    def roles(request: Request) -> dict[str, Any]:
        require_permission(request, "manage_roles")
        return {"roles": service.store.list_roles()}

    @api.post('/admin/roles')
    def create_role(payload: RoleRequest, request: Request) -> dict[str, Any]:
        context = require_permission(request, "manage_roles")
        try:
            role = service.store.create_role(payload.name, payload.description, payload.permissions)
        except Exception as exc:
            raise HTTPException(status_code=400, detail=f"Unable to create role: {exc}") from exc
        service.store.log_audit(context.user_id, "role_create", payload.name, {"permissions": payload.permissions})
        return {"role": role}

    @api.put('/admin/roles/{role_id}')
    def update_role(role_id: int, payload: RoleRequest, request: Request) -> dict[str, Any]:
        context = require_permission(request, "manage_roles")
        role = service.store.update_role(role_id, payload.name, payload.description, payload.permissions)
        if not role:
            raise HTTPException(status_code=404, detail=f"Role not found: {role_id}")
        service.store.log_audit(context.user_id, "role_update", str(role_id), {"permissions": payload.permissions})
        return {"role": role}

    @api.delete('/admin/roles/{role_id}')
    def delete_role(role_id: int, request: Request) -> dict[str, bool]:
        context = require_permission(request, "manage_roles")
        if not service.store.delete_role(role_id):
            raise HTTPException(status_code=400, detail="System roles cannot be deleted or role was not found")
        service.store.log_audit(context.user_id, "role_delete", str(role_id), {})
        return {"deleted": True}

    app.mount('/api', api)
    return app


def _resolve_path(value: str) -> Path:
    path = Path(value)
    if path.exists():
        return path

    repo_root = Path(__file__).resolve().parents[3]
    candidate = repo_root / value
    if candidate.exists():
        return candidate

    return path


def _cors_origins() -> list[str]:
    raw_value = os.getenv('ENTERPRISE_RAG_CORS_ORIGINS', '').strip()
    if raw_value:
        return [origin.strip() for origin in raw_value.split(',') if origin.strip()]
    return [
        'http://localhost:5173',
        'http://127.0.0.1:5173',
        'http://localhost:5000',
        'http://127.0.0.1:5000',
        'http://localhost:5174',
        'http://127.0.0.1:5174',
        'http://localhost:4173',
        'http://127.0.0.1:4173',
    ]


def _estimate_tokens(value: str) -> int:
    """在模型未返回 usage 时提供稳定的本地 token 估算。"""
    return max(1, len(value.replace("\n", " ").split()))


def _require_audit_approval(approval_token: str, config: Any) -> None:
    """校验破坏性审计操作的服务端审批令牌，未配置或不匹配时拒绝执行。"""
    if not config.audit_approval_token:
        raise HTTPException(status_code=503, detail="Audit approval token is not configured")
    if not hmac.compare_digest(approval_token, config.audit_approval_token):
        raise HTTPException(status_code=403, detail="Valid audit approval token required")
