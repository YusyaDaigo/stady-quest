import json
from typing import Any, Dict

from tools.question_builder.generated_question_pipeline import (
    validate_generated_question,
)


def _strip_markdown_code_fence(
    text: str,
) -> str:
    """
    ```json ... ``` や ``` ... ``` を除去する。
    """

    stripped = text.strip()

    if not stripped.startswith("```"):
        return stripped

    lines = stripped.splitlines()

    if lines and lines[0].startswith("```"):
        lines = lines[1:]

    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]

    return "\n".join(
        lines
    ).strip()


def parse_similar_question_response(
    response_text: str,
) -> Dict[str, Any]:
    """
    AIのレスポンス文字列をJSONとして読み込み、
    生成問題形式を検証してdictで返す。
    """

    if not isinstance(
        response_text,
        str,
    ):
        raise ValueError(
            "response_text must be a string"
        )

    cleaned = _strip_markdown_code_fence(
        response_text
    )

    if not cleaned:
        raise ValueError(
            "AI response is empty"
        )

    try:
        data = json.loads(
            cleaned
        )
    except json.JSONDecodeError as exc:
        raise ValueError(
            "AI response is not valid JSON: "
            f"{exc}"
        ) from exc

    if not isinstance(
        data,
        dict,
    ):
        raise ValueError(
            "AI response JSON must be an object"
        )

    validate_generated_question(
        data
    )

    return data
