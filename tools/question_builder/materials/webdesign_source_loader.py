from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from pypdf import PdfReader


DEFAULT_SOURCE_DIR = Path(
    "source_materials/webdesign/theory/pdf"
)

DEFAULT_OUTPUT_DIR = Path(
    "generated_materials/webdesign/source_pages"
)


def normalize_page_text(
    text: str,
) -> str:
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

    normalized: list[str] = []
    previous_blank = False

    for line in lines:
        stripped = line.strip()

        if not stripped:
            if not previous_blank:
                normalized.append("")
            previous_blank = True
            continue

        normalized.append(stripped)
        previous_blank = False

    return "\n".join(
        normalized
    ).strip()


def extract_pdf_pages(
    pdf_path: Path,
) -> list[dict[str, Any]]:
    if not pdf_path.exists():
        raise FileNotFoundError(
            f"PDF not found: {pdf_path}"
        )

    reader = PdfReader(
        str(pdf_path)
    )

    pages: list[dict[str, Any]] = []

    for page_number, page in enumerate(
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
                "page": page_number,
                "text": text,
                "characterCount": len(text),
            }
        )

    return pages


def build_source_cache(
    source_dir: Path,
    output_dir: Path,
) -> dict[str, Any]:
    pdf_paths = sorted(
        source_dir.glob("*.pdf")
    )

    if not pdf_paths:
        raise FileNotFoundError(
            "No PDF files found in: "
            f"{source_dir}"
        )

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    documents = []

    for pdf_path in pdf_paths:
        pages = extract_pdf_pages(
            pdf_path
        )

        document_id = pdf_path.stem

        document_dir = (
            output_dir
            / document_id
        )

        document_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        pages_path = (
            document_dir
            / "pages.json"
        )

        pages_path.write_text(
            json.dumps(
                pages,
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
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

        requires_vision = (
            total_characters == 0
        )

        documents.append(
            {
                "id": document_id,
                "source": str(pdf_path),
                "pageCount": len(pages),
                "emptyPages": empty_pages,
                "characterCount": (
                    total_characters
                ),
                "requiresVision": (
                    requires_vision
                ),
                "pagesFile": str(
                    pages_path
                ),
            }
        )

    manifest = {
        "exam": "webdesign",
        "materialType": "source_pages",
        "documents": documents,
        "documentCount": len(documents),
        "visionRequiredCount": sum(
            1
            for item in documents
            if item["requiresVision"]
        ),
        "pageCount": sum(
            item["pageCount"]
            for item in documents
        ),
        "characterCount": sum(
            item["characterCount"]
            for item in documents
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

    manifest["manifestFile"] = str(
        manifest_path
    )

    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Extract WebDesign PDF sources "
            "into page-level text caches."
        )
    )

    parser.add_argument(
        "--source-dir",
        default=str(
            DEFAULT_SOURCE_DIR
        ),
    )

    parser.add_argument(
        "--output-dir",
        default=str(
            DEFAULT_OUTPUT_DIR
        ),
    )

    args = parser.parse_args()

    manifest = build_source_cache(
        source_dir=Path(
            args.source_dir
        ),
        output_dir=Path(
            args.output_dir
        ),
    )

    print(
        "==================================="
    )
    print(
        "WEBDESIGN SOURCE LOADER"
    )
    print(
        "==================================="
    )
    print(
        f"Documents  : "
        f"{manifest['documentCount']}"
    )
    print(
        f"Pages      : "
        f"{manifest['pageCount']}"
    )
    print(
        f"Characters : "
        f"{manifest['characterCount']}"
    )
    print(
        f"Manifest   : "
        f"{manifest['manifestFile']}"
    )


if __name__ == "__main__":
    main()
