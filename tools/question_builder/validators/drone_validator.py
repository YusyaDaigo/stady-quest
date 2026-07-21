from __future__ import annotations

from typing import Any

from tools.question_builder.validators.base_validator import (
    validate_answer,
    validate_choices,
    validate_figure_type,
    validate_non_empty_string,
)


DRONE_FIGURE_TYPES = {
    "none",
    "table",
    "line_chart",
    "bar_chart",
    "flowchart",
}


def validate_drone_generated_question(
    question: dict[str, Any],
    *,
    index: int | None = None,
) -> None:
    """
    AIが生成したドローン問題の最低限の構造を検証する。

    ID、難易度、出典などの保存後フィールドは、
    drone_question_bank.validatorで別途検証する。
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

    choices = validate_choices(
        question.get("choices"),
        expected_count=3,
        context=context,
    )

    validate_answer(
        question.get("answer"),
        choice_count=len(choices),
        context=context,
    )

    validate_figure_type(
        question.get("figureType"),
        allowed_types=DRONE_FIGURE_TYPES,
        context=context,
    )

    figure_data = question.get("figureData")

    if not isinstance(figure_data, dict):
        raise ValueError(
            f"{context}: figureData must be an object"
        )
