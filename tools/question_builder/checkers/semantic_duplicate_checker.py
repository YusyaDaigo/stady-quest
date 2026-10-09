from __future__ import annotations

import math
import os
import re
import unicodedata
from pathlib import Path
from typing import Any, Iterable

from dotenv import load_dotenv
from openai import OpenAI


ROOT_DIR = Path(
    __file__
).resolve().parents[3]

load_dotenv(
    dotenv_path=ROOT_DIR / ".env"
)


DEFAULT_EMBEDDING_MODEL = (
    "text-embedding-3-small"
)

WEBDESIGN_DUPLICATE_THRESHOLD = 0.88
WEBDESIGN_REVIEW_THRESHOLD = 0.75


def normalize_exact_text(
    value: str,
) -> str:
    text = unicodedata.normalize(
        "NFKC",
        str(value),
    ).lower()

    return re.sub(
        r"[\W_]+",
        "",
        text,
        flags=re.UNICODE,
    )


def build_question_semantic_text(
    question: dict[str, Any],
) -> str:
    if not isinstance(
        question,
        dict,
    ):
        raise ValueError(
            "question must be an object"
        )

    question_text = str(
        question.get(
            "question",
            "",
        )
    ).strip()

    if not question_text:
        raise ValueError(
            "question text must not be empty"
        )

    parts = [
        f"問題: {question_text}",
    ]

    choices = question.get(
        "choices"
    )

    answer = question.get(
        "answer"
    )

    if (
        isinstance(
            choices,
            list,
        )
        and isinstance(
            answer,
            int,
        )
        and 0
        <= answer
        < len(choices)
    ):
        correct_choice = str(
            choices[answer]
        ).strip()

        if correct_choice:
            parts.append(
                f"正答: {correct_choice}"
            )

    explanation = str(
        question.get(
            "explanation",
            "",
        )
    ).strip()

    if explanation:
        parts.append(
            f"解説: {explanation}"
        )

    return "\n".join(
        parts
    )


def is_exact_duplicate(
    left: dict[str, Any],
    right: dict[str, Any],
) -> bool:
    left_text = normalize_exact_text(
        str(
            left.get(
                "question",
                "",
            )
        )
    )

    right_text = normalize_exact_text(
        str(
            right.get(
                "question",
                "",
            )
        )
    )

    return bool(
        left_text
        and left_text == right_text
    )


def cosine_similarity(
    left: Iterable[float],
    right: Iterable[float],
) -> float:
    left_values = [
        float(value)
        for value in left
    ]

    right_values = [
        float(value)
        for value in right
    ]

    if len(
        left_values
    ) != len(
        right_values
    ):
        raise ValueError(
            "Embedding dimensions do not match"
        )

    if not left_values:
        raise ValueError(
            "Embedding must not be empty"
        )

    dot_product = sum(
        left_value * right_value
        for left_value, right_value
        in zip(
            left_values,
            right_values,
        )
    )

    left_norm = math.sqrt(
        sum(
            value * value
            for value in left_values
        )
    )

    right_norm = math.sqrt(
        sum(
            value * value
            for value in right_values
        )
    )

    if (
        left_norm == 0
        or right_norm == 0
    ):
        return 0.0

    return (
        dot_product
        / (
            left_norm
            * right_norm
        )
    )


def validate_thresholds(
    *,
    duplicate_threshold: float,
    review_threshold: float,
) -> None:
    if not (
        0.0
        <= review_threshold
        <= duplicate_threshold
        <= 1.0
    ):
        raise ValueError(
            "Thresholds must satisfy "
            "0 <= review <= duplicate <= 1"
        )


def classify_similarity(
    similarity: float,
    *,
    duplicate_threshold: float,
    review_threshold: float,
) -> str:
    validate_thresholds(
        duplicate_threshold=(
            duplicate_threshold
        ),
        review_threshold=(
            review_threshold
        ),
    )

    similarity = float(
        similarity
    )

    if similarity >= (
        duplicate_threshold
    ):
        return "duplicate"

    if similarity >= (
        review_threshold
    ):
        return "review"

    return "pass"


def classify_webdesign_similarity(
    similarity: float,
) -> str:
    """
    Classify semantic similarity using the
    provisional WebDesign thresholds.

    These values were calibrated against
    same-concept and different-concept
    WebDesign question samples and should be
    re-evaluated as the sample set grows.
    """

    return classify_similarity(
        similarity,
        duplicate_threshold=(
            WEBDESIGN_DUPLICATE_THRESHOLD
        ),
        review_threshold=(
            WEBDESIGN_REVIEW_THRESHOLD
        ),
    )


def rank_embedding_matches(
    candidate_embedding: Iterable[
        float
    ],
    existing_embeddings: list[
        Iterable[float]
    ],
    *,
    duplicate_threshold: float,
    review_threshold: float,
) -> list[dict[str, Any]]:
    validate_thresholds(
        duplicate_threshold=(
            duplicate_threshold
        ),
        review_threshold=(
            review_threshold
        ),
    )

    matches = []

    for index, embedding in enumerate(
        existing_embeddings
    ):
        similarity = (
            cosine_similarity(
                candidate_embedding,
                embedding,
            )
        )

        matches.append(
            {
                "index": index,
                "similarity": (
                    similarity
                ),
                "status": (
                    classify_similarity(
                        similarity,
                        duplicate_threshold=(
                            duplicate_threshold
                        ),
                        review_threshold=(
                            review_threshold
                        ),
                    )
                ),
            }
        )

    matches.sort(
        key=lambda item: (
            -item["similarity"],
            item["index"],
        )
    )

    return matches


def embed_texts(
    texts: Iterable[str],
    *,
    allow_api: bool = False,
    model: str = (
        DEFAULT_EMBEDDING_MODEL
    ),
) -> list[list[float]]:
    normalized_texts = [
        str(text).strip()
        for text in texts
    ]

    if (
        not normalized_texts
        or any(
            not text
            for text in normalized_texts
        )
    ):
        raise ValueError(
            "texts must contain "
            "non-empty strings"
        )

    if not allow_api:
        raise RuntimeError(
            "Embedding API呼び出しは無効です。"
            "実行する場合は allow_api=True を"
            "明示してください。"
        )

    if (
        os.getenv(
            "STUDY_QUEST_NO_API"
        )
        == "1"
    ):
        raise RuntimeError(
            "STUDY_QUEST_NO_API=1 のため"
            "Embedding APIを呼びません"
        )

    if not os.getenv(
        "OPENAI_API_KEY"
    ):
        raise RuntimeError(
            "OPENAI_API_KEY が"
            "設定されていません"
        )

    print(
        "[API CALL] "
        "semantic embeddings "
        f"count={len(normalized_texts)} "
        f"model={model}"
    )

    client = OpenAI()

    response = (
        client.embeddings.create(
            model=model,
            input=normalized_texts,
        )
    )

    ordered = sorted(
        response.data,
        key=lambda item: item.index,
    )

    if len(
        ordered
    ) != len(
        normalized_texts
    ):
        raise ValueError(
            "Embedding response count mismatch"
        )

    return [
        [
            float(value)
            for value
            in item.embedding
        ]
        for item
        in ordered
    ]
