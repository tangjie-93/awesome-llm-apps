from __future__ import annotations

import hashlib
import logging
import math
import re
import time
from typing import Protocol

EMBEDDING_DIMENSIONS = 128
TOKEN_PATTERN = re.compile(r"[\w\u4e00-\u9fff]+", re.UNICODE)
OPENAI_EMBEDDING_MAX_ATTEMPTS = 3
OPENAI_EMBEDDING_RETRY_DELAY_SECONDS = 0.5
logger = logging.getLogger(__name__)


class EmbeddingServiceUnavailable(RuntimeError):
    pass


class EmbeddingGenerator(Protocol):
    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        ...


class LocalHashingEmbeddingGenerator:
    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        return [embed_text(text) for text in texts]


class OpenAIEmbeddingGenerator:
    def __init__(self, model: str, api_key: str | None = None, base_url: str | None = None) -> None:
        self.model = model
        self.api_key = api_key
        self.base_url = base_url
        self.fallback = LocalHashingEmbeddingGenerator()

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        if not self.api_key:
            raise RuntimeError("Embedding API key is required for OpenAI embeddings")
        if not texts:
            return []

        try:
            from openai import APIConnectionError, APIStatusError, OpenAI
        except ImportError as exc:
            raise RuntimeError("openai package is not installed") from exc

        client = OpenAI(api_key=self.api_key, base_url=self.base_url)
        for attempt in range(OPENAI_EMBEDDING_MAX_ATTEMPTS):
            try:
                response = client.embeddings.create(model=self.model, input=texts)
                break
            except APIStatusError as exc:
                if exc.status_code != 503:
                    raise
                if attempt == OPENAI_EMBEDDING_MAX_ATTEMPTS - 1:
                    return self._fallback(texts, exc)
                time.sleep(OPENAI_EMBEDDING_RETRY_DELAY_SECONDS * (2**attempt))
            except APIConnectionError as exc:
                if attempt == OPENAI_EMBEDDING_MAX_ATTEMPTS - 1:
                    return self._fallback(texts, exc)
                time.sleep(OPENAI_EMBEDDING_RETRY_DELAY_SECONDS * (2**attempt))
        else:
            return self._fallback(texts)

        items = sorted(response.data, key=lambda item: item.index)
        return [list(item.embedding) for item in items]

    def _fallback(self, texts: list[str], cause: Exception | None = None) -> list[list[float]]:
        logger.warning(
            "Embedding service unavailable; using local hashing embeddings%s",
            f": {cause}" if cause else "",
        )
        return self.fallback.embed_texts(texts)


def create_embedding_generator(
    provider: str,
    model: str,
    api_key: str | None,
    base_url: str | None,
) -> EmbeddingGenerator:
    if provider == "local":
        return LocalHashingEmbeddingGenerator()
    if provider in {"openai", "chatgpt"}:
        return OpenAIEmbeddingGenerator(model=model, api_key=api_key, base_url=base_url)
    raise ValueError(f"Unsupported embedding provider: {provider}")


def _tokenize(text: str) -> list[str]:
    return [token.lower() for token in TOKEN_PATTERN.findall(text)]


def embed_text(text: str, dimensions: int = EMBEDDING_DIMENSIONS) -> list[float]:
    tokens = _tokenize(text)
    vector = [0.0] * dimensions
    if not tokens:
        return vector

    for token in tokens:
        digest = hashlib.sha256(token.encode("utf-8")).digest()
        index = int.from_bytes(digest[:4], "big") % dimensions
        sign = 1.0 if digest[4] % 2 == 0 else -1.0
        vector[index] += sign

    norm = math.sqrt(sum(value * value for value in vector))
    if norm == 0:
        return vector
    return [value / norm for value in vector]


def cosine_similarity(left: list[float], right: list[float]) -> float:
    if not left or not right or len(left) != len(right):
        return 0.0
    return sum(left_value * right_value for left_value, right_value in zip(left, right))
