import json

import pytest

from tools.question_builder.generators.drone_question_generator import (
    DroneQuestionGenerator,
)


def build_question(
    number,
):
    return {
        "question": (
            f"ドローン問題{number}"
        ),
        "choices": [
            f"正しい選択肢{number}",
            f"誤りの選択肢A{number}",
            f"誤りの選択肢B{number}",
        ],
        "answer": 0,
        "explanation": (
            f"問題{number}の解説"
        ),
        "figureType": "none",
        "figureData": {},
    }


def test_build_prompt_returns_prompt():
    generator = DroneQuestionGenerator()

    result = generator.build_prompt(
        {
            "prompt": "問題を2問生成",
            "expected_count": 2,
        }
    )

    assert result == "問題を2問生成"


@pytest.mark.parametrize(
    "prompt",
    [
        "",
        "   ",
        None,
    ],
)
def test_build_prompt_rejects_invalid_prompt(
    prompt,
):
    generator = DroneQuestionGenerator()

    with pytest.raises(
        ValueError,
        match="prompt must be a non-empty string",
    ):
        generator.build_prompt(
            {
                "prompt": prompt,
                "expected_count": 2,
            }
        )


@pytest.mark.parametrize(
    "expected_count",
    [
        0,
        51,
        -1,
    ],
)
def test_build_prompt_rejects_out_of_range_count(
    expected_count,
):
    generator = DroneQuestionGenerator()

    with pytest.raises(
        ValueError,
        match="between 1 and 50",
    ):
        generator.build_prompt(
            {
                "prompt": "Generate",
                "expected_count": (
                    expected_count
                ),
            }
        )


@pytest.mark.parametrize(
    "expected_count",
    [
        None,
        "2",
        2.0,
    ],
)
def test_build_prompt_rejects_non_integer_count(
    expected_count,
):
    generator = DroneQuestionGenerator()

    with pytest.raises(
        ValueError,
        match="must be an integer",
    ):
        generator.build_prompt(
            {
                "prompt": "Generate",
                "expected_count": (
                    expected_count
                ),
            }
        )


def test_parse_response_returns_valid_questions():
    generator = DroneQuestionGenerator()

    response_text = json.dumps(
        [
            build_question(1),
            build_question(2),
        ],
        ensure_ascii=False,
    )

    result = generator.parse_response(
        response_text=response_text,
        input_data={
            "expected_count": 2,
        },
    )

    assert len(result) == 2
    assert result[0]["question"] == (
        "ドローン問題1"
    )


def test_parse_response_rejects_wrong_count():
    generator = DroneQuestionGenerator()

    response_text = json.dumps(
        [
            build_question(1),
        ],
        ensure_ascii=False,
    )

    with pytest.raises(
        ValueError,
        match="Generated item count does not match",
    ):
        generator.parse_response(
            response_text=response_text,
            input_data={
                "expected_count": 2,
            },
        )


def test_parse_response_rejects_invalid_question():
    generator = DroneQuestionGenerator()

    invalid = build_question(1)
    invalid["choices"] = [
        "重複",
        "重複",
        "別",
    ]

    response_text = json.dumps(
        [invalid],
        ensure_ascii=False,
    )

    with pytest.raises(
        ValueError,
        match="must not contain duplicates",
    ):
        generator.parse_response(
            response_text=response_text,
            input_data={
                "expected_count": 1,
            },
        )


def test_validate_cached_result_accepts_valid_list():
    generator = DroneQuestionGenerator()

    cached = [
        build_question(1),
        build_question(2),
    ]

    result = generator.validate_cached_result(
        cached=cached,
        input_data={
            "expected_count": 2,
        },
    )

    assert result == cached


def test_validate_cached_result_rejects_object():
    generator = DroneQuestionGenerator()

    with pytest.raises(
        ValueError,
        match="JSON root must be an array",
    ):
        generator.validate_cached_result(
            cached={
                "question": "invalid",
            },
            input_data={
                "expected_count": 1,
            },
        )


def test_validate_cached_result_rejects_wrong_count():
    generator = DroneQuestionGenerator()

    with pytest.raises(
        ValueError,
        match="キャッシュ内の問題数",
    ):
        generator.validate_cached_result(
            cached=[
                build_question(1),
            ],
            input_data={
                "expected_count": 2,
            },
        )
