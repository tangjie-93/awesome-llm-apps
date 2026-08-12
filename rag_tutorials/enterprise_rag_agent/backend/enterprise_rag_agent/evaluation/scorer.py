from __future__ import annotations

from collections import Counter


def score_answer(expected_answer: str | None, actual_answer: str) -> tuple[float, str]:
    if not expected_answer:
        return 0.0, "No expected answer supplied."

    expected_tokens = _tokens(expected_answer)
    actual_tokens = _tokens(actual_answer)
    if not expected_tokens or not actual_tokens:
        return 0.0, "Empty answer or reference."

    overlap = len(set(expected_tokens) & set(actual_tokens))
    score = overlap / max(1, len(set(expected_tokens)))
    if score >= 0.8:
        notes = "Strong lexical overlap."
    elif score >= 0.4:
        notes = "Partial coverage."
    else:
        notes = "Weak coverage."
    return round(score, 4), notes


def _tokens(text: str) -> list[str]:
    return [token.lower() for token in text.replace("\n", " ").split() if token.strip()]

