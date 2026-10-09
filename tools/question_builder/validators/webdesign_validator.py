from __future__ import annotations

from typing import Any, Iterable

from tools.question_builder.exam_generation_profiles import (
    get_exam_generation_profile,
)
from tools.question_builder.validators.base_validator import (
    validate_answer,
    validate_choices,
    validate_figure_type,
    validate_non_empty_string,
)


_PROFILE = get_exam_generation_profile(
    "webdesign"
)

WEBDESIGN_FIGURE_TYPES = set(
    _PROFILE["supportedFigureTypes"]
)

WEBDESIGN_QUESTION_TYPES = {
    question_type: int(config["choiceCount"])
    for question_type, config
    in _PROFILE["questionTypes"].items()
}


def validate_webdesign_generated_question(
    question: dict[str, Any],
    *,
    index: int | None = None,
    expected_question_type: str | None = None,
    allowed_source_knowledge_ids: (
        Iterable[str] | None
    ) = None,
) -> None:
    """
    AIが生成したウェブデザイン技能検定3級の
    学科問題構造を検証する。
    """

    if not isinstance(question, dict):
        raise ValueError(
            "Question must be an object"
        )

    context = (
        f"Question {index}"
        if index is not None
        else "Question"
    )

    question_type = question.get(
        "questionType"
    )

    if question_type not in WEBDESIGN_QUESTION_TYPES:
        raise ValueError(
            f"{context}: invalid questionType: "
            f"{question_type}"
        )

    if (
        expected_question_type is not None
        and question_type
        != expected_question_type
    ):
        raise ValueError(
            f"{context}: questionType must be "
            f"{expected_question_type}, "
            f"got {question_type}"
        )

    validate_non_empty_string(
        question.get("question"),
        field_name="question",
        context=context,
    )

    validate_non_empty_string(
        question.get("explanation"),
        field_name="explanation",
        context=context,
    )

    expected_choice_count = (
        WEBDESIGN_QUESTION_TYPES[
            question_type
        ]
    )

    choices = validate_choices(
        question.get("choices"),
        expected_count=expected_choice_count,
        context=context,
    )

    validate_answer(
        question.get("answer"),
        choice_count=len(choices),
        context=context,
    )

    validate_figure_type(
        question.get("figureType"),
        allowed_types=WEBDESIGN_FIGURE_TYPES,
        context=context,
    )

    figure_data = question.get(
        "figureData"
    )

    if not isinstance(figure_data, dict):
        raise ValueError(
            f"{context}: figureData must be an object"
        )

    source_knowledge_ids = question.get(
        "sourceKnowledgeIds"
    )

    if (
        not isinstance(
            source_knowledge_ids,
            list,
        )
        or not source_knowledge_ids
    ):
        raise ValueError(
            f"{context}: "
            "sourceKnowledgeIds must be "
            "a non-empty array"
        )

    normalized_source_ids = []

    for source_id in source_knowledge_ids:
        if (
            not isinstance(
                source_id,
                str,
            )
            or not source_id.strip()
        ):
            raise ValueError(
                f"{context}: "
                "sourceKnowledgeIds must "
                "contain non-empty strings"
            )

        normalized_source_ids.append(
            source_id.strip()
        )

    if (
        len(
            set(
                normalized_source_ids
            )
        )
        != len(
            normalized_source_ids
        )
    ):
        raise ValueError(
            f"{context}: "
            "sourceKnowledgeIds contains "
            "duplicates"
        )

    if (
        allowed_source_knowledge_ids
        is not None
    ):
        allowed_ids = {
            str(source_id).strip()
            for source_id
            in allowed_source_knowledge_ids
            if str(source_id).strip()
        }

        invalid_ids = [
            source_id
            for source_id
            in normalized_source_ids
            if source_id
            not in allowed_ids
        ]

        if invalid_ids:
            raise ValueError(
                f"{context}: "
                "sourceKnowledgeIds contains "
                "unknown ids: "
                f"{invalid_ids}"
            )
