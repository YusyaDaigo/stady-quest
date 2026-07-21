import json
from typing import Any, Dict

from tools.question_builder.prompt_loader import (
    render_prompt_template,
)


PHARMACY_SIMILAR_TEMPLATE = (
    "pharmacy_similar"
)


def validate_source_question(
    source_question: Dict[str, Any],
) -> None:
    """
    類題生成元の問題形式を検証する。
    """

    if not isinstance(
        source_question,
        dict,
    ):
        raise ValueError(
            "source_question must be a dictionary"
        )

    required_fields = {
        "question",
        "choices",
        "answer",
        "explanation",
    }

    missing_fields = (
        required_fields
        - source_question.keys()
    )

    if missing_fields:
        raise ValueError(
            "source_question is missing "
            "required fields: "
            f"{sorted(missing_fields)}"
        )

    if not isinstance(
        source_question["question"],
        str,
    ) or not source_question["question"].strip():
        raise ValueError(
            "'question' must be a non-empty string"
        )

    choices = source_question["choices"]

    if not isinstance(
        choices,
        list,
    ) or not choices:
        raise ValueError(
            "'choices' must be a non-empty list"
        )

    answer = source_question["answer"]

    if not isinstance(answer, int):
        raise ValueError(
            "'answer' must be an integer"
        )

    if not 0 <= answer < len(choices):
        raise ValueError(
            "'answer' is outside choices range"
        )


def build_similar_question_prompt(
    source_question: Dict[str, Any],
) -> str:
    """
    元問題1問から薬剤師国家試験の
    類題生成Promptを構築する。
    """

    validate_source_question(
        source_question
    )

    source_json = json.dumps(
        source_question,
        ensure_ascii=False,
        indent=2,
    )

    return render_prompt_template(
        template_name=(
            PHARMACY_SIMILAR_TEMPLATE
        ),
        variables={
            "SOURCE_QUESTION_JSON": (
                source_json
            ),
        },
    )
