from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from tools.question_builder.exam_generation_profiles import (
    validate_generation_request,
)
from tools.question_builder.knowledge.retriever import (
    retrieve,
)
from tools.question_builder.openai_drone_question_generator import (
    generate_drone_questions,
)
from tools.question_builder.prompt_builder import (
    build_rag_question_generation_prompt,
)


QUESTION_FILE_PATTERN = re.compile(
    r"^(?P<section>[a-z0-9_]+)"
    r"_l(?P<level>[1-5])"
    r"_(?P<number>\d{3})\.json$"
)

ALLOWED_FIGURE_TYPES = {
    "none",
    "table",
    "line_chart",
    "bar_chart",
    "flowchart",
}

SECTION_CATEGORY_MAP = {
    "mindset": "RISK",
    "rule": "RULE",
    "system": "SYSTEM",
    "operation": "SYSTEM",
    "risk": "RISK",
}


def build_output_directory(
    section: str,
    difficulty: int,
) -> Path:
    return (
        Path("generated_questions")
        / "drone"
        / "common"
        / section
        / f"level{difficulty}"
    )


def find_existing_numbers(
    output_directory: Path,
    section: str,
    difficulty: int,
) -> list[int]:
    if not output_directory.exists():
        return []

    numbers: list[int] = []

    for path in output_directory.glob("*.json"):
        match = QUESTION_FILE_PATTERN.match(
            path.name
        )

        if match is None:
            continue

        if match.group("section") != section:
            continue

        if int(match.group("level")) != difficulty:
            continue

        numbers.append(
            int(match.group("number"))
        )

    return sorted(numbers)


def build_target_paths(
    section: str,
    difficulty: int,
    count: int,
) -> list[Path]:
    output_directory = build_output_directory(
        section=section,
        difficulty=difficulty,
    )

    output_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    existing_numbers = find_existing_numbers(
        output_directory=output_directory,
        section=section,
        difficulty=difficulty,
    )

    start_number = (
        max(existing_numbers) + 1
        if existing_numbers
        else 1
    )

    return [
        output_directory
        / (
            f"{section}_l{difficulty}_"
            f"{number:03d}.json"
        )
        for number in range(
            start_number,
            start_number + count,
        )
    ]


def validate_generated_question(
    question: dict[str, Any],
    index: int,
) -> None:
    """
    API応答に対する最低限の構造検証。
    本格的な品質検証は既存Validatorへ後で接続する。
    """

    required_string_fields = [
        "question",
        "explanation",
        "figureType",
    ]

    for field in required_string_fields:
        value = question.get(field)

        if not isinstance(value, str):
            raise ValueError(
                f"Question {index}: "
                f"{field} must be a string"
            )

        if field != "figureType" and not value.strip():
            raise ValueError(
                f"Question {index}: "
                f"{field} must not be empty"
            )

    choices = question.get("choices")

    if not isinstance(choices, list):
        raise ValueError(
            f"Question {index}: "
            "choices must be a list"
        )

    if len(choices) != 3:
        raise ValueError(
            f"Question {index}: "
            "choices must contain exactly 3 items"
        )

    if not all(
        isinstance(choice, str)
        and choice.strip()
        for choice in choices
    ):
        raise ValueError(
            f"Question {index}: "
            "every choice must be a non-empty string"
        )

    answer = question.get("answer")

    if not isinstance(answer, int):
        raise ValueError(
            f"Question {index}: "
            "answer must be an integer"
        )

    if answer not in range(3):
        raise ValueError(
            f"Question {index}: "
            "answer must be between 0 and 2"
        )

    figure_type = question.get(
        "figureType"
    )

    if figure_type not in ALLOWED_FIGURE_TYPES:
        raise ValueError(
            f"Question {index}: "
            f"unsupported figureType={figure_type}"
        )

    figure_data = question.get(
        "figureData"
    )

    if not isinstance(figure_data, dict):
        raise ValueError(
            f"Question {index}: "
            "figureData must be an object"
        )


def build_saved_question(
    *,
    raw_question: dict[str, Any],
    target_path: Path,
    section: str,
    difficulty: int,
    knowledge_items: list[dict[str, Any]],
    keywords: list[str],
) -> dict[str, Any]:
    """
    AIが生成した本文へPython側でmetadataを付与する。
    """

    knowledge_ids = [
        str(item["id"])
        for item in knowledge_items
    ]

    source_pages = sorted(
        {
            int(page)
            for item in knowledge_items
            for page in item.get("pages", [])
            if isinstance(page, int)
        }
    )

    return {
        "id": target_path.stem,
        "exam": "drone",
        "category": SECTION_CATEGORY_MAP[section],
        "section": section,
        "difficulty": difficulty,
        "tags": list(dict.fromkeys(keywords)),
        "question": raw_question["question"].strip(),
        "choices": [
            choice.strip()
            for choice in raw_question["choices"]
        ],
        "answer": raw_question["answer"],
        "explanation": (
            raw_question["explanation"].strip()
        ),
        "figureType": raw_question["figureType"],
        "figureData": raw_question["figureData"],
        "source": {
            "type": "rag_knowledge",
            "manual": (
                "無人航空機の飛行の安全に関する教則 第5版"
            ),
            "knowledgeIds": knowledge_ids,
            "pages": source_pages,
            "keywords": keywords,
        },
    }


