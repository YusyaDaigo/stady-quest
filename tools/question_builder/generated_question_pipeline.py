from pathlib import Path
from typing import Any, Dict

from tools.question_builder.figure_pipeline import (
    attach_generated_figure,
)


REQUIRED_QUESTION_FIELDS = {
    "question",
    "choices",
    "answer",
    "explanation",
    "figureType",
    "figureData",
}


def validate_generated_question(
    question: Dict[str, Any],
) -> None:
    """
    AIが生成した1問分の最低限の形式を検証する。
    """

    if not isinstance(question, dict):
        raise ValueError(
            "generated question must be a dictionary"
        )

    missing_fields = (
        REQUIRED_QUESTION_FIELDS
        - question.keys()
    )

    if missing_fields:
        raise ValueError(
            "generated question is missing required fields: "
            f"{sorted(missing_fields)}"
        )

    if not isinstance(
        question["question"],
        str,
    ) or not question["question"].strip():
        raise ValueError(
            "'question' must be a non-empty string"
        )

    choices = question["choices"]

    if not isinstance(
        choices,
        list,
    ) or not choices:
        raise ValueError(
            "'choices' must be a non-empty list"
        )

    if not all(
        isinstance(choice, str)
        and choice.strip()
        for choice in choices
    ):
        raise ValueError(
            "every choice must be a non-empty string"
        )

    answer = question["answer"]

    if not isinstance(
        answer,
        int,
    ):
        raise ValueError(
            "'answer' must be an integer"
        )

    if not (
        0
        <= answer
        < len(choices)
    ):
        raise ValueError(
            "'answer' must be between "
            f"0 and {len(choices) - 1}"
        )

    if not isinstance(
        question["explanation"],
        str,
    ) or not question["explanation"].strip():
        raise ValueError(
            "'explanation' must be a non-empty string"
        )


def process_generated_question(
    question: Dict[str, Any],
    figure_output_path: str,
    public_image_path: str,
) -> Dict[str, Any]:
    """
    AIが生成した1問分を検証し、
    必要に応じてDiagram Engineで図を生成する。
    """

    validate_generated_question(
        question
    )

    processed = (
        attach_generated_figure(
            question=question,
            output_path=figure_output_path,
            public_image_path=public_image_path,
        )
    )

    return processed


def build_generated_figure_paths(
    exam: str,
    category: str,
    question_id: str,
) -> Dict[str, str]:
    """
    生成問題用のSVG保存パスと公開パスを作る。

    例:
    exam="pharmacy"
    category="required"
    question_id="generated_0001"
    """

    filename = (
        f"{question_id}.svg"
    )

    output_path = (
        Path("public")
        / exam
        / "generated"
        / category
        / filename
    )

    public_path = (
        f"/{exam}/generated/"
        f"{category}/{filename}"
    )

    return {
        "outputPath": str(
            output_path
        ),
        "publicPath": public_path,
    }


def save_generated_question_json(
    question: Dict[str, Any],
    output_path: str,
) -> str:
    """
    処理済みの生成問題をJSONファイルとして保存する。
    """

    import json

    path = Path(
        output_path
    )

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with path.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            question,
            file,
            ensure_ascii=False,
            indent=2,
        )

    return str(path)


def build_generated_question_paths(
    exam: str,
    category: str,
    question_id: str,
) -> Dict[str, str]:
    """
    生成問題のraw / processed JSON保存パスを作る。

    例:
    generated_questions/
        pharmacy/
            required/
                raw/
                    generated_0001.json
                processed/
                    generated_0001.json
    """

    filename = (
        f"{question_id}.json"
    )

    base_path = (
        Path("generated_questions")
        / exam
        / category
    )

    raw_path = (
        base_path
        / "raw"
        / filename
    )

    processed_path = (
        base_path
        / "processed"
        / filename
    )

    return {
        "rawPath": str(
            raw_path
        ),
        "processedPath": str(
            processed_path
        ),
    }


def run_generated_question_pipeline(
    question: Dict[str, Any],
    exam: str,
    category: str,
    question_id: str,
) -> Dict[str, Any]:
    """
    生成問題1問分の完全な後処理パイプライン。

    処理内容:
    1. raw JSON保存
    2. 問題形式チェック
    3. 必要ならDiagram EngineでSVG生成
    4. imageパス付与
    5. processed JSON保存
    6. 処理済み問題を返す
    """

    question_paths = build_generated_question_paths(
        exam=exam,
        category=category,
        question_id=question_id,
    )

    figure_paths = build_generated_figure_paths(
        exam=exam,
        category=category,
        question_id=question_id,
    )

    # AIの生出力を先に保存する。
    save_generated_question_json(
        question=question,
        output_path=question_paths["rawPath"],
    )

    processed = process_generated_question(
        question=question,
        figure_output_path=figure_paths["outputPath"],
        public_image_path=figure_paths["publicPath"],
    )

    save_generated_question_json(
        question=processed,
        output_path=question_paths["processedPath"],
    )

    return processed


def build_study_quest_question(
    processed_question: Dict[str, Any],
    *,
    exam: str,
    category: str,
    source_question: Dict[str, Any],
) -> Dict[str, Any]:
    """
    処理済みの生成問題をStudy QUEST内部形式へ変換する。

    類題のfieldや元問題情報はsource_questionから引き継ぐ。
    """

    validate_generated_question(
        processed_question
    )

    result: Dict[str, Any] = {
        "subject": exam,
        "category": category.upper(),

        "sourceType": "generated",

        "field": source_question.get(
            "field",
            "",
        ),

        "question": processed_question[
            "question"
        ],

        "choices": processed_question[
            "choices"
        ],

        "answer": processed_question[
            "answer"
        ],

        "explanation": processed_question[
            "explanation"
        ],
    }

    question_type = processed_question.get(
        "questionType"
    )

    if question_type is not None:
        result[
            "questionType"
        ] = question_type

    source_exam_number = source_question.get(
        "examNumber"
    )

    if source_exam_number is not None:
        result[
            "sourceExamNumber"
        ] = source_exam_number

    source_number = source_question.get(
        "sourceNumber"
    )

    if source_number is not None:
        result[
            "sourceNumber"
        ] = source_number

    image = processed_question.get(
        "image"
    )

    if image:
        result[
            "hasImage"
        ] = True

        result[
            "image"
        ] = image
    else:
        result[
            "hasImage"
        ] = False

    return result
