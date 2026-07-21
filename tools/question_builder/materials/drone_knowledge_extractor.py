from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


DEFAULT_SECTIONS_DIR = Path(
    "generated_materials/drone/manual/sections"
)

DEFAULT_OUTPUT_DIR = Path(
    "generated_materials/drone/knowledge"
)

SECTION_NAMES = (
    "mindset",
    "rule",
    "system",
    "operation",
    "risk",
)

PAGE_MARKER_PATTERN = re.compile(
    r"^===== PDF PAGE (\d+) =====$"
)

HEADING_PATTERNS = (
    # 3.1 航空法全般
    re.compile(
        r"^\d+\.\d+(?:\.\d+)*\s+\S+"
    ),

    # （1）航空法における無人航空機の定義
    re.compile(
        r"^（\d+）\s*\S+"
    ),

    # 1）無人航空機の登録
    re.compile(
        r"^\d+）\s*\S+"
    ),

    # a. 規制対象となる飛行の空域
    re.compile(
        r"^[a-zA-Z]\.\s*\S+"
    ),
)

KEYWORD_STOP_WORDS = {
    "する",
    "ある",
    "いる",
    "こと",
    "もの",
    "ため",
    "場合",
    "これ",
    "それ",
    "及び",
    "また",
    "なお",
    "より",
    "又は",
    "として",
    "について",
    "において",
    "無人航空機",
    "飛行",
    "操縦者",
    "必要",
    "以下",
    "当該",
    "できる",
    "行う",
    "いう",
    "なる",
    "ない",
    "れる",
    "られる",
}


def normalize_line(line: str) -> str:
    line = line.replace("\u3000", " ")
    line = re.sub(r"[ \t]+", " ", line)
    return line.strip()


def is_heading(line: str) -> bool:
    if not line:
        return False

    return any(
        pattern.match(line)
        for pattern in HEADING_PATTERNS
    )


def clean_title(line: str) -> str:
    title = normalize_line(line)

    title = re.sub(
        r"^\d+\.\d+(?:\.\d+)*\s*",
        "",
        title,
    )

    title = re.sub(
        r"^（\d+）\s*",
        "",
        title,
    )

    title = re.sub(
        r"^\d+）\s*",
        "",
        title,
    )

    title = re.sub(
        r"^[a-zA-Z]\.\s*",
        "",
        title,
    )

    return title.strip() or line.strip()


def extract_terms(text: str) -> list[str]:
    candidates = re.findall(
        r"[一-龥々ヶァ-ヶーA-Za-z0-9]{2,}",
        text,
    )

    cleaned: list[str] = []

    for candidate in candidates:
        candidate = candidate.strip()

        if candidate in KEYWORD_STOP_WORDS:
            continue

        if candidate.isdigit():
            continue

        if len(candidate) > 30:
            continue

        cleaned.append(candidate)

    counts = Counter(cleaned)

    ranked = sorted(
        counts.items(),
        key=lambda item: (
            -item[1],
            -len(item[0]),
            item[0],
        ),
    )

    return [
        word
        for word, _ in ranked[:8]
    ]


def make_content_hash(text: str) -> str:
    normalized = re.sub(
        r"\s+",
        "",
        text,
    )

    return hashlib.sha256(
        normalized.encode("utf-8")
    ).hexdigest()[:16]