def save_questions(
    *,
    questions: list[dict[str, Any]],
    target_paths: list[Path],
    section: str,
    difficulty: int,
    knowledge_items: list[dict[str, Any]],
    keywords: list[str],
) -> list[Path]:
    if len(questions) != len(target_paths):
        raise ValueError(
            "Question count and target path count "
            "do not match"
        )

    saved_paths: list[Path] = []

    for index, (
        raw_question,
        target_path,
    ) in enumerate(
        zip(questions, target_paths),
        start=1,
    ):
        validate_generated_question(
            question=raw_question,
            index=index,
        )

        saved_question = build_saved_question(
            raw_question=raw_question,
            target_path=target_path,
            section=section,
            difficulty=difficulty,
            knowledge_items=knowledge_items,
            keywords=keywords,
        )

        target_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        target_path.write_text(
            json.dumps(
                saved_question,
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

        saved_paths.append(target_path)

    return saved_paths


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "二等無人航空機操縦士試験の"
            "RAG問題生成CLI"
        )
    )

    parser.add_argument(
        "--section",
        required=True,
        help=(
            "生成分野。例: rule, system, "
            "operation, risk"
        ),
    )

    parser.add_argument(
        "--difficulty",
        type=int,
        required=True,
        help="難易度1〜5",
    )

    parser.add_argument(
        "--count",
        type=int,
        default=10,
        help="生成問題数1〜50",
    )

    parser.add_argument(
        "--keywords",
        nargs="+",
        required=True,
        help=(
            "Knowledge検索キーワード。"
            "例: --keywords 登録 カテゴリー"
        ),
    )

    parser.add_argument(
        "--max-knowledge",
        type=int,
        default=5,
        help="GPTへ渡すKnowledgeの最大件数",
    )

    parser.add_argument(
        "--allow-api",
        action="store_true",
        help="OpenAI API呼び出しを許可する",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help=(
            "APIを呼ばず、検索結果と"
            "プロンプトだけ確認する"
        ),
    )

    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="OpenAI応答キャッシュを使用しない",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_arguments()

    request = validate_generation_request(
        exam="drone",
        section=args.section,
        difficulty=args.difficulty,
        count=args.count,
    )

    section = request["section"]
    difficulty = request["difficulty"]
    count = request["count"]
    profile = request["profile"]

    keywords = [
        keyword.strip()
        for keyword in args.keywords
        if keyword.strip()
    ]

    if not keywords:
        raise ValueError(
            "At least one keyword is required"
        )

    if args.max_knowledge <= 0:
        raise ValueError(
            "--max-knowledge must be greater than zero"
        )

    knowledge_items = retrieve(
        exam="drone",
        section=section,
        keywords=keywords,
        max_items=args.max_knowledge,
        include_score=True,
    )

    if not knowledge_items:
        raise RuntimeError(
            "条件に一致するKnowledgeがありません。"
            "sectionまたはkeywordsを確認してください。"
        )

    target_paths = build_target_paths(
        section=section,
        difficulty=difficulty,
        count=count,
    )

    prompt = build_rag_question_generation_prompt(
        section=section,
        section_display_name=(
            profile["sections"][section]
        ),
        difficulty=difficulty,
        count=count,
        keywords=keywords,
        knowledge_items=knowledge_items,
    )

    print()
    print("DRONE RAG QUESTION GENERATOR")
    print("----------------------------")
    print(f"section      : {section}")
    print(
        "sectionName  : "
        f"{profile['sections'][section]}"
    )
    print(f"difficulty   : {difficulty}")
    print(f"count        : {count}")
    print(
        "keywords     : "
        f"{', '.join(keywords)}"
    )
    print(
        "knowledge    : "
        f"{len(knowledge_items)}"
    )
    print(
        "outputDir    : "
        f"{target_paths[0].parent}"
    )

    print()
    print("retrieved knowledge:")

    for item in knowledge_items:
        retrieval = item.get(
            "_retrieval",
            {}
        )

        print(
            "  "
            f"{item['id']} "
            f"score={retrieval.get('score')} "
            f"title={item['title']}"
        )

    print()
    print("target files:")

    for path in target_paths:
        print(f"  {path.name}")

    if args.dry_run:
        print()
        print("PROMPT")
        print("----------------------------")
        print(prompt)
        return

    questions = generate_drone_questions(
        prompt=prompt,
        expected_count=count,
        allow_api=args.allow_api,
        use_cache=not args.no_cache,
    )

    saved_paths = save_questions(
        questions=questions,
        target_paths=target_paths,
        section=section,
        difficulty=difficulty,
        knowledge_items=knowledge_items,
        keywords=keywords,
    )

    print()
    print("GENERATED QUESTIONS")
    print("----------------------------")

    for path in saved_paths:
        print(f"[SAVED] {path}")

    print()
    print(
        f"Completed: {len(saved_paths)} questions"
    )


if __name__ == "__main__":
    main()
