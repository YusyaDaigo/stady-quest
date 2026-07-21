import argparse
import json
from pathlib import Path
from typing import Any, Dict

from tools.question_builder.generated_question_pipeline import (
    build_study_quest_question,
    run_generated_question_pipeline,
)
from tools.question_builder.generated_question_writer import (
    write_generated_questions_js,
)
from tools.question_builder.openai_similar_question_generator import (
    generate_similar_question,
)


def load_source_question(
    exam: str,
    category: str,
    source_exam: int,
    source_number: int,
) -> Dict[str, Any]:
    """
    現段階ではprocessed JSON等から自動取得せず、
    一時的にソース問題JSONファイルを読む方式にする。

    将来的にはrequired_111.js等から直接取得する。
    """

    source_path = (
        Path("generated_questions")
        / "source_questions"
        / exam
        / category
        / f"{source_exam}_{source_number}.json"
    )

    if not source_path.exists():
        raise FileNotFoundError(
            "元問題JSONが見つかりません: "
            f"{source_path}"
        )

    with source_path.open(
        "r",
        encoding="utf-8",
    ) as file:
        source_question = json.load(file)

    if not isinstance(
        source_question,
        dict,
    ):
        raise ValueError(
            "元問題JSONはobjectである必要があります"
        )

    return source_question


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Study QUEST類題生成CLI"
        )
    )

    parser.add_argument(
        "--exam",
        required=True,
    )

    parser.add_argument(
        "--category",
        required=True,
    )

    parser.add_argument(
        "--source-exam",
        type=int,
        required=True,
    )

    parser.add_argument(
        "--source-number",
        type=int,
        required=True,
    )

    parser.add_argument(
        "--count",
        type=int,
        default=1,
    )

    parser.add_argument(
        "--allow-api",
        action="store_true",
        help=(
            "OpenAI API呼び出しを許可する"
        ),
    )

    args = parser.parse_args()

    if args.count != 1:
        raise ValueError(
            "現在の安全仕様では "
            "--count 1 のみ対応しています"
        )

    source_question = load_source_question(
        exam=args.exam,
        category=args.category,
        source_exam=args.source_exam,
        source_number=args.source_number,
    )

    question_id = (
        f"generated_"
        f"{args.source_exam}_"
        f"{args.source_number}_"
        f"001"
    )

    generated_question = (
        generate_similar_question(
            source_question,
            allow_api=args.allow_api,
            use_cache=True,
        )
    )

    processed_question = (
        run_generated_question_pipeline(
            question=generated_question,
            exam=args.exam,
            category=args.category,
            question_id=question_id,
        )
    )

    study_quest_question = (
        build_study_quest_question(
            processed_question,
            exam=args.exam,
            category=args.category,
            source_question=source_question,
        )
    )

    if (
        args.exam == "pharmacy"
        and args.category == "required"
    ):
        output_path = (
            "src/exams/pharmacy/questions/"
            "generated_required.js"
        )

        export_name = (
            "generatedRequiredQuestions"
        )
    else:
        raise ValueError(
            "現在は pharmacy / required "
            "のみ対応しています"
        )

    write_generated_questions_js(
        questions=[
            study_quest_question
        ],
        output_path=output_path,
        export_name=export_name,
    )

    print()
    print("類題生成完了")
    print(
        f"question_id: {question_id}"
    )
    print(
        f"output: {output_path}"
    )


if __name__ == "__main__":
    main()
