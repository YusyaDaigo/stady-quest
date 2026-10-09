from __future__ import annotations

from typing import Any, Callable, Iterable

from tools.question_builder.checkers.semantic_duplicate_checker import (
    WEBDESIGN_DUPLICATE_THRESHOLD,
    WEBDESIGN_REVIEW_THRESHOLD,
    build_question_semantic_text,
    embed_texts,
    is_exact_duplicate,
    rank_embedding_matches,
)


EmbeddingProvider = Callable[
    [list[str], bool],
    list[list[float]],
]


def build_comparison_record(
    *,
    question: dict[str, Any],
    source: str,
    record_id: str,
) -> dict[str, Any]:
    normalized_source = str(
        source
    ).strip()

    normalized_id = str(
        record_id
    ).strip()

    if not normalized_source:
        raise ValueError(
            "source must not be empty"
        )

    if not normalized_id:
        raise ValueError(
            "record_id must not be empty"
        )

    build_question_semantic_text(
        question
    )

    return {
        "source": normalized_source,
        "id": normalized_id,
        "question": question,
    }


def build_app_comparison_records(
    questions: Iterable[
        dict[str, Any]
    ],
) -> list[dict[str, Any]]:
    records = []

    for index, question in enumerate(
        questions,
        start=1,
    ):
        question_id = str(
            question.get(
                "id",
                "",
            )
        ).strip()

        if not question_id:
            question_id = (
                f"app-question-{index}"
            )

        records.append(
            build_comparison_record(
                question=question,
                source="app",
                record_id=question_id,
            )
        )

    return records


def _default_embedding_provider(
    texts: list[str],
    allow_api: bool,
) -> list[list[float]]:
    return embed_texts(
        texts,
        allow_api=allow_api,
    )


def _validate_comparison_records(
    records: list[
        dict[str, Any]
    ],
) -> None:
    seen_keys: set[
        tuple[str, str]
    ] = set()

    for index, record in enumerate(
        records,
        start=1,
    ):
        if not isinstance(
            record,
            dict,
        ):
            raise ValueError(
                "comparison record "
                f"{index} must be an object"
            )

        source = str(
            record.get(
                "source",
                "",
            )
        ).strip()

        record_id = str(
            record.get(
                "id",
                "",
            )
        ).strip()

        question = record.get(
            "question"
        )

        if not source:
            raise ValueError(
                "comparison record "
                f"{index} requires source"
            )

        if not record_id:
            raise ValueError(
                "comparison record "
                f"{index} requires id"
            )

        if not isinstance(
            question,
            dict,
        ):
            raise ValueError(
                "comparison record "
                f"{index} requires question"
            )

        build_question_semantic_text(
            question
        )

        key = (
            source,
            record_id,
        )

        if key in seen_keys:
            raise ValueError(
                "duplicate comparison record: "
                f"{source}:{record_id}"
            )

        seen_keys.add(
            key
        )


def evaluate_webdesign_semantic_gate(
    *,
    candidate: dict[str, Any],
    comparison_records: list[
        dict[str, Any]
    ],
    allow_api: bool = False,
    embedding_provider: (
        EmbeddingProvider | None
    ) = None,
) -> dict[str, Any]:
    candidate_text = (
        build_question_semantic_text(
            candidate
        )
    )

    _validate_comparison_records(
        comparison_records
    )

    for record in comparison_records:
        if is_exact_duplicate(
            candidate,
            record["question"],
        ):
            return {
                "status": "duplicate",
                "matchType": "exact",
                "duplicateThreshold": (
                    WEBDESIGN_DUPLICATE_THRESHOLD
                ),
                "reviewThreshold": (
                    WEBDESIGN_REVIEW_THRESHOLD
                ),
                "topMatch": {
                    "source": (
                        record["source"]
                    ),
                    "id": record["id"],
                    "similarity": 1.0,
                    "status": "duplicate",
                },
                "matches": [
                    {
                        "source": (
                            record["source"]
                        ),
                        "id": record["id"],
                        "similarity": 1.0,
                        "status": (
                            "duplicate"
                        ),
                    }
                ],
            }

    if not comparison_records:
        return {
            "status": "pass",
            "matchType": "none",
            "duplicateThreshold": (
                WEBDESIGN_DUPLICATE_THRESHOLD
            ),
            "reviewThreshold": (
                WEBDESIGN_REVIEW_THRESHOLD
            ),
            "topMatch": None,
            "matches": [],
        }

    if embedding_provider is None:
        embedding_provider = (
            _default_embedding_provider
        )

    comparison_texts = [
        build_question_semantic_text(
            record["question"]
        )
        for record
        in comparison_records
    ]

    texts = [
        candidate_text,
        *comparison_texts,
    ]

    embeddings = embedding_provider(
        texts,
        allow_api,
    )

    if not isinstance(
        embeddings,
        list,
    ):
        raise ValueError(
            "embedding provider "
            "must return a list"
        )

    if len(embeddings) != len(
        texts
    ):
        raise ValueError(
            "embedding count mismatch. "
            f"expected={len(texts)}, "
            f"actual={len(embeddings)}"
        )

    candidate_embedding = (
        embeddings[0]
    )

    comparison_embeddings = (
        embeddings[1:]
    )

    ranked = rank_embedding_matches(
        candidate_embedding,
        comparison_embeddings,
        duplicate_threshold=(
            WEBDESIGN_DUPLICATE_THRESHOLD
        ),
        review_threshold=(
            WEBDESIGN_REVIEW_THRESHOLD
        ),
    )

    matches = []

    for ranked_match in ranked:
        record = comparison_records[
            ranked_match["index"]
        ]

        matches.append(
            {
                "source": (
                    record["source"]
                ),
                "id": record["id"],
                "similarity": (
                    ranked_match[
                        "similarity"
                    ]
                ),
                "status": (
                    ranked_match[
                        "status"
                    ]
                ),
            }
        )

    top_match = (
        matches[0]
        if matches
        else None
    )

    status = (
        top_match["status"]
        if top_match is not None
        else "pass"
    )

    return {
        "status": status,
        "matchType": "semantic",
        "duplicateThreshold": (
            WEBDESIGN_DUPLICATE_THRESHOLD
        ),
        "reviewThreshold": (
            WEBDESIGN_REVIEW_THRESHOLD
        ),
        "topMatch": top_match,
        "matches": matches,
    }
