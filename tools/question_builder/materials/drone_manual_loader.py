from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from pypdf import PdfReader


DEFAULT_MANUAL_PATH = Path(
    "source_materials/drone/manuals/"
    "drone_manual_5th.pdf"
)

DEFAULT_OUTPUT_DIR = Path(
    "generated_materials/drone/manual"
)


def normalize_page_text(
    text: str,
) -> str:
    """
    PDFから抽出したページ本文を最低限整形する。
    """

    lines = [
        line.rstrip()
        for line in text.replace(
            "\r\n",
            "\n",
        ).replace(
            "\r",
            "\n",
        ).splitlines()
    ]

    normalized_lines: list[str] = []
    previous_blank = False

    for line in lines:
        stripped = line.strip()

        if not stripped:
            if not previous_blank:
                normalized_lines.append("")
            previous_blank = True
            continue

        normalized_lines.append(stripped)
        previous_blank = False

    return "\n".join(
        normalized_lines
    ).strip()


def extract_manual_pages(
    manual_path: Path,
) -> list[dict[str, Any]]:
    """
    教則PDFをページ単位で抽出する。
    """

    if not manual_path.exists():
        raise FileNotFoundError(
            f"Manual not found: {manual_path}"
        )

    reader = PdfReader(
        manual_path
    )

    pages: list[dict[str, Any]] = []

    for index, page in enumerate(
        reader.pages,
        start=1,
    ):
        raw_text = (
            page.extract_text()
            or ""
        )

        text = normalize_page_text(
            raw_text
        )

        pages.append(
            {
                "page": index,
                "text": text,
                "characterCount": len(text),
            }
        )

    return pages


def save_manual_cache(
    pages: list[dict[str, Any]],
    output_dir: Path,
    source_path: Path,
) -> None:
    """
    ページ別テキストとmanifestを保存する。
    """

    pages_dir = (
        output_dir
        / "pages"
    )

    pages_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    manifest_pages: list[dict[str, Any]] = []

    for page in pages:
        page_number = page["page"]

        filename = (
            f"page_{page_number:03d}.txt"
        )

        page_path = (
            pages_dir
            / filename
        )

        page_path.write_text(
            page["text"],
            encoding="utf-8",
        )

        manifest_pages.append(
            {
                "page": page_number,
                "file": str(page_path),
                "characterCount": (
                    page["characterCount"]
                ),
            }
        )

    manifest = {
        "source": str(
            source_path
        ),
        "pageCount": len(
            pages
        ),
        "pages": manifest_pages,
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


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Extract the drone manual "
            "into page-level text files."
        )
    )

    parser.add_argument(
        "--input",
        default=str(
            DEFAULT_MANUAL_PATH
        ),
    )

    parser.add_argument(
        "--output",
        default=str(
            DEFAULT_OUTPUT_DIR
        ),
    )

    args = parser.parse_args()

    input_path = Path(
        args.input
    )

    output_dir = Path(
        args.output
    )

    pages = extract_manual_pages(
        input_path
    )

    save_manual_cache(
        pages=pages,
        output_dir=output_dir,
        source_path=input_path,
    )

    empty_pages = sum(
        1
        for page in pages
        if not page["text"]
    )

    total_characters = sum(
        page["characterCount"]
        for page in pages
    )

    print(
        "==================================="
    )
    print(
        "DRONE MANUAL LOADER"
    )
    print(
        "==================================="
    )
    print(
        f"Input      : {input_path}"
    )
    print(
        f"Output     : {output_dir}"
    )
    print(
        f"Pages      : {len(pages)}"
    )
    print(
        f"Empty pages: {empty_pages}"
    )
    print(
        f"Characters : {total_characters}"
    )


if __name__ == "__main__":
    main()
