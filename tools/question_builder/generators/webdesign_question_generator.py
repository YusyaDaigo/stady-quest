from __future__ import annotations

from pathlib import Path
from typing import Any

from tools.question_builder.exam_generation_profiles import (
    get_exam_generation_profile,
)
from tools.question_builder.generators.base_generator import (
    BaseGenerator,
    GeneratedData,
)
from tools.question_builder.webdesign_question_response_parser import (
    parse_webdesign_question_response,
)
from tools.question_builder.validators.webdesign_validator import (
    validate_webdesign_generated_question,
)


_PROFILE = get_exam_generation_profile(
    "webdesign"
)


class WebDesignQuestionGenerator(
    BaseGenerator
):
    """
    ウェブデザイン技能検定3級の
    学科問題を一括生成するGenerator。
    """

    template_path = Path(
        "tools/question_builder/templates/"
        "webdesign.md"
    )

    partial_paths: tuple[Path, ...] = ()

    def __init__(self) -> None:
        super().__init__(
            model="gpt-5.5",
            cache_dir=Path(
                "generated_questions/cache/"
                "webdesign_questions"
            ),
            max_api_calls=1,
        )

    def build_prompt_variables(
        self,
        input_data: dict[str, Any],
    ) -> dict[str, Any]:
        prompt = input_data.get(
            "prompt"
        )

        if (
            not isinstance(prompt, str)
            or not prompt.strip()
        ):
            raise ValueError(
                "prompt must be a non-empty string"
            )

        expected_count = input_data.get(
            "expected_count"
        )

        if not isinstance(
            expected_count,
            int,
        ):
            raise ValueError(
                "expected_count must be an integer"
            )

        if not 1 <= expected_count <= 50:
            raise ValueError(
                "expected_count must be between "
                "1 and 50"
            )

        question_type = input_data.get(
            "question_type"
        )

        if question_type not in _PROFILE[
            "questionTypes"
        ]:
            raise ValueError(
                "Unsupported question_type: "
                f"{question_type}"
            )

        allowed_source_knowledge_ids = (
            input_data.get(
                "allowed_source_knowledge_ids"
            )
        )

        if (
            not isinstance(
                allowed_source_knowledge_ids,
                list,
            )
            or not allowed_source_knowledge_ids
            or any(
                not isinstance(
                    source_id,
                    str,
                )
                or not source_id.strip()
                for source_id
                in allowed_source_knowledge_ids
            )
        ):
            raise ValueError(
                "allowed_source_knowledge_ids "
                "must be a non-empty "
                "list of strings"
            )

        if (
            len(
                {
                    source_id.strip()
                    for source_id
                    in allowed_source_knowledge_ids
                }
            )
            != len(
                allowed_source_knowledge_ids
            )
        ):
            raise ValueError(
                "allowed_source_knowledge_ids "
                "must not contain duplicates"
            )

        return {
            "PROMPT": prompt,
        }

    def parse_response(
        self,
        response_text: str,
        input_data: dict[str, Any],
    ) -> list[dict[str, Any]]:
        return parse_webdesign_question_response(
            response_text=response_text,
            expected_count=input_data[
                "expected_count"
            ],
            expected_question_type=input_data[
                "question_type"
            ],
            allowed_source_knowledge_ids=input_data[
                "allowed_source_knowledge_ids"
            ],
        )

    def validate_cached_result(
        self,
        cached: GeneratedData,
        input_data: dict[str, Any],
    ) -> list[dict[str, Any]]:
        expected_count = input_data[
            "expected_count"
        ]

        question_type = input_data[
            "question_type"
        ]

        if not isinstance(cached, list):
            raise ValueError(
                "Invalid webdesign question cache: "
                "JSON root must be an array"
            )

        if len(cached) != expected_count:
            raise ValueError(
                "Cached question count does not "
                "match. "
                f"expected={expected_count}, "
                f"actual={len(cached)}"
            )

        if not all(
            isinstance(item, dict)
            for item in cached
        ):
            raise ValueError(
                "Invalid webdesign question "
                "cache items"
            )

        questions: list[
            dict[str, Any]
        ] = cached

        for index, question in enumerate(
            questions,
            start=1,
        ):
            validate_webdesign_generated_question(
                question,
                index=index,
                expected_question_type=(
                    question_type
                ),
                allowed_source_knowledge_ids=(
                    input_data[
                        "allowed_source_knowledge_ids"
                    ]
                ),
            )

        return questions