def split_raw_units(
    section_text: str,
) -> list[dict[str, Any]]:
    units: list[dict[str, Any]] = []

    current_page: int | None = None
    current_title = ""
    current_lines: list[str] = []
    current_pages: set[int] = set()

    def flush() -> None:
        nonlocal current_title
        nonlocal current_lines
        nonlocal current_pages

        text = "\n".join(
            current_lines
        ).strip()

        if text:
            units.append(
                {
                    "title": (
                        current_title
                        or text.splitlines()[0][:80]
                    ),
                    "text": text,
                    "pages": sorted(
                        current_pages
                    ),
                }
            )

        current_title = ""
        current_lines = []
        current_pages = set()

    for raw_line in section_text.splitlines():
        line = normalize_line(raw_line)

        page_match = PAGE_MARKER_PATTERN.match(
            line
        )

        if page_match:
            current_page = int(
                page_match.group(1)
            )

            if current_lines:
                current_pages.add(
                    current_page
                )

            continue

        if not line:
            if current_lines:
                current_lines.append("")
            continue

        if is_heading(line):
            flush()
            current_title = clean_title(line)
            current_lines = [line]

            if current_page is not None:
                current_pages.add(
                    current_page
                )

            continue

        if not current_lines:
            current_title = line[:80]

        current_lines.append(line)

        if current_page is not None:
            current_pages.add(
                current_page
            )

    flush()

    return units


def merge_small_units(
    units: list[dict[str, Any]],
    min_characters: int,
) -> list[dict[str, Any]]:
    merged: list[dict[str, Any]] = []

    for unit in units:
        if (
            merged
            and len(unit["text"]) < min_characters
        ):
            previous = merged[-1]

            previous["text"] = (
                previous["text"].rstrip()
                + "\n\n"
                + unit["text"].lstrip()
            )

            previous["pages"] = sorted(
                set(previous["pages"])
                | set(unit["pages"])
            )

            if (
                unit["title"]
                and unit["title"]
                not in previous["title"]
            ):
                previous["subtitles"].append(
                    unit["title"]
                )

            continue

        merged.append(
            {
                **unit,
                "subtitles": [],
            }
        )

    return merged


def split_large_text(
    unit: dict[str, Any],
    max_characters: int,
) -> list[dict[str, Any]]:
    text = unit["text"]

    if len(text) <= max_characters:
        return [unit]

    paragraphs = [
        paragraph.strip()
        for paragraph in re.split(
            r"\n\s*\n",
            text,
        )
        if paragraph.strip()
    ]

    if len(paragraphs) <= 1:
        paragraphs = [
            text[index:index + max_characters]
            for index in range(
                0,
                len(text),
                max_characters,
            )
        ]

    results: list[dict[str, Any]] = []
    current: list[str] = []
    current_length = 0

    for paragraph in paragraphs:
        paragraph_length = len(paragraph)

        if (
            current
            and current_length
            + paragraph_length
            + 2
            > max_characters
        ):
            results.append(
                {
                    **unit,
                    "text": "\n\n".join(
                        current
                    ).strip(),
                }
            )

            current = []
            current_length = 0

        current.append(paragraph)
        current_length += (
            paragraph_length + 2
        )

    if current:
        results.append(
            {
                **unit,
                "text": "\n\n".join(
                    current
                ).strip(),
            }
        )

    total = len(results)

    for index, result in enumerate(
        results,
        start=1,
    ):
        if total > 1:
            result["title"] = (
                f"{unit['title']} "
                f"({index}/{total})"
            )

    return results


def finalize_units(
    section: str,
    units: list[dict[str, Any]],
    max_characters: int,
) -> list[dict[str, Any]]:
    expanded: list[dict[str, Any]] = []

    for unit in units:
        expanded.extend(
            split_large_text(
                unit=unit,
                max_characters=max_characters,
            )
        )

    knowledge_items: list[dict[str, Any]] = []

    for index, unit in enumerate(
        expanded,
        start=1,
    ):
        text = unit["text"].strip()
        pages = unit["pages"]

        knowledge_items.append(
            {
                "id": f"{section}_{index:04d}",
                "section": section,
                "title": unit["title"],
                "subtitles": unit.get(
                    "subtitles",
                    [],
                ),
                "pages": pages,
                "startPage": (
                    min(pages)
                    if pages
                    else None
                ),
                "endPage": (
                    max(pages)
                    if pages
                    else None
                ),
                "keywords": extract_terms(
                    unit["title"]
                    + "\n"
                    + text
                ),
                "text": text,
                "characterCount": len(text),
                "contentHash": make_content_hash(
                    text
                ),
            }
        )

    return knowledge_items


