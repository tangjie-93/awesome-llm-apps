from __future__ import annotations

import re

from core.models import ChunkRecord

ENGLISH_ENTITY_PATTERN = re.compile(r"\b[A-Z][A-Za-z0-9-]*(?:[ \t]+[A-Z][A-Za-z0-9-]*){0,3}\b")
CAMEL_CASE_ENTITY_PATTERN = re.compile(r"\b[A-Z][a-z]+(?:[A-Z][A-Za-z0-9-]*)+\b")
CHINESE_ENTITY_PATTERN = re.compile(r"[\u4e00-\u9fff]{2,8}")
LEADING_ARTICLES = {"a", "an", "the"}


def extract_entities(text: str, limit: int = 8) -> list[str]:
    """从标题和正文中提取稳定的轻量实体，供本地图谱索引和查询扩展使用。"""
    entities: list[str] = []
    for match in ENGLISH_ENTITY_PATTERN.findall(text):
        words = match.split()
        if words and words[0].lower() in LEADING_ARTICLES:
            words = words[1:]
        entity = " ".join(words).strip()
        if len(entity) >= 3:
            entities.append(entity)
    entities.extend(CAMEL_CASE_ENTITY_PATTERN.findall(text))
    entities.extend(CHINESE_ENTITY_PATTERN.findall(text))

    unique: dict[str, str] = {}
    for entity in entities:
        normalized = normalize_entity(entity)
        if normalized:
            unique.setdefault(normalized, entity)
        if len(unique) >= limit:
            break
    return list(unique.values())


def normalize_entity(entity: str) -> str:
    """统一实体比较键，避免大小写和连续空白导致同一实体被重复存储。"""
    return re.sub(r"\s+", " ", entity).strip().lower()


def build_graph_records(chunks: list[ChunkRecord]) -> tuple[list[tuple[str, str]], list[tuple[str, str, str]]]:
    """根据切块生成实体提及和同块共现关系，返回值可直接写入 SQLite 图谱表。"""
    mentions: list[tuple[str, str]] = []
    relations: list[tuple[str, str, str]] = []
    for chunk in chunks:
        entities = extract_entities(f"{chunk.title}\n{chunk.section_path}\n{chunk.text}")
        normalized_entities = [(normalize_entity(entity), entity) for entity in entities]
        mentions.extend((chunk.chunk_id, entity) for _, entity in normalized_entities)
        for index, (source_key, source_entity) in enumerate(normalized_entities):
            for target_key, target_entity in normalized_entities[index + 1 :]:
                if source_key == target_key:
                    continue
                relations.append((chunk.chunk_id, source_entity, target_entity))
    return mentions, relations
