from __future__ import annotations

from collections.abc import Sequence


def normalize_groups(groups: Sequence[str] | None) -> tuple[str, ...]:
    if not groups:
        return ("public",)
    cleaned = sorted({group.strip().lower() for group in groups if group.strip()})
    return tuple(cleaned or ["public"])


def can_access(allowed_groups: Sequence[str], user_groups: Sequence[str] | None) -> bool:
    allowed = {group.lower() for group in allowed_groups}
    if "public" in allowed:
        return True
    if not user_groups:
        return False
    requested = {group.lower() for group in user_groups if group.strip()}
    return bool(allowed & requested)

