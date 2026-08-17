from __future__ import annotations

from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

import httpx
from openai import APIStatusError

from enterprise_rag_agent.retrieval.embeddings import (
    OpenAIEmbeddingGenerator,
)


class EmbeddingGeneratorTest(unittest.TestCase):
    def test_retries_temporary_503_and_returns_embedding(self) -> None:
        error = APIStatusError(
            "temporarily unavailable",
            response=httpx.Response(503, request=httpx.Request("POST", "https://example.test/embeddings")),
            body={"error": {"message": "Service temporarily unavailable"}},
        )
        response = SimpleNamespace(
            data=[SimpleNamespace(index=0, embedding=[0.1, 0.2])],
        )
        client = SimpleNamespace(
            embeddings=SimpleNamespace(create=Mock(side_effect=[error, response])),
        )
        generator = OpenAIEmbeddingGenerator("text-embedding-3-small", api_key="test-key")

        with patch("openai.OpenAI", return_value=client), patch(
            "enterprise_rag_agent.retrieval.embeddings.time.sleep"
        ) as sleep:
            result = generator.embed_texts(["hello"])

        self.assertEqual(result, [[0.1, 0.2]])
        self.assertEqual(client.embeddings.create.call_count, 2)
        sleep.assert_called_once()

    def test_falls_back_to_local_embedding_after_repeated_503(self) -> None:
        error = APIStatusError(
            "temporarily unavailable",
            response=httpx.Response(503, request=httpx.Request("POST", "https://example.test/embeddings")),
            body={"error": {"message": "Service temporarily unavailable"}},
        )
        client = SimpleNamespace(
            embeddings=SimpleNamespace(create=Mock(side_effect=error)),
        )
        generator = OpenAIEmbeddingGenerator("text-embedding-3-small", api_key="test-key")

        with patch("openai.OpenAI", return_value=client), patch(
            "enterprise_rag_agent.retrieval.embeddings.time.sleep"
        ):
            result = generator.embed_texts(["hello"])

        self.assertEqual(client.embeddings.create.call_count, 3)
        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]), 128)


if __name__ == "__main__":
    unittest.main()
