from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


VALID_DIFFICULTIES = {3, 4, 5}
VALID_CATEGORIES = {"RISK", "RULE", "SYSTEM", "CALC", "FIRST"}
VALID_SECTIONS = {"mindset", "rule", "system", "operation", "risk"}


def validate_question(question: dict[str, Any], source_path: Path) -> list[str]:
    errors: list[str] = []

    required_fields = {
        "id",
        "difficulty",
        "section",
        "category",
        "source",
        "tags",
        "question",
        "choices",
        "answer",
        "explanation",
    }

    missing_fields = sorted(required_fields - question.keys())

    if missing_fields:
        errors.append(
            f"{source_path}: missing fields: {', '.join(missing_fields)}"
        )
        return errors

    question_id = question["id"]

    if not isinstance(question_id, str) or not question_id.strip():
        errors.append(f"{source_path}: id must be a non-empty string")

    difficulty = question["difficulty"]

    if difficulty not in VALID_DIFFICULTIES:
        errors.append(
            f"{source_path}: difficulty must be one of "
            f"{sorted(VALID_DIFFICULTIES)}"
        )

    section = question["section"]

    if section not in VALID_SECTIONS:
        errors.append(
            f"{source_path}: invalid section '{section}'"
        )

    category = question["category"]

    if category not in VALID_CATEGORIES:
        errors.append(
            f"{source_path}: invalid category '{category}'"
        )

    source = question["source"]

    if isinstance(source, str):
        if not source.strip():
            errors.append(
                f"{source_path}: source must not be empty"
            )
    elif isinstance(source, dict):
        source_type = source.get("type")
        manual = source.get("manual")
        knowledge_ids = source.get("knowledgeIds")
        pages = source.get("pages")
        keywords = source.get("keywords")

        if (
            not isinstance(source_type, str)
            or not source_type.strip()
        ):
            errors.append(
                f"{source_path}: "
                "source.type must be a non-empty string"
            )

        if (
            not isinstance(manual, str)
            or not manual.strip()
        ):
            errors.append(
                f"{source_path}: "
                "source.manual must be a non-empty string"
            )

        if (
            not isinstance(knowledge_ids, list)
            or not knowledge_ids
            or not all(
                isinstance(item, str)
                and item.strip()
                for item in knowledge_ids
            )
        ):
            errors.append(
                f"{source_path}: "
                "source.knowledgeIds must be a "
                "non-empty list of strings"
            )

        if (
            not isinstance(pages, list)
            or not all(
                isinstance(page, int)
                and page > 0
                for page in pages
            )
        ):
            errors.append(
                f"{source_path}: "
                "source.pages must be a list "
                "of positive integers"
            )

        if (
            not isinstance(keywords, list)
            or not keywords
            or not all(
                isinstance(keyword, str)
                and keyword.strip()
                for keyword in keywords
            )
        ):
            errors.append(
                f"{source_path}: "
                "source.keywords must be a "
                "non-empty list of strings"
            )
    else:
        errors.append(
            f"{source_path}: "
            "source must be a string or object"
        )

    tags = question["tags"]

    if (
        not isinstance(tags, list)
        or not tags
        or not all(
            isinstance(tag, str) and tag.strip()
            for tag in tags
        )
    ):
        errors.append(
            f"{source_path}: tags must be a non-empty list of strings"
        )

    question_text = question["question"]

    if not isinstance(question_text, str) or not question_text.strip():
        errors.append(
            f"{source_path}: question must be a non-empty string"
        )

    choices = question["choices"]

    if not isinstance(choices, list):
        errors.append(
            f"{source_path}: choices must be a list"
        )
    else:
        if len(choices) != 3:
            errors.append(
                f"{source_path}: choices must contain exactly 3 items"
            )

        if not all(
            isinstance(choice, str) and choice.strip()
            for choice in choices
        ):
            errors.append(
                f"{source_path}: every choice must be a non-empty string"
            )
        else:
            normalized_choices = [
                choice.strip()
                for choice in choices
            ]

            if len(set(normalized_choices)) != len(
                normalized_choices
            ):
                errors.append(
                    f"{source_path}: "
                    "choices must not contain duplicates"
                )

    answer = question["answer"]

    if not isinstance(answer, int):
        errors.append(
            f"{source_path}: answer must be an integer"
        )
    elif isinstance(choices, list) and not (
        0 <= answer < len(choices)
    ):
        errors.append(
            f"{source_path}: answer index is outside choices"
        )

    explanation = question["explanation"]

    if (
        not isinstance(explanation, str)
        or not explanation.strip()
    ):
        errors.append(
            f"{source_path}: explanation must be a non-empty string"
        )

    return errors


def load_question_file(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if isinstance(data, dict):
        return [data]

    if isinstance(data, list):
        if not all(isinstance(item, dict) for item in data):
            raise ValueError(
                "JSON array must contain only question objects"
            )

        return data

    raise ValueError(
        "JSON root must be an object or an array of objects"
    )


def collect_json_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target]

    return sorted(
        path
        for path in target.rglob("*.json")
        if "cache" not in path.parts
    )


def validate_target(target: Path) -> int:
    files = collect_json_files(target)

    if not files:
        print(f"No JSON files found: {target}")
        return 1

    all_errors: list[str] = []
    seen_ids: dict[str, Path] = {}
    question_count = 0

    for path in files:
        try:
            questions = load_question_file(path)
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            all_errors.append(f"{path}: {exc}")
            continue

        for question in questions:
            question_count += 1
            all_errors.extend(
                validate_question(question, path)
            )

            question_id = question.get("id")

            if isinstance(question_id, str) and question_id:
                if question_id in seen_ids:
                    all_errors.append(
                        f"{path}: duplicate id '{question_id}' "
                        f"(first found in {seen_ids[question_id]})"
                    )
                else:
                    seen_ids[question_id] = path

    print("===================================")
    print("DRONE QUESTION BANK VALIDATOR")
    print("===================================")
    print(f"Files     : {len(files)}")
    print(f"Questions : {question_count}")
    print(f"Errors    : {len(all_errors)}")

    if all_errors:
        print()
        for error in all_errors:
            print(f"[ERROR] {error}")

        return 1

    print()
    print("Validation passed.")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate Study QUEST drone question-bank JSON files."
    )
    parser.add_argument(
        "target",
        nargs="?",
        default="generated_questions/drone",
        help="JSON file or directory to validate",
    )

    args = parser.parse_args()
    target = Path(args.target)

    if not target.exists():
        raise SystemExit(f"Target not found: {target}")

    raise SystemExit(validate_target(target))


if __name__ == "__main__":
    main()
