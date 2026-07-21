from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from .loader import (
    build_knowledge_map,
    get_knowledge_directory,
    load_knowledge,
)


DEFAULT_MAX_ITEMS = 5
DEFAULT_MIN_CHARACTERS = 80


@dataclass(frozen=True)
class RetrievalScore:
    """
    Internal score details for one Knowledge item.
    """

    total: int
    section_score: int
    keyword_score: int
    title_score: int
    text_score: int
    matched_keywords: tuple[str, ...]


def normalize_query(value: str) -> str:
    """
    Normalize user input and indexed values.

    Japanese has no case distinction, but lower() is useful
    for English words and abbreviations.
    """
    return " ".join(
        str(value).strip().lower().split()
    )


def normalize_keywords(
    keywords: Iterable[str] | None,
) -> list[str]:
    """
    Normalize keywords while preserving their input order.
    """
    if not keywords:
        return []

    normalized: list[str] = []
    seen: set[str] = set()

    for value in keywords:
        keyword = normalize_query(value)

        if not keyword:
            continue

        if keyword in seen:
            continue

        seen.add(keyword)
        normalized.append(keyword)

    return normalized


def load_json_index(
    path: Path,
) -> dict[str, list[str]]:
    """
    Load an index JSON file.

    Missing index files are treated as empty indexes so that
    text search can still work.
    """
    if not path.exists():
        return {}

    try:
        data = json.loads(
            path.read_text(encoding="utf-8")
        )
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Invalid index JSON: {path}"
        ) from exc

    if not isinstance(data, dict):
        raise ValueError(
            f"Index must contain a JSON object: {path}"
        )

    result: dict[str, list[str]] = {}

    for raw_key, raw_ids in data.items():
        if not isinstance(raw_ids, list):
            continue

        key = normalize_query(raw_key)

        if not key:
            continue

        result[key] = [
            str(knowledge_id)
            for knowledge_id in raw_ids
        ]

    return result


def load_indexes(
    exam: str,
) -> dict[str, dict[str, list[str]]]:
    """
    Load all indexes used by the Retriever.
    """
    knowledge_directory = get_knowledge_directory(exam)

    return {
        "keyword": load_json_index(
            knowledge_directory / "keyword_index.json"
        ),
        "section": load_json_index(
            knowledge_directory / "section_index.json"
        ),
        "title": load_json_index(
            knowledge_directory / "title_index.json"
        ),
    }


def is_usable_knowledge(
    item: dict[str, Any],
    min_characters: int,
) -> bool:
    """
    Exclude empty or heading-only Knowledge items.

    The minimum length is intentionally enforced here rather
    than permanently deleting data from knowledge.json.
    """
    text = str(
        item.get("text", "")
    ).strip()

    if not text:
        return False

    character_count = item.get(
        "characterCount",
        len(text),
    )

    try:
        character_count = int(character_count)
    except (TypeError, ValueError):
        character_count = len(text)

    if character_count < min_characters:
        return False

    non_empty_lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if len(non_empty_lines) <= 1:
        return False

    return True


def get_exact_keyword_ids(
    keyword: str,
    keyword_index: dict[str, list[str]],
) -> set[str]:
    """
    Return Knowledge IDs for an exact keyword-index match.
    """
    return set(
        keyword_index.get(keyword, [])
    )


def get_partial_title_ids(
    keyword: str,
    title_index: dict[str, list[str]],
) -> set[str]:
    """
    Return IDs whose indexed title contains the keyword.
    """
    matches: set[str] = set()

    for title, knowledge_ids in title_index.items():
        if keyword in title:
            matches.update(knowledge_ids)

    return matches


