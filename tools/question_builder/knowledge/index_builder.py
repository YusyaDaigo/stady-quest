from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

from .loader import (
    get_knowledge_directory,
    load_knowledge,
)


def normalize_keyword(value: str) -> str:
    """
    Normalize a keyword for index lookup.

    Japanese text is kept as-is except for surrounding
    spaces and repeated whitespace.
    """
    return " ".join(
        str(value).strip().split()
    )


def unique_sorted(values: Iterable[str]) -> list[str]:
    """
    Remove duplicates and return sorted values.
    """
    return sorted(set(values))


def build_keyword_index(
    knowledge_items: list[dict[str, Any]],
) -> dict[str, list[str]]:
    """
    Build:
        keyword -> knowledge IDs
    """
    index: defaultdict[str, list[str]] = defaultdict(list)

    for item in knowledge_items:
        knowledge_id = item["id"]

        raw_keywords = item.get("keywords", [])

        for raw_keyword in raw_keywords:
            keyword = normalize_keyword(raw_keyword)

            if not keyword:
                continue

            index[keyword].append(knowledge_id)

    return {
        keyword: unique_sorted(knowledge_ids)
        for keyword, knowledge_ids in sorted(index.items())
    }


def build_section_index(
    knowledge_items: list[dict[str, Any]],
) -> dict[str, list[str]]:
    """
    Build:
        section -> knowledge IDs
    """
    index: defaultdict[str, list[str]] = defaultdict(list)

    for item in knowledge_items:
        section = str(item["section"]).strip()
        knowledge_id = item["id"]

        if not section:
            continue

        index[section].append(knowledge_id)

    return {
        section: unique_sorted(knowledge_ids)
        for section, knowledge_ids in sorted(index.items())
    }


def build_page_index(
    knowledge_items: list[dict[str, Any]],
) -> dict[str, list[str]]:
    """
    Build:
        PDF page number -> knowledge IDs

    JSON object keys are strings.
    """
    index: defaultdict[str, list[str]] = defaultdict(list)

    for item in knowledge_items:
        knowledge_id = item["id"]

        for raw_page in item.get("pages", []):
            try:
                page = int(raw_page)
            except (TypeError, ValueError):
                continue

            index[str(page)].append(knowledge_id)

    return {
        page: unique_sorted(index[page])
        for page in sorted(
            index,
            key=lambda value: int(value),
        )
    }


def build_title_index(
    knowledge_items: list[dict[str, Any]],
) -> dict[str, list[str]]:
    """
    Build:
        normalized title -> knowledge IDs

    This will later be useful for title-based retrieval.
    """
    index: defaultdict[str, list[str]] = defaultdict(list)

    for item in knowledge_items:
        title = normalize_keyword(item.get("title", ""))
        knowledge_id = item["id"]

        if not title:
            continue

        index[title].append(knowledge_id)

    return {
        title: unique_sorted(knowledge_ids)
        for title, knowledge_ids in sorted(index.items())
    }


def write_json(
    path: Path,
    data: Any,
) -> None:
    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    path.write_text(
        json.dumps(
            data,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def build_indexes(
    exam: str,
    output_directory: Path | None = None,
) -> dict[str, Any]:
    """
    Build and save all local indexes for one exam.
    """
    knowledge_items = load_knowledge(exam)

    if output_directory is None:
        output_directory = get_knowledge_directory(exam)

    keyword_index = build_keyword_index(knowledge_items)
    section_index = build_section_index(knowledge_items)
    page_index = build_page_index(knowledge_items)
    title_index = build_title_index(knowledge_items)

    output_files = {
        "keywordIndex": output_directory / "keyword_index.json",
        "sectionIndex": output_directory / "section_index.json",
        "pageIndex": output_directory / "page_index.json",
        "titleIndex": output_directory / "title_index.json",
    }

    write_json(
        output_files["keywordIndex"],
        keyword_index,
    )
    write_json(
        output_files["sectionIndex"],
        section_index,
    )
    write_json(
        output_files["pageIndex"],
        page_index,
    )
    write_json(
        output_files["titleIndex"],
        title_index,
    )

    manifest = {
        "exam": exam,
        "knowledgeItems": len(knowledge_items),
        "indexes": {
            "keywords": {
                "entryCount": len(keyword_index),
                "outputFile": str(
                    output_files["keywordIndex"]
                ),
            },
            "sections": {
                "entryCount": len(section_index),
                "outputFile": str(
                    output_files["sectionIndex"]
                ),
            },
            "pages": {
                "entryCount": len(page_index),
                "outputFile": str(
                    output_files["pageIndex"]
                ),
            },
            "titles": {
                "entryCount": len(title_index),
                "outputFile": str(
                    output_files["titleIndex"]
                ),
            },
        },
    }

    index_manifest_path = (
        output_directory / "index_manifest.json"
    )

    write_json(
        index_manifest_path,
        manifest,
    )

    manifest["manifestFile"] = str(index_manifest_path)

    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build local search indexes from an exam's "
            "knowledge.json file."
        )
    )

    parser.add_argument(
        "--exam",
        required=True,
        help="Exam key such as drone or pharmacy",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    manifest = build_indexes(
        exam=args.exam,
    )

    print("=" * 40)
    print("KNOWLEDGE INDEX BUILDER")
    print("=" * 40)
    print(f"Exam             : {manifest['exam']}")
    print(
        "Knowledge items  : "
        f"{manifest['knowledgeItems']}"
    )

    for name, details in manifest["indexes"].items():
        print(
            f"{name:<17}: "
            f"{details['entryCount']:>4} entries"
        )

    print("-" * 40)
    print(
        "Manifest         : "
        f"{manifest['manifestFile']}"
    )


if __name__ == "__main__":
    main()
