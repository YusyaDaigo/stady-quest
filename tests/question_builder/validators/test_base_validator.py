import pytest

from tools.question_builder.validators.base_validator import (
    validate_answer,
    validate_choices,
    validate_figure_type,
    validate_non_empty_string,
)


def test_validate_non_empty_string_accepts_text():
    validate_non_empty_string(
        "問題文",
        field_name="question",
    )


@pytest.mark.parametrize(
    "value",
    [
        "",
        "   ",
        None,
        123,
    ],
)
def test_validate_non_empty_string_rejects_invalid_value(
    value,
):
    with pytest.raises(ValueError):
        validate_non_empty_string(
            value,
            field_name="question",
        )


def test_validate_choices_returns_normalized_choices():
    result = validate_choices(
        [
            " 選択肢A ",
            "選択肢B",
            "選択肢C ",
        ],
        expected_count=3,
    )

    assert result == [
        "選択肢A",
        "選択肢B",
        "選択肢C",
    ]


def test_validate_choices_rejects_non_list():
    with pytest.raises(
        ValueError,
        match="choices must be a list",
    ):
        validate_choices(
            "選択肢A",
            expected_count=3,
        )


def test_validate_choices_rejects_wrong_count():
    with pytest.raises(
        ValueError,
        match="exactly 3 items",
    ):
        validate_choices(
            [
                "A",
                "B",
            ],
            expected_count=3,
        )


def test_validate_choices_rejects_empty_choice():
    with pytest.raises(
        ValueError,
        match="non-empty string",
    ):
        validate_choices(
            [
                "A",
                "",
                "C",
            ],
            expected_count=3,
        )


def test_validate_choices_rejects_duplicates():
    with pytest.raises(
        ValueError,
        match="must not contain duplicates",
    ):
        validate_choices(
            [
                "A",
                "B",
                "A",
            ],
            expected_count=3,
        )


@pytest.mark.parametrize(
    "answer",
    [
        0,
        1,
        2,
    ],
)
def test_validate_answer_accepts_zero_based_index(
    answer,
):
    validate_answer(
        answer,
        choice_count=3,
    )


@pytest.mark.parametrize(
    "answer",
    [
        -1,
        3,
        10,
    ],
)
def test_validate_answer_rejects_out_of_range(
    answer,
):
    with pytest.raises(
        ValueError,
        match="answer must be between",
    ):
        validate_answer(
            answer,
            choice_count=3,
        )


@pytest.mark.parametrize(
    "answer",
    [
        True,
        False,
        "1",
        1.0,
    ],
)
def test_validate_answer_rejects_non_integer(
    answer,
):
    with pytest.raises(
        ValueError,
        match="answer must be an integer",
    ):
        validate_answer(
            answer,
            choice_count=3,
        )


def test_validate_figure_type_accepts_supported_type():
    result = validate_figure_type(
        "table",
        allowed_types={
            "none",
            "table",
        },
    )

    assert result == "table"


def test_validate_figure_type_rejects_unknown_type():
    with pytest.raises(
        ValueError,
        match="unsupported figureType",
    ):
        validate_figure_type(
            "pie_chart",
            allowed_types={
                "none",
                "table",
            },
        )
