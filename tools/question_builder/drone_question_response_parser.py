from __future__ import annotations

from typing import Any

from tools.question_builder.core.parser import (
    parse_json_array,
)


def parse_drone_question_response(
    response_text: str,
    expected_count: int,
) -> list[dict[str, Any]]:
    """
    AIレスポンスをドローン問題配列として解析する。
    """

    return parse_json_array(
        response_text,
        expected_count=expected_count,
    )
