from __future__ import annotations

from typing import Any

from tools.question_builder.drone_question_response_parser import (
    parse_drone_question_response,
)
from tools.question_builder.generators.drone_question_generator import (
    DroneQuestionGenerator,
)


DRONE_QUESTION_MODEL = "gpt-5.5"

_generator = DroneQuestionGenerator()


def generate_drone_questions(
    prompt: str,
    *,
    expected_count: int,
    allow_api: bool = False,
    use_cache: bool = True,
) -> list[dict[str, Any]]:
    """
    後方互換用ラッパー。

    実際の生成処理はDroneQuestionGeneratorへ委譲する。
    """

    generated = _generator.generate(
        input_data={
            "prompt": prompt,
            "expected_count": expected_count,
        },
        allow_api=allow_api,
        use_cache=use_cache,
    )

    if not isinstance(generated, list):
        raise ValueError(
            "Drone generator result must be a list"
        )

    return generated


__all__ = [
    "DRONE_QUESTION_MODEL",
    "generate_drone_questions",
    "parse_drone_question_response",
]
