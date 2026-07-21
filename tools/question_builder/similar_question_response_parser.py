from __future__ import annotations

from typing import Any

from tools.question_builder.core.parser import (
    parse_json_object,
)
from tools.question_builder.generated_question_pipeline import (
    validate_generated_question,
)


def parse_similar_question_response(
    response_text: str,
) -> dict[str, Any]:
    """
    AIレスポンスを1問分のJSONとして解析・検証する。
    """

    data = parse_json_object(
        response_text
    )

    validate_generated_question(
        data
    )

    return data
