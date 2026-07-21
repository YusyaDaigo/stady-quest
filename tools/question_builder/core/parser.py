from __future__ import annotations

import json
import re
from typing import Any


def strip_code_fence(
    response_text: str,
) -> str:
    """
    ```json ... ``` または ``` ... ``` を除去する。
    """

    if not isinstance(response_text, str):
        raise ValueError(
            "response_text must be a string"
        )

    cleaned = response_text.strip()

    if not cleaned:
        raise ValueError(
            "AI response is empty"
        )

    match = re.fullmatch(
        r"```(?:json)?\s*(.*?)\s*```",
        cleaned,
        flags=re.DOTALL | re.IGNORECASE,
    )

    if match:
        return match.group(1).strip()

    return cleaned


def parse_json_response(
    response_text: str,
) -> Any:
    """
    AIレスポンスをJSONとして解析する。
    """

    cleaned = strip_code_fence(
        response_text
    )

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as exc:
        raise ValueError(
            "AI response is not valid JSON: "
            f"{exc}"
        ) from exc


def parse_json_object(
    response_text: str,
) -> dict[str, Any]:
    """
    AIレスポンスをJSONオブジェクトとして解析する。
    """

    data = parse_json_response(
        response_text
    )

    if not isinstance(data, dict):
        raise ValueError(
            "AI response JSON must be an object"
        )

    return data


def parse_json_array(
    response_text: str,
    *,
    expected_count: int | None = None,
) -> list[dict[str, Any]]:
    """
    AIレスポンスを問題オブジェクト配列として解析する。
    """

    data = parse_json_response(
        response_text
    )

    if not isinstance(data, list):
        raise ValueError(
            "AI response JSON must be an array"
        )

    if expected_count is not None:
        if not isinstance(expected_count, int):
            raise ValueError(
                "expected_count must be an integer"
            )

        if expected_count < 1:
            raise ValueError(
                "expected_count must be at least 1"
            )

        if len(data) != expected_count:
            raise ValueError(
                "Generated item count does not match. "
                f"expected={expected_count}, "
                f"actual={len(data)}"
            )

    if not all(
        isinstance(item, dict)
        for item in data
    ):
        raise ValueError(
            "AI response array must contain "
            "only JSON objects"
        )

    return data
