from copy import deepcopy

import pytest

from tools.question_builder.validators.drone_validator import (
    validate_drone_generated_question,
)


@pytest.fixture
def valid_question():
    return {
        "question": "無人航空機を安全に飛行させるために必要な確認はどれか。",
        "choices": [
            "周辺状況を確認する",
            "確認せず直ちに飛行する",
            "機体を目視しない",
        ],
        "answer": 0,
        "explanation": "飛行前には周辺状況と機体状態の確認が必要である。",
        "figureType": "none",
        "figureData": {},
    }


def test_valid_drone_question_passes(
    valid_question,
):
    validate_drone_generated_question(
        valid_question
    )


def test_question_must_be_object():
    with pytest.raises(
        ValueError,
        match="Question must be an object",
    ):
        validate_drone_generated_question(
            []
        )


def test_empty_question_is_rejected(
    valid_question,
):
    question = deepcopy(valid_question)
    question["question"] = ""

    with pytest.raises(
        ValueError,
        match="question must not be empty",
    ):
        validate_drone_generated_question(
            question
        )


def test_empty_explanation_is_rejected(
    valid_question,
):
    question = deepcopy(valid_question)
    question["explanation"] = " "

    with pytest.raises(
        ValueError,
        match="explanation must not be empty",
    ):
        validate_drone_generated_question(
            question
        )


def test_wrong_choice_count_is_rejected(
    valid_question,
):
    question = deepcopy(valid_question)
    question["choices"] = [
        "A",
        "B",
    ]

    with pytest.raises(
        ValueError,
        match="exactly 3 items",
    ):
        validate_drone_generated_question(
            question
        )


def test_duplicate_choices_are_rejected(
    valid_question,
):
    question = deepcopy(valid_question)
    question["choices"] = [
        "同じ",
        "同じ",
        "別",
    ]

    with pytest.raises(
        ValueError,
        match="must not contain duplicates",
    ):
        validate_drone_generated_question(
            question
        )


def test_invalid_answer_is_rejected(
    valid_question,
):
    question = deepcopy(valid_question)
    question["answer"] = 3

    with pytest.raises(
        ValueError,
        match="answer must be between",
    ):
        validate_drone_generated_question(
            question
        )


def test_unknown_figure_type_is_rejected(
    valid_question,
):
    question = deepcopy(valid_question)
    question["figureType"] = "pie_chart"

    with pytest.raises(
        ValueError,
        match="unsupported figureType",
    ):
        validate_drone_generated_question(
            question
        )


def test_figure_data_must_be_object(
    valid_question,
):
    question = deepcopy(valid_question)
    question["figureData"] = None

    with pytest.raises(
        ValueError,
        match="figureData must be an object",
    ):
        validate_drone_generated_question(
            question
        )


def test_error_contains_question_index(
    valid_question,
):
    question = deepcopy(valid_question)
    question["question"] = ""

    with pytest.raises(
        ValueError,
        match="Question 7",
    ):
        validate_drone_generated_question(
            question,
            index=7,
        )
