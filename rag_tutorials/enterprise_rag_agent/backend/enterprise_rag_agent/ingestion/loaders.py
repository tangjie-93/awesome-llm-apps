from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Iterable
from uuid import NAMESPACE_URL, uuid5

from ..core.models import SourceDocument

SUPPORTED_SUFFIXES = {".md", ".txt", ".json", ".csv", ".pdf"}


def load_sources(target: Path, default_knowledge_base: str) -> list[SourceDocument]:
    files = _resolve_files(target)
    root = target if target.is_dir() else target.parent
    documents: list[SourceDocument] = []

    for path in files:
        content, content_type = _read_file(path)
        knowledge_base = _infer_knowledge_base(path, root, default_knowledge_base)
        documents.append(
            SourceDocument(
                source_id=str(uuid5(NAMESPACE_URL, str(path.resolve()))),
                knowledge_base=knowledge_base,
                path=str(path.resolve()),
                title=path.stem.replace("_", " ").strip() or path.name,
                content=content,
                content_type=content_type,
                metadata={"filename": path.name, "suffix": path.suffix.lower()},
            )
        )

    return documents


def _resolve_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target]
    if target.is_dir():
        return sorted(
            path for path in target.rglob("*") if path.is_file() and path.suffix.lower() in SUPPORTED_SUFFIXES
        )
    raise FileNotFoundError(target)


def _infer_knowledge_base(path: Path, root: Path, default_knowledge_base: str) -> str:
    try:
        relative = path.resolve().relative_to(root.resolve())
    except ValueError:
        return default_knowledge_base
    parts = relative.parts
    if len(parts) >= 2:
        return parts[0]
    return default_knowledge_base


def _read_file(path: Path) -> tuple[str, str]:
    suffix = path.suffix.lower()
    if suffix in {".md", ".txt"}:
        return path.read_text(encoding="utf-8", errors="ignore").strip(), "markdown" if suffix == ".md" else "text"
    if suffix == ".json":
        raw = json.loads(path.read_text(encoding="utf-8", errors="ignore"))
        return _flatten_json(raw).strip(), "json"
    if suffix == ".csv":
        return _flatten_csv(path).strip(), "csv"
    if suffix == ".pdf":
        return _read_pdf(path).strip(), "pdf"
    return "", "text"


def _flatten_json(value: object, prefix: str = "") -> str:
    lines: list[str] = []
    if isinstance(value, dict):
        for key, item in value.items():
            next_prefix = f"{prefix}{key}" if prefix else str(key)
            lines.append(_flatten_json(item, f"{next_prefix}."))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            lines.append(_flatten_json(item, f"{prefix}{index}."))
    else:
        label = prefix[:-1] if prefix.endswith(".") else prefix
        lines.append(f"{label}: {value}" if label else str(value))
    return "\n".join(line for line in lines if line)


def _flatten_csv(path: Path) -> str:
    rows: list[str] = []
    with path.open("r", encoding="utf-8", errors="ignore", newline="") as handle:
        for row in csv.reader(handle):
            cleaned = [cell.strip() for cell in row if cell.strip()]
            if cleaned:
                rows.append(" | ".join(cleaned))
    return "\n".join(rows)


def _read_pdf(path: Path) -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        return f"PDF support unavailable for {path.name}"

    reader = PdfReader(str(path))
    pages: list[str] = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    return "\n\n".join(part for part in pages if part.strip())
