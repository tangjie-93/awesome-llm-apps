from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
import struct
from typing import Iterable
from uuid import NAMESPACE_URL, uuid5

from ..core.models import SourceDocument

SUPPORTED_SUFFIXES = {".md", ".txt", ".json", ".csv", ".pdf", ".png", ".jpg", ".jpeg"}


def load_sources(
    target: Path,
    default_knowledge_base: str,
    tenant_id: str = "default",
) -> list[SourceDocument]:
    files = _resolve_files(target)
    root = target if target.is_dir() else target.parent
    documents: list[SourceDocument] = []

    for path in files:
        content, content_type = _read_file(path)
        knowledge_base = _infer_knowledge_base(path, root, default_knowledge_base)
        documents.append(
            SourceDocument(
                source_id=str(uuid5(NAMESPACE_URL, f"{tenant_id}:{path.resolve()}")),
                tenant_id=tenant_id,
                knowledge_base=knowledge_base,
                path=str(path.resolve()),
                title=path.stem.replace("_", " ").strip() or path.name,
                content=content,
                content_type=content_type,
                content_hash=_content_hash(path, content, content_type),
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
    if suffix in {".png", ".jpg", ".jpeg"}:
        return _read_image(path), "image"
    return "", "text"


def _content_hash(path: Path, content: str, content_type: str) -> str:
    if content_type == "image":
        return hashlib.sha256(path.read_bytes()).hexdigest()
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


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


def _read_image(path: Path) -> str:
    """生成图片的可检索文本，优先使用同名人工说明文件，避免依赖外部视觉服务。"""
    width, height = _image_dimensions(path)
    filename = path.stem.replace("_", " ").replace("-", " ").strip()
    captions: list[str] = []
    for suffix in (".caption.txt", ".caption.md", ".txt", ".md"):
        sidecar = path.with_name(f"{path.stem}{suffix}")
        if sidecar.exists() and sidecar != path:
            caption = sidecar.read_text(encoding="utf-8", errors="ignore").strip()
            if caption:
                captions.append(caption)
            break
    description = "\n".join(captions) or "未提供人工图片说明。"
    return (
        f"图片文件：{path.name}\n"
        f"图片名称：{filename}\n"
        f"图片尺寸：{width} x {height}\n"
        f"图片说明：{description}"
    )


def _image_dimensions(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    if data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) >= 24:
        return struct.unpack(">II", data[16:24])
    if data.startswith(b"\xff\xd8"):
        index = 2
        while index + 9 < len(data):
            if data[index] != 0xFF:
                index += 1
                continue
            marker = data[index + 1]
            index += 2
            if marker in {0xD8, 0xD9}:
                continue
            if index + 2 > len(data):
                break
            length = int.from_bytes(data[index:index + 2], "big")
            if length < 2 or index + length > len(data):
                break
            if marker in {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}:
                return (
                    int.from_bytes(data[index + 5:index + 7], "big"),
                    int.from_bytes(data[index + 3:index + 5], "big"),
                )
            index += length
    return 0, 0
