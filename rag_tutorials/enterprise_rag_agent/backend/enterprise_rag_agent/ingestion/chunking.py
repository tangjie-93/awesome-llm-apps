from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(slots=True)
class SectionBlock:
    section_path: str
    text: str


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    return text.strip()


def split_sections(text: str, content_type: str) -> list[SectionBlock]:
    clean_text = normalize_text(text)
    if not clean_text:
        return []
    if content_type != "markdown":
        return [SectionBlock(section_path="Document", text=clean_text)]

    lines = clean_text.splitlines()
    blocks: list[SectionBlock] = []
    current_headers: list[str] = []
    buffer: list[str] = []

    def flush() -> None:
        if buffer:
            section_path = " > ".join(current_headers) if current_headers else "Document"
            blocks.append(SectionBlock(section_path=section_path, text=normalize_text("\n".join(buffer))))
            buffer.clear()

    for line in lines:
        match = re.match(r"^(#{1,6})\s+(.*)$", line.strip())
        if match:
            flush()
            level = len(match.group(1))
            title = match.group(2).strip()
            current_headers[:] = current_headers[: level - 1]
            current_headers.append(title)
            continue
        buffer.append(line)

    flush()
    return blocks or [SectionBlock(section_path="Document", text=clean_text)]


def chunk_text(text: str, chunk_size: int, overlap: int) -> list[str]:
    clean_text = normalize_text(text)
    if not clean_text:
        return []

    if len(clean_text) <= chunk_size:
        return [clean_text]

    pieces: list[str] = []
    step = max(1, chunk_size - overlap)
    start = 0
    while start < len(clean_text):
        end = min(len(clean_text), start + chunk_size)
        piece = clean_text[start:end].strip()
        if piece:
            pieces.append(piece)
        if end >= len(clean_text):
            break
        start += step
    return pieces

