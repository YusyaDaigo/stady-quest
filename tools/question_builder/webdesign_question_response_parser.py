from __future__ import annotations

from typing import Any

from tools.question_builder.core.parser import (
    parse_json_array,
)
from tools.question_builder.validators.webdesign_validator import (
    validate_webdesign_generated_question,
)


def parse_webdesign_question_response(
    response_text: str,
    expected_count: int,
    expected_question_type: str,
    allowed_source_knowledge_ids: (
        list[str] | None
    ) = None,
) -> list[dict[str, Any]]:
    """
    AIレスポンスをWebDesign問題配列として解析し、
    各問題を検証する。
    """

    questions = parse_json_array(
        response_text,
        expected_count=expected_count,
    )

    for index, question in enumerate(
        questions,
        start=1,
    ):
        validate_webdesign_generated_question(
            question,
            index=index,
            expected_question_type=(
                expected_question_type
            ),
            allowed_source_knowledge_ids=(
                allowed_source_knowledge_ids
            ),
        )

    return questions
