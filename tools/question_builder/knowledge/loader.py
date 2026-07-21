from __future__ import annotations

import json
from pathlib import Path
from typing import Any


DEFAULT_GENERATED_ROOT = Path("generated_materials")


def get_knowledge_directory(
    exam: str,
    generated_root: Path | str = DEFAULT_GENERATED_ROOT,
) -> Path:
    """
    Return the knowledge directory for an exam.

    Example:
        generated_materials/drone/knowledge
    """
    normalized_exam = exam.strip().lower()

    if not normalized_exam:
        raise ValueError("exam must not be empty")

    return Path(generated_root) / normalized_exam / "knowledge"


def get_knowledge_path(
    exam: str,
    generated_root: Path | str = DEFAULT_GENERATED_ROOT,
) -> Path:
    """
    Return the knowledge.json path for an exam.
    """
    return get_knowledge_directory(
        exam=exam,
        generated_root=generated_root,
    ) / "knowledge.json"


def load_knowledge(
    exam: str,
    generated_root: Path | str = DEFAULT_GENERATED_ROOT,
) -> list[dict[str, Any]]:
    """
    Load and validate knowledge items for an exam.
    """
    path = get_knowledge_path(
        exam=exam,
        generated_root=generated_root,
    )

    if not path.exists():
        raise FileNotFoundError(
            f"Knowledge file not found: {path}"
        )

    try:
        raw_data = json.loads(
            path.read_text(encoding="utf-8")
        )
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Invalid JSON in knowledge file: {path}"
        ) from exc

    if not isinstance(raw_data, list):
        raise ValueError(
            f"Knowledge file must contain a list: {path}"
        )

    required_fields = {
        "id",
        "section",
        "title",
        "pages",
        "keywords",
        "text",
    }

    knowledge_items: list[dict[str, Any]] = []

    for index, item in enumerate(raw_data):
        if not isinstance(item, dict):
            raise ValueError(
                f"Knowledge item at index {index} "
                "must be an object"
            )

        missing_fields = required_fields - item.keys()

        if missing_fields:
            raise ValueError(
                f"Knowledge item at index {index} "
                f"is missing fields: {sorted(missing_fields)}"
            )

        if not isinstance(item["id"], str):
            raise ValueError(
                f"Knowledge item at index {index} "
                "has invalid id"
            )

        if not isinstance(item["pages"], list):
            raise ValueError(
                f"Knowledge item {item['id']} "
                "has invalid pages"
            )

        if not isinstance(item["keywords"], list):
            raise ValueError(
                f"Knowledge item {item['id']} "
                "has invalid keywords"
            )

        knowledge_items.append(item)

    return knowledge_items


def build_knowledge_map(
    knowledge_items: list[dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    """
    Build an ID-to-knowledge lookup map.
    """
    knowledge_map: dict[str, dict[str, Any]] = {}

    for item in knowledge_items:
        knowledge_id = item["id"]

        if knowledge_id in knowledge_map:
            raise ValueError(
                f"Duplicate knowledge ID: {knowledge_id}"
            )

        knowledge_map[knowledge_id] = item

    return knowledge_map
