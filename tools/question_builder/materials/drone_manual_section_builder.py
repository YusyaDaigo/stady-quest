from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


DEFAULT_PAGES_DIR = Path(
    "generated_materials/drone/manual/pages"
)

DEFAULT_OUTPUT_DIR = Path(
    "generated_materials/drone/manual/sections"
)

SECTION_DEFINITIONS: dict[str, dict[str, Any]] = {
    "mindset": {
        "chapter": 2,
        "title": "無人航空機操縦者の心得",
        "startPage": 8,
        "endPage": 12,
    },
    "rule": {
        "chapter": 3,
        "title": "無人航空機に関する規則",
        "startPage": 13,
        "endPage": 39,
    },
    "system": {
        "chapter": 4,
        "title": "無人航空機のシステム",
        "startPage": 40,
        "endPage": 57,
    },
    "operation": {
        "chapter": 5,
        "title": "無人航空機の操縦者及び運航体制",
        "startPage": 58,
        "endPage": 68,
    },
    "risk": {
        "chapter": 6,
        "title": "運航上のリスク管理",
        "startPage": 69,
        "endPage": 87,
    },
}


def load_page_text(
    pages_dir: Path,
    page_number: int,
) -> str:
    page_path = (
        pages_dir
        / f"page_{page_number:03d}.txt"
    )

    if not page_path.exists():
        raise FileNotFoundError(
            f"Page file not found: {page_path}"
        )

    return page_path.read_text(
        encoding="utf-8"
    ).strip()


def load_page_range(
    pages_dir: Path,
    start_page: int,
    end_page: int,
) -> str:
    blocks: list[str] = []

    for page_number in range(
        start_page,
        end_page + 1,
    ):
        text = load_page_text(
            pages_dir=pages_dir,
            page_number=page_number,
        )

        blocks.append(
            "\n".join(
                [
                    (
                        f"===== PDF PAGE "
                        f"{page_number} ====="
                    ),
                    text,
                ]
            )
        )

    return "\n\n".join(blocks)


def split_text_into_chunks(
    text: str,
    max_characters: int = 5000,
    overlap_characters: int = 300,
) -> list[str]:
    if max_characters <= 0:
        raise ValueError(
            "max_characters must be positive"
        )

    if overlap_characters < 0:
        raise ValueError(
            "overlap_characters cannot be negative"
        )

    if overlap_characters >= max_characters:
        raise ValueError(
            "overlap_characters must be smaller "
            "than max_characters"
        )

    paragraphs = [
        paragraph.strip()
        for paragraph in text.split("\n\n")
        if paragraph.strip()
    ]

    chunks: list[str] = []
    current_parts: list[str] = []
    current_length = 0

    for paragraph in paragraphs:
        paragraph_length = len(paragraph)

        if (
            current_parts
            and current_length
            + paragraph_length
            + 2
            > max_characters
        ):
            chunk = "\n\n".join(
                current_parts
            ).strip()

            chunks.append(chunk)

            overlap_text = (
                chunk[-overlap_characters:]
                if overlap_characters
                else ""
            )

            current_parts = (
                [overlap_text]
                if overlap_text
                else []
            )

            current_length = len(
                overlap_text
            )

        current_parts.append(
            paragraph
        )

        current_length += (
            paragraph_length + 2
        )

    if current_parts:
        chunk = "\n\n".join(
            current_parts
        ).strip()

        if chunk:
            chunks.append(chunk)

    return chunks


def build_sections(
    pages_dir: Path,
    output_dir: Path,
    max_characters: int,
    overlap_characters: int,
) -> dict[str, Any]:
    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    manifest_sections: dict[str, Any] = {}

    for section_name, definition in (
        SECTION_DEFINITIONS.items()
    ):
        section_dir = (
            output_dir
            / section_name
        )

        chunks_dir = (
            section_dir
            / "chunks"
        )

        chunks_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        section_text = load_page_range(
            pages_dir=pages_dir,
            start_page=definition["startPage"],
            end_page=definition["endPage"],
        )

        section_text_path = (
            section_dir
            / "section.txt"
        )

        section_text_path.write_text(
            section_text,
            encoding="utf-8",
        )

        chunks = split_text_into_chunks(
            text=section_text,
            max_characters=max_characters,
            overlap_characters=(
                overlap_characters
            ),
        )

        chunk_entries: list[dict[str, Any]] = []

        for index, chunk in enumerate(
            chunks,
            start=1,
        ):
            chunk_filename = (
                f"chunk_{index:03d}.txt"
            )

            chunk_path = (
                chunks_dir
                / chunk_filename
            )

            chunk_path.write_text(
                chunk,
                encoding="utf-8",
            )

            chunk_entries.append(
                {
                    "index": index,
                    "file": str(chunk_path),
                    "characterCount": len(chunk),
                }
            )

        manifest_sections[section_name] = {
            **definition,
            "sectionFile": str(
                section_text_path
            ),
            "characterCount": len(
                section_text
            ),
            "chunkCount": len(
                chunks
            ),
            "chunks": chunk_entries,
        }

    manifest = {
        "exam": "drone",
        "edition": 5,
        "chunkSettings": {
            "maxCharacters": max_characters,
            "overlapCharacters": (
                overlap_characters
            ),
        },
        "sections": manifest_sections,
    }

    manifest_path = (
        output_dir
        / "sections.json"
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
            "Build section-level and chunk-level "
            "text files from the drone manual."
        )
    )

    parser.add_argument(
        "--pages-dir",
        default=str(
            DEFAULT_PAGES_DIR
        ),
    )

    parser.add_argument(
        "--output-dir",
        default=str(
            DEFAULT_OUTPUT_DIR
        ),
    )

    parser.add_argument(
        "--chunk-size",
        type=int,
        default=5000,
    )

    parser.add_argument(
        "--overlap",
        type=int,
        default=300,
    )

    args = parser.parse_args()

    manifest = build_sections(
        pages_dir=Path(
            args.pages_dir
        ),
        output_dir=Path(
            args.output_dir
        ),
        max_characters=(
            args.chunk_size
        ),
        overlap_characters=(
            args.overlap
        ),
    )

    print(
        "==================================="
    )
    print(
        "DRONE MANUAL SECTION BUILDER"
    )
    print(
        "==================================="
    )

    for section_name, data in (
        manifest["sections"].items()
    ):
        print(
            f"{section_name:<10} "
            f"pages={data['startPage']:02d}"
            f"-{data['endPage']:02d} "
            f"chars={data['characterCount']:>6} "
            f"chunks={data['chunkCount']}"
        )


if __name__ == "__main__":
    main()
