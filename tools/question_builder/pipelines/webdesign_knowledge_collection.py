import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

ROOT_DIR = Path(__file__).resolve().parents[3]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(
        0,
        str(ROOT_DIR),
    )

from tools.question_builder.pipelines.webdesign_knowledge_pipeline import (
    build_knowledge_draft,
    sanitize_id,
)


DEFAULT_OUTPUT_DIR = (
    ROOT_DIR
    / "generated_materials"
    / "webdesign"
    / "knowledge_collection"
)


def find_pdf_files(
    source_dir: Path,
) -> List[Path]:
    source_dir = Path(
        source_dir
    ).resolve()

    if not source_dir.exists():
        raise FileNotFoundError(
            source_dir
        )

    if not source_dir.is_dir():
        raise ValueError(
            "source_dir must be a directory"
        )

    pdf_files = sorted(
        path
        for path in source_dir.iterdir()
        if (
            path.is_file()
            and path.suffix.lower() == ".pdf"
        )
    )

    if not pdf_files:
        raise FileNotFoundError(
            "No PDF files found: "
            f"{source_dir}"
        )

    return pdf_files


def build_collection(
    source_dir: Path,
    *,
    start_page: int = 1,
    max_pages_per_document: int = 1,
    allow_api: bool = False,
    max_api_calls_total: int = 0,
) -> Dict[str, Any]:
    if start_page < 1:
        raise ValueError(
            "start_page must be at least 1"
        )

    if max_pages_per_document < 1:
        raise ValueError(
            "max_pages_per_document "
            "must be at least 1"
        )

    if max_api_calls_total < 0:
        raise ValueError(
            "max_api_calls_total "
            "must not be negative"
        )

    pdf_files = find_pdf_files(
        source_dir
    )

    documents = []

    total_api_calls = 0
    total_items = 0
    total_processed_pages = 0
    total_skipped_pages = 0
    total_concepts = 0
    total_excluded_concepts = 0

    for pdf_path in pdf_files:
        document_id = pdf_path.stem

        remaining_api_calls = max(
            0,
            max_api_calls_total
            - total_api_calls,
        )

        document_allow_api = (
            allow_api
            and remaining_api_calls > 0
        )

        result = build_knowledge_draft(
            pdf_path,
            document_id=document_id,
            start_page=start_page,
            max_pages=max_pages_per_document,
            allow_api=document_allow_api,
            max_api_calls=remaining_api_calls,
        )

        total_api_calls += (
            result["apiCalls"]
        )

        total_items += (
            result["itemCount"]
        )

        total_processed_pages += len(
            result["processedPages"]
        )

        total_skipped_pages += len(
            result["skippedPages"]
        )

        total_concepts += (
            result[
                "totalConceptCount"
            ]
        )

        total_excluded_concepts += (
            result[
                "excludedConceptCount"
            ]
        )

        documents.append(
            result
        )

        print(
            "[DOCUMENT] "
            f"{document_id} "
            f"processed="
            f"{len(result['processedPages'])} "
            f"skipped="
            f"{len(result['skippedPages'])} "
            f"items="
            f"{result['itemCount']} "
            f"api="
            f"{result['apiCalls']}"
        )

    return {
        "exam": "webdesign",
        "materialType": (
            "knowledge_collection"
        ),
        "sourceDir": str(
            Path(source_dir).resolve()
        ),
        "documentCount": len(
            documents
        ),
        "processedPageCount": (
            total_processed_pages
        ),
        "skippedPageCount": (
            total_skipped_pages
        ),
        "conceptCount": (
            total_concepts
        ),
        "excludedConceptCount": (
            total_excluded_concepts
        ),
        "itemCount": (
            total_items
        ),
        "apiCalls": (
            total_api_calls
        ),
        "documents": documents,
    }


def write_collection(
    collection: Dict[str, Any],
    *,
    output_dir: Path,
) -> Path:
    output_dir = Path(
        output_dir
    )

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    documents_dir = (
        output_dir
        / "documents"
    )

    documents_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    for document in collection[
        "documents"
    ]:
        document_id = document[
            "documentId"
        ]

        document_path = (
            documents_dir
            / (
                sanitize_id(
                    document_id
                )
                + ".json"
            )
        )

        document_path.write_text(
            json.dumps(
                document,
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )

    manifest = {
        key: value
        for key, value
        in collection.items()
        if key != "documents"
    }

    manifest["documents"] = [
        {
            "documentId": (
                document[
                    "documentId"
                ]
            ),
            "processedPages": (
                document[
                    "processedPages"
                ]
            ),
            "skippedPages": (
                document[
                    "skippedPages"
                ]
            ),
            "itemCount": (
                document[
                    "itemCount"
                ]
            ),
            "apiCalls": (
                document[
                    "apiCalls"
                ]
            ),
        }
        for document
        in collection["documents"]
    ]

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

    return manifest_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Build WebDesign "
            "Knowledge drafts "
            "from a PDF collection."
        )
    )

    parser.add_argument(
        "--source-dir",
        required=True,
    )

    parser.add_argument(
        "--start-page",
        type=int,
        default=1,
    )

    parser.add_argument(
        "--max-pages-per-document",
        type=int,
        default=1,
    )

    parser.add_argument(
        "--allow-api",
        action="store_true",
    )

    parser.add_argument(
        "--max-api-calls-total",
        type=int,
        default=0,
    )

    parser.add_argument(
        "--output-dir",
        default=str(
            DEFAULT_OUTPUT_DIR
        ),
    )

    args = parser.parse_args()

    collection = build_collection(
        Path(
            args.source_dir
        ),
        start_page=(
            args.start_page
        ),
        max_pages_per_document=(
            args.max_pages_per_document
        ),
        allow_api=(
            args.allow_api
        ),
        max_api_calls_total=(
            args.max_api_calls_total
        ),
    )

    manifest_path = (
        write_collection(
            collection,
            output_dir=Path(
                args.output_dir
            ),
        )
    )

    print()
    print(
        "==================================="
    )
    print(
        "WEBDESIGN KNOWLEDGE COLLECTION"
    )
    print(
        "==================================="
    )
    print(
        "Documents       :",
        collection[
            "documentCount"
        ],
    )
    print(
        "Processed pages :",
        collection[
            "processedPageCount"
        ],
    )
    print(
        "Skipped pages   :",
        collection[
            "skippedPageCount"
        ],
    )
    print(
        "Concepts        :",
        collection[
            "conceptCount"
        ],
    )
    print(
        "Excluded        :",
        collection[
            "excludedConceptCount"
        ],
    )
    print(
        "Knowledge items :",
        collection[
            "itemCount"
        ],
    )
    print(
        "API calls       :",
        collection[
            "apiCalls"
        ],
    )
    print(
        "Manifest        :",
        manifest_path,
    )


if __name__ == "__main__":
    main()
