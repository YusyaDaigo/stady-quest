from __future__ import annotations

from typing import Any, Collection


def validate_non_empty_string(
    value: Any,
    *,
    field_name: str,
    context: str = "Question",
) -> None:
    if not isinstance(value, str):
        raise ValueError(
            f"{context}: {field_name} must be a string"
        )

    if not value.strip():
        raise ValueError(
            f"{context}: {field_name} must not be empty"
        )


def validate_choices(
    choices: Any,
    *,
    expected_count: int | None = None,
    context: str = "Question",
) -> list[str]:
    if not isinstance(choices, list):
        raise ValueError(
            f"{context}: choices must be a list"
        )

    if expected_count is not None and len(choices) != expected_count:
        raise ValueError(
            f"{context}: choices must contain exactly "
            f"{expected_count} items"
        )

    if not all(
        isinstance(choice, str) and choice.strip()
        for choice in choices
    ):
        raise ValueError(
            f"{context}: every choice must be "
            "a non-empty string"
        )

    normalized = [
        choice.strip()
        for choice in choices
    ]

    if len(set(normalized)) != len(normalized):
        raise ValueError(
            f"{context}: choices must not contain duplicates"
        )

    return normalized


def validate_answer(
    answer: Any,
    *,
    choice_count: int,
    context: str = "Question",
) -> None:
    if not isinstance(answer, int) or isinstance(answer, bool):
        raise ValueError(
            f"{context}: answer must be an integer"
        )

    if not 0 <= answer < choice_count:
        raise ValueError(
            f"{context}: answer must be between "
            f"0 and {choice_count - 1}"
        )


def validate_figure_type(
    figure_type: Any,
    *,
    allowed_types: Collection[str],
    context: str = "Question",
) -> str:
    if not isinstance(figure_type, str):
        raise ValueError(
            f"{context}: figureType must be a string"
        )

    if figure_type not in allowed_types:
        raise ValueError(
            f"{context}: unsupported "
            f"figureType={figure_type}"
        )

    return figure_type