def score_item(
    item: dict[str, Any],
    requested_section: str | None,
    keywords: list[str],
    exact_keyword_ids: dict[str, set[str]],
    partial_title_ids: dict[str, set[str]],
) -> RetrievalScore:
    """
    Score one Knowledge item.

    Score weights:
        section match          +5
        exact keyword index   +10 per keyword
        keyword in title       +6 per keyword
        title-index match      +3 per keyword
        keyword in text        +1 per keyword
    """
    knowledge_id = str(item["id"])
    item_section = normalize_query(
        item.get("section", "")
    )
    title = normalize_query(
        item.get("title", "")
    )
    text = normalize_query(
        item.get("text", "")
    )

    section_score = 0
    keyword_score = 0
    title_score = 0
    text_score = 0
    matched_keywords: list[str] = []

    if (
        requested_section
        and item_section == requested_section
    ):
        section_score = 5

    for keyword in keywords:
        matched = False

        if knowledge_id in exact_keyword_ids[keyword]:
            keyword_score += 10
            matched = True

        if keyword in title:
            title_score += 6
            matched = True
        elif knowledge_id in partial_title_ids[keyword]:
            title_score += 3
            matched = True

        if keyword in text:
            text_score += 1
            matched = True

        if matched:
            matched_keywords.append(keyword)

    total = (
        section_score
        + keyword_score
        + title_score
        + text_score
    )

    return RetrievalScore(
        total=total,
        section_score=section_score,
        keyword_score=keyword_score,
        title_score=title_score,
        text_score=text_score,
        matched_keywords=tuple(
            matched_keywords
        ),
    )


