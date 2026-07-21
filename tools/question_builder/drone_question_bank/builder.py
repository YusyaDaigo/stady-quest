from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from tools.question_builder.drone_question_bank.validator import (
    load_question_file,
    validate_question,
)


DEFAULT_INPUT = Path("generated_questions/drone")
DEFAULT_OUTPUT = Path(
    "src/exams/drone/questions/droneGeneratedQuestions.js"
)

CATEGORY_MAP = {
    "RISK": "CATEGORIES.RISK",
    "RULE": "CATEGORIES.RULE",
    "SYSTEM": "CATEGORIES.SYSTEM",
    "CALC": "CATEGORIES.CALC",
    "FIRST": "CATEGORIES.FIRST",
}


def collect_json_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target]

    return sorted(
        path
        for path in target.rglob("*.json")
        if "cache" not in path.parts
    )


def load_questions(target: Path) -> list[dict[str, Any]]:
    files = collect_json_files(target)

    if not files:
        raise ValueError(f"No JSON files found: {target}")

    questions: list[dict[str, Any]] = []
    errors: list[str] = []
    seen_ids: dict[str, Path] = {}

    for path in files:
        try:
            loaded = load_question_file(path)
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            errors.append(f"{path}: {exc}")
            continue

        for question in loaded:
            question_errors = validate_question(question, path)
            errors.extend(question_errors)

            question_id = question.get("id")

            if isinstance(question_id, str) and question_id:
                if question_id in seen_ids:
                    errors.append(
                        f"{path}: duplicate id '{question_id}' "
                        f"(first found in {seen_ids[question_id]})"
                    )
                else:
                    seen_ids[question_id] = path

            questions.append(question)

    if errors:
        formatted = "\n".join(
            f"[ERROR] {error}"
            for error in errors
        )
        raise ValueError(
            "Question-bank validation failed:\n"
            f"{formatted}"
        )

    questions.sort(
        key=lambda question: (
            question["difficulty"],
            question["section"],
            question["id"],
        )
    )

    return questions


def js_string(value: str, indent: int = 0) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
    )

    if "\n" not in value:
        return encoded

    padding = " " * indent
    return encoded.replace(
        "\\n",
        f"\\n{padding}",
    )


def js_string_array(
    values: list[str],
    indent: int,
) -> list[str]:
    padding = " " * indent
    lines = ["["]

    for index, value in enumerate(values):
        comma = "," if index < len(values) - 1 else ""
        lines.append(
            f"{padding}  {js_string(value)}{comma}"
        )

    lines.append(f"{padding}]")
    return lines


def build_source_label(
    source: Any,
) -> str:
    if isinstance(source, str):
        return source

    if not isinstance(source, dict):
        raise ValueError(
            "source must be a string or object"
        )

    manual = str(
        source.get("manual", "RAG Knowledge")
    ).strip()

    knowledge_ids = source.get(
        "knowledgeIds",
        [],
    )

    if isinstance(knowledge_ids, list):
        ids = [
            str(item).strip()
            for item in knowledge_ids
            if str(item).strip()
        ]
    else:
        ids = []

    if ids:
        return (
            f"{manual} / Knowledge: "
            + ", ".join(ids)
        )

    return manual


def render_question(
    question: dict[str, Any],
) -> list[str]:
    category = CATEGORY_MAP[question["category"]]
    source_label = build_source_label(
        question["source"]
    )

    lines = [
        "  {",
        f'    id: {js_string(question["id"])},',
        '    subject: "drone",',
        f"    category: {category},",
        f'    difficulty: {question["difficulty"]},',
        f'    section: {js_string(question["section"])},',
        f'    source: {js_string(source_label)},',
        "    tags: [",
    ]

    tags = question["tags"]

    for index, tag in enumerate(tags):
        comma = "," if index < len(tags) - 1 else ""
        lines.append(
            f"      {js_string(tag)}{comma}"
        )

    lines.extend(
        [
            "    ],",
            f'    question: {js_string(question["question"])},',
            "    choices: [",
        ]
    )

    choices = question["choices"]

    for index, choice in enumerate(choices):
        comma = "," if index < len(choices) - 1 else ""
        lines.append(
            f"      {js_string(choice)}{comma}"
        )

    lines.extend(
        [
            "    ],",
            f'    answer: {question["answer"]},',
            f'    explanation: {js_string(question["explanation"])}',
            "  }",
        ]
    )

    return lines


def build_javascript(
    questions: list[dict[str, Any]],
) -> str:
    lines = [
        'import { CATEGORIES } from "./categories";',
        "",
        "// このファイルは自動生成されています。",
        "// JSON原本を修正してBuilderを再実行してください。",
        "",
        "export const generatedDroneQuestions = [",
    ]

    for index, question in enumerate(questions):
        rendered = render_question(question)

        if index < len(questions) - 1:
            rendered[-1] += ","

        lines.extend(rendered)
        lines.append("")

    lines.append("];")
    lines.append("")

    return "\n".join(lines)


def write_output(
    questions: list[dict[str, Any]],
    output_path: Path,
) -> None:
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    javascript = build_javascript(questions)

    output_path.write_text(
        javascript,
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Build Study QUEST drone questions "
            "from JSON question-bank files."
        )
    )
    parser.add_argument(
        "--input",
        default=str(DEFAULT_INPUT),
        help="Input JSON file or directory",
    )
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT),
        help="Output JavaScript file",
    )

    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        raise SystemExit(
            f"Input not found: {input_path}"
        )

    try:
        questions = load_questions(input_path)
        write_output(
            questions,
            output_path,
        )
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc

    print("===================================")
    print("DRONE QUESTION BANK BUILDER")
    print("===================================")
    print(f"Input     : {input_path}")
    print(f"Output    : {output_path}")
    print(f"Questions : {len(questions)}")
    print()
    print("Build completed.")


if __name__ == "__main__":
    main()
