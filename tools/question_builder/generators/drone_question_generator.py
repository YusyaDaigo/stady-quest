from __future__ import annotations

from pathlib import Path
from typing import Any

from tools.question_builder.generators.base_generator import (
    BaseGenerator,
    GeneratedData,
)
from tools.question_builder.drone_question_response_parser import (
    parse_drone_question_response,
)
from tools.question_builder.validators.drone_validator import (
    validate_drone_generated_question,
)


class DroneQuestionGenerator(
    BaseGenerator
):
    """
    無人航空機問題を一括生成するGenerator。
    """

    def __init__(self) -> None:
        super().__init__(
            model="gpt-5.5",
            cache_dir=Path(
                "generated_questions/cache/"
                "drone_questions"
            ),
            max_api_calls=1,
        )

    def build_prompt(
        self,
        input_data: dict[str, Any],
    ) -> str:
        prompt = input_data.get("prompt")

        if not isinstance(prompt, str) or not prompt.strip():
            raise ValueError(
                "prompt must be a non-empty string"
            )

        expected_count = input_data.get(
            "expected_count"
        )

        if not isinstance(expected_count, int):
            raise ValueError(
                "expected_count must be an integer"
            )

        if not 1 <= expected_count <= 50:
            raise ValueError(
                "expected_count must be between 1 and 50"
            )

        return prompt

    def build_cache_payload(
        self,
        input_data: dict[str, Any],
        prompt: str,
    ) -> dict[str, Any]:
        """
        旧ドローンGeneratorと同じキャッシュキーを維持する。
        """

        del input_data

        return {
            "prompt": prompt,
            "model": self.model,
        }

    def parse_response(
        self,
        response_text: str,
        input_data: dict[str, Any],
    ) -> list[dict[str, Any]]:
        expected_count = input_data[
            "expected_count"
        ]

        questions = parse_drone_question_response(
            response_text=response_text,
            expected_count=expected_count,
        )

        for index, question in enumerate(
            questions,
            start=1,
        ):
            validate_drone_generated_question(
                question,
                index=index,
            )

        return questions

    def validate_cached_result(
        self,
        cached: GeneratedData,
        input_data: dict[str, Any],
    ) -> list[dict[str, Any]]:
        expected_count = input_data[
            "expected_count"
        ]

        if not isinstance(cached, list):
            raise ValueError(
                "Invalid drone question cache: "
                "JSON root must be an array"
            )

        if len(cached) != expected_count:
            raise ValueError(
                "キャッシュ内の問題数が要求数と"
                "一致しません。"
                f" expected={expected_count}, "
                f"actual={len(cached)}"
            )

        if not all(
            isinstance(item, dict)
            for item in cached
        ):
            raise ValueError(
                "Invalid drone question cache items"
            )

        questions: list[dict[str, Any]] = cached

        for index, question in enumerate(
            questions,
            start=1,
        ):
            validate_drone_generated_question(
                question,
                index=index,
            )

        return questions
