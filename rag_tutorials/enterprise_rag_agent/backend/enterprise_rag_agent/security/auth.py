from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import jwt
from fastapi import HTTPException, Request
from jwt import PyJWKClient

from ..core.config import EnterpriseRAGConfig


@dataclass(frozen=True, slots=True)
class AuthContext:
    """已验证请求身份的最小上下文。"""

    user_id: str
    display_name: str
    email: str | None
    groups: tuple[str, ...]
    is_admin: bool
    claims: dict[str, Any]


def authenticate_request(request: Request, config: EnterpriseRAGConfig) -> AuthContext:
    """验证 Bearer JWT，并从可信 claims 中提取用户组。"""
    if config.auth_mode == "off":
        return AuthContext(
            config.dev_user_id,
            "Local Admin",
            None,
            config.dev_user_groups,
            True,
            {"sub": config.dev_user_id},
        )

    header = request.headers.get("Authorization", "")
    if not header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Bearer token required")
    token = header[7:].strip()
    if not token:
        raise HTTPException(status_code=401, detail="Bearer token required")
    try:
        signing_key = PyJWKClient(config.jwt_jwks_url).get_signing_key_from_jwt(token).key
        claims = jwt.decode(
            token,
            signing_key,
            algorithms=[config.jwt_algorithm],
            issuer=config.jwt_issuer or None,
            audience=config.jwt_audience or None,
            options={"require": ["sub"]},
        )
    except Exception as exc:
        raise HTTPException(status_code=401, detail="Invalid identity token") from exc

    groups = _claim_values(claims, config.jwt_groups_claim)
    roles = _claim_values(claims, config.jwt_roles_claim)
    admin = bool(set(groups) & set(config.admin_groups) or "admin" in roles)
    display_name = str(claims.get("name") or claims.get("preferred_username") or claims["sub"])
    email = str(claims["email"]) if claims.get("email") else None
    return AuthContext(str(claims["sub"]), display_name, email, tuple(groups), admin, claims)


def require_admin(context: AuthContext) -> None:
    """拒绝非管理员访问管理端接口。"""
    if not context.is_admin:
        raise HTTPException(status_code=403, detail="Administrator permission required")


def _claim_values(claims: dict[str, Any], name: str) -> list[str]:
    value = claims.get(name, [])
    if isinstance(value, str):
        return [item.strip().lower() for item in value.split(",") if item.strip()]
    if isinstance(value, list):
        return [str(item).strip().lower() for item in value if str(item).strip()]
    return []
