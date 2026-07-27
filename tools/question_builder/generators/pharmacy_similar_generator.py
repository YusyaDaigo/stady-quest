from __future__ import annotations

import json

from pathlib import Path
from typing import Any

from tools.question_builder.generated_question_pipeline import (
    validate_generated_question,
)
from tools.question_builder.generators.base_generator import (
    BaseGenerator,
    GeneratedData,
)
from tools.question_builder.similar_question_generator import (
    validate_source_question,
)
from tools.question_builder.similar_question_response_parser import (
    parse_similar_question_response,
)


class PharmacySimilarGenerator(
    BaseGenerator
):
    """
    薬剤師国家試験の類題生成Generator。
    """

    template_path = Path(
        "tools/question_builder/templates/"
        "pharmacy_similar.md"
    )

    partial_paths: tuple[Path, ...] = ()

    def __init__(self) -> None:
        super().__init__(
            model="gpt-5.5",
            cache_dir=Path(
                "generated_questions/cache/"
                "similar_questions"
            ),
            max_api_calls=1,
        )

    def build_prompt_variables(
        self,
        input_data: dict[str, Any],
    ) -> dict[str, Any]:
        validate_source_question(
            input_data
        )

        source_json = json.dumps(
            input_data,
            ensure_ascii=False,
            indent=2,
        )

        return {
            "SOURCE_QUESTION_JSON": (
                source_json
            ),
        }

    def parse_response(
        self,
        response_text: str,
        input_data: dict[str, Any],
    ) -> dict[str, Any]:
        del input_data

        return parse_similar_question_response(
            response_text
        )

    def validate_cached_result(
        self,
        cached: GeneratedData,
        input_data: dict[str, Any],
    ) -> dict[str, Any]:
        del input_data

        if not isinstance(cached, dict):
            raise ValueError(
                "Invalid pharmacy question cache: "
                "JSON root must be an object"
            )

        validate_generated_question(
            cached
        )

        return cached