def retrieve(
    exam: str,
    section: str | None = None,
    keywords: Iterable[str] | None = None,
    max_items: int = DEFAULT_MAX_ITEMS,
    min_characters: int = DEFAULT_MIN_CHARACTERS,
    include_score: bool = False,
) -> list[dict[str, Any]]:
    """
    Retrieve the most relevant Knowledge items.

    Args:
        exam:
            Exam key, such as "drone".

        section:
            Optional section filter, such as "rule".

        keywords:
            Search terms.

        max_items:
            Maximum number of returned Knowledge items.

        min_characters:
            Exclude items shorter than this value.

        include_score:
            Include `_retrieval` debugging information in
            returned dictionaries.

    Returns:
        Ranked Knowledge dictionaries.
    """
    normalized_exam = normalize_query(exam)

    if not normalized_exam:
        raise ValueError("exam must not be empty")

    normalized_section = (
        normalize_query(section)
        if section
        else None
    )

    normalized_keywords = normalize_keywords(
        keywords
    )

    if max_items <= 0:
        raise ValueError(
            "max_items must be greater than zero"
        )

    if min_characters < 0:
        raise ValueError(
            "min_characters must not be negative"
        )

    knowledge_items = load_knowledge(
        normalized_exam
    )
    knowledge_map = build_knowledge_map(
        knowledge_items
    )
    indexes = load_indexes(
        normalized_exam
    )

    section_index = indexes["section"]
    keyword_index = indexes["keyword"]
    title_index = indexes["title"]

    candidate_ids: set[str]

    if normalized_section:
        candidate_ids = set(
            section_index.get(
                normalized_section,
                [],
            )
        )
    else:
        candidate_ids = set(
            knowledge_map.keys()
        )

    # When section_index is unavailable or stale, fall back
    # to direct section comparison.
    if normalized_section and not candidate_ids:
        candidate_ids = {
            knowledge_id
            for knowledge_id, item
            in knowledge_map.items()
            if normalize_query(
                item.get("section", "")
            ) == normalized_section
        }

    exact_keyword_ids = {
        keyword: get_exact_keyword_ids(
            keyword=keyword,
            keyword_index=keyword_index,
        )
        for keyword in normalized_keywords
    }

    partial_title_ids = {
        keyword: get_partial_title_ids(
            keyword=keyword,
            title_index=title_index,
        )
        for keyword in normalized_keywords
    }

    ranked: list[
        tuple[
            RetrievalScore,
            dict[str, Any],
        ]
    ] = []

    for knowledge_id in candidate_ids:
        item = knowledge_map.get(
            knowledge_id
        )

        if item is None:
            continue

        if not is_usable_knowledge(
            item=item,
            min_characters=min_characters,
        ):
            continue

        score = score_item(
            item=item,
            requested_section=normalized_section,
            keywords=normalized_keywords,
            exact_keyword_ids=exact_keyword_ids,
            partial_title_ids=partial_title_ids,
        )

        # With keywords supplied, unrelated items should not
        # appear merely because their section matched.
        if (
            normalized_keywords
            and not score.matched_keywords
        ):
            continue

        ranked.append(
            (
                score,
                item,
            )
        )

    ranked.sort(
        key=lambda result: (
            -result[0].total,
            -len(result[0].matched_keywords),
            int(
                result[1].get(
                    "characterCount",
                    len(
                        str(
                            result[1].get(
                                "text",
                                "",
                            )
                        )
                    ),
                )
            ),
            str(result[1]["id"]),
        )
    )

    results: list[dict[str, Any]] = []

    for score, item in ranked[:max_items]:
        result = dict(item)

        if include_score:
            result["_retrieval"] = {
                "score": score.total,
                "sectionScore": (
                    score.section_score
                ),
                "keywordScore": (
                    score.keyword_score
                ),
                "titleScore": (
                    score.title_score
                ),
                "textScore": (
                    score.text_score
                ),
                "matchedKeywords": list(
                    score.matched_keywords
                ),
            }

        results.append(result)

    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Retrieve relevant Knowledge items "
            "for question generation."
        )
    )

    parser.add_argument(
        "--exam",
        required=True,
        help="Exam key such as drone",
    )

    parser.add_argument(
        "--section",
        help="Optional section such as rule",
    )

    parser.add_argument(
        "--keywords",
        nargs="*",
        default=[],
        help=(
            "Search keywords separated by spaces"
        ),
    )

    parser.add_argument(
        "--max-items",
        type=int,
        default=DEFAULT_MAX_ITEMS,
        help="Maximum number of results",
    )

    parser.add_argument(
        "--min-characters",
        type=int,
        default=DEFAULT_MIN_CHARACTERS,
        help=(
            "Exclude Knowledge items shorter "
            "than this value"
        ),
    )

    parser.add_argument(
        "--show-text",
        action="store_true",
        help="Print full Knowledge text",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    results = retrieve(
        exam=args.exam,
        section=args.section,
        keywords=args.keywords,
        max_items=args.max_items,
        min_characters=args.min_characters,
        include_score=True,
    )

    print("=" * 60)
    print("KNOWLEDGE RETRIEVER")
    print("=" * 60)
    print(f"Exam       : {args.exam}")
    print(f"Section    : {args.section or 'ALL'}")
    print(
        "Keywords   : "
        f"{', '.join(args.keywords) or 'NONE'}"
    )
    print(f"Results    : {len(results)}")
    print("=" * 60)

    for index, item in enumerate(
        results,
        start=1,
    ):
        retrieval = item["_retrieval"]

        print(
            f"\n[{index}] {item['id']}"
        )
        print(
            f"Title      : {item['title']}"
        )
        print(
            f"Section    : {item['section']}"
        )
        print(
            f"Pages      : {item['pages']}"
        )
        print(
            f"Characters : "
            f"{item.get('characterCount')}"
        )
        print(
            f"Score      : "
            f"{retrieval['score']}"
        )
        print(
            "Matched    : "
            + ", ".join(
                retrieval["matchedKeywords"]
            )
        )

        if args.show_text:
            print("-" * 60)
            print(item["text"])
        else:
            preview = " ".join(
                str(item["text"]).split()
            )[:180]

            print(
                f"Preview    : {preview}"
            )

    if not results:
        print(
            "\nNo matching Knowledge items found."
        )


if __name__ == "__main__":
    main()