def build_knowledge_database(
    sections_dir: Path,
    output_dir: Path,
    min_characters: int,
    max_characters: int,
) -> dict[str, Any]:
    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    all_items: list[dict[str, Any]] = []
    section_summary: dict[str, Any] = {}

    for section in SECTION_NAMES:
        section_file = (
            sections_dir
            / section
            / "section.txt"
        )

        if not section_file.exists():
            raise FileNotFoundError(
                f"Section file not found: "
                f"{section_file}"
            )

        section_text = section_file.read_text(
            encoding="utf-8"
        )

        raw_units = split_raw_units(
            section_text
        )

        merged_units = merge_small_units(
            units=raw_units,
            min_characters=min_characters,
        )

        knowledge_items = finalize_units(
            section=section,
            units=merged_units,
            max_characters=max_characters,
        )

        section_output = (
            output_dir
            / f"{section}.json"
        )

        section_output.write_text(
            json.dumps(
                knowledge_items,
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )

        all_items.extend(
            knowledge_items
        )

        section_summary[section] = {
            "itemCount": len(
                knowledge_items
            ),
            "characterCount": sum(
                item["characterCount"]
                for item in knowledge_items
            ),
            "outputFile": str(
                section_output
            ),
        }

    combined_output = (
        output_dir
        / "knowledge.json"
    )

    combined_output.write_text(
        json.dumps(
            all_items,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    manifest = {
        "exam": "drone",
        "edition": 5,
        "settings": {
            "minCharacters": min_characters,
            "maxCharacters": max_characters,
        },
        "totalItems": len(all_items),
        "totalCharacters": sum(
            item["characterCount"]
            for item in all_items
        ),
        "sections": section_summary,
        "knowledgeFile": str(
            combined_output
        ),
    }

    manifest_path = (
        output_dir
        / "manifest.json"
    )

    manifest_path.write_text(
        json.dumps(
            manifest,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Extract structured knowledge units "
            "from the drone manual sections."
        )
    )

    parser.add_argument(
        "--sections-dir",
        default=str(
            DEFAULT_SECTIONS_DIR
        ),
    )

    parser.add_argument(
        "--output-dir",
        default=str(
            DEFAULT_OUTPUT_DIR
        ),
    )

    parser.add_argument(
        "--min-characters",
        type=int,
        default=250,
    )

    parser.add_argument(
        "--max-characters",
        type=int,
        default=2200,
    )

    args = parser.parse_args()

    if args.min_characters <= 0:
        raise ValueError(
            "--min-characters must be positive"
        )

    if (
        args.max_characters
        <= args.min_characters
    ):
        raise ValueError(
            "--max-characters must be greater "
            "than --min-characters"
        )

    manifest = build_knowledge_database(
        sections_dir=Path(
            args.sections_dir
        ),
        output_dir=Path(
            args.output_dir
        ),
        min_characters=(
            args.min_characters
        ),
        max_characters=(
            args.max_characters
        ),
    )

    print(
        "==================================="
    )
    print(
        "DRONE KNOWLEDGE EXTRACTOR"
    )
    print(
        "==================================="
    )

    for section, data in (
        manifest["sections"].items()
    ):
        print(
            f"{section:<10} "
            f"items={data['itemCount']:>3} "
            f"chars={data['characterCount']:>6}"
        )

    print(
        "-----------------------------------"
    )
    print(
        f"Total items : "
        f"{manifest['totalItems']}"
    )
    print(
        f"Characters  : "
        f"{manifest['totalCharacters']}"
    )
    print(
        f"Output      : "
        f"{manifest['knowledgeFile']}"
    )


if __name__ == "__main__":
    main()
