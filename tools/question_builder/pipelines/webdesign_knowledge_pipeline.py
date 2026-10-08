import argparse
import json
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List

import fitz


ROOT_DIR = Path(__file__).resolve().parents[3]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(
        0,
        str(ROOT_DIR),
    )

from tools.question_builder.vision.webdesign_source_vision import (
    analyze_webdesign_page_cached,
    get_cache_path,
)


DEFAULT_OUTPUT_DIR = (
    ROOT_DIR
    / "generated_materials"
    / "webdesign"
    / "knowledge_drafts"
)


def sanitize_id(value: str) -> str:
    cleaned = (
        value.strip()
        .replace("/", "_")
        .replace("\\", "_")
        .replace(" ", "_")
    )

    if not cleaned:
        raise ValueError(
            "document_id must not be empty"
        )

    return cleaned


def render_page(
    document: fitz.Document,
    *,
    page_number: int,
    output_path: Path,
) -> Path:
    if page_number < 1:
        raise ValueError(
            "page_number must be at least 1"
        )

    if page_number > len(document):
        raise ValueError(
            "page_number exceeds PDF page count"
        )

    page = document[
        page_number - 1
    ]

    pix = page.get_pixmap(
        matrix=fitz.Matrix(2, 2)
    )

    pix.save(
        output_path
    )

    return output_path


def concept_to_knowledge_item(
    concept: Dict[str, Any],
    *,
    document_id: str,
    page_number: int,
    concept_index: int,
) -> Dict[str, Any]:
    item_id = (
        f"webdesign-"
        f"{sanitize_id(document_id)}-"
        f"p{page_number:03d}-"
        f"c{concept_index:02d}"
    )

    learning_objectives = concept[
        "learningObjectives"
    ]

    facts = concept["facts"]

    text_parts = [
        concept["summary"],
    ]

    if facts:
        text_parts.append(
            "確認事項: "
            + " / ".join(
                facts
            )
        )

    if learning_objectives:
        text_parts.append(
            "学習目標: "
            + " / ".join(
                learning_objectives
            )
        )

    return {
        "id": item_id,
        "section": concept["section"],
        "title": concept["title"],
        "pages": concept["sourcePages"],
        "keywords": concept["keywords"],
        "facts": facts,
        "text": "\n".join(
            text_parts
        ),
        "learningObjectives": (
            learning_objectives
        ),
        "knowledgeType": concept[
            "knowledgeType"
        ],
        "sourceQuestionNumbers": concept[
            "sourceQuestionNumbers"
        ],
        "questionGenerationEligible": (
            concept[
                "questionGenerationEligible"
            ]
        ),
        "reviewStatus": "pending",
        "sourceDocument": document_id,
    }


def build_knowledge_draft(
    pdf_path: Path,
    *,
    document_id: str,
    start_page: int = 1,
    max_pages: int = 1,
    allow_api: bool = False,
    max_api_calls: int = 1,
) -> Dict[str, Any]:
    pdf_path = Path(
        pdf_path
    ).resolve()

    if not pdf_path.exists():
        raise FileNotFoundError(
            pdf_path
        )

    if start_page < 1:
        raise ValueError(
            "start_page must be at least 1"
        )

    if max_pages < 1:
        raise ValueError(
            "max_pages must be at least 1"
        )

    if max_api_calls < 0:
        raise ValueError(
            "max_api_calls must not be negative"
        )

    document = fitz.open(
        pdf_path
    )

    try:
        final_page = min(
            len(document),
            start_page
            + max_pages
            - 1,
        )

        if start_page > len(document):
            raise ValueError(
                "start_page exceeds PDF page count"
            )

        processed_pages = []
        skipped_pages = []
        items: List[
            Dict[str, Any]
        ] = []

        total_concepts = 0
        excluded_concepts = 0
        api_calls = 0

        with tempfile.TemporaryDirectory(
            prefix=(
                "study_quest_"
                "webdesign_"
            )
        ) as temp_dir:
            temp_path = Path(
                temp_dir
            )

            for page_number in range(
                start_page,
                final_page + 1,
            ):
                cache_path = (
                    get_cache_path(
                        document_id,
                        page_number,
                    )
                )

                cache_exists = (
                    cache_path.exists()
                )

                if (
                    not cache_exists
                    and not allow_api
                ):
                    print(
                        "[SKIP] "
                        f"page={page_number} "
                        "cache missing / "
                        "API disabled"
                    )

                    skipped_pages.append(
                        page_number
                    )

                    continue

                if (
                    not cache_exists
                    and allow_api
                ):
                    if (
                        api_calls
                        >= max_api_calls
                    ):
                        print(
                            "[SKIP] "
                            f"page={page_number} "
                            "API call limit reached"
                        )

                        skipped_pages.append(
                            page_number
                        )

                        continue

                    api_calls += 1

                image_path = (
                    temp_path
                    / (
                        f"page_"
                        f"{page_number:03d}"
                        f".png"
                    )
                )

                render_page(
                    document,
                    page_number=page_number,
                    output_path=image_path,
                )

                result = (
                    analyze_webdesign_page_cached(
                        image_path,
                        document_id=(
                            document_id
                        ),
                        page_number=(
                            page_number
                        ),
                        allow_api=(
                            allow_api
                        ),
                    )
                )

                concepts = result[
                    "concepts"
                ]

                total_concepts += len(
                    concepts
                )

                eligible_concepts = [
                    concept
                    for concept
                    in concepts
                    if (
                        concept[
                            "knowledgeType"
                        ]
                        == "exam_content"
                        and concept[
                            "questionGenerationEligible"
                        ]
                        is True
                    )
                ]

                excluded_concepts += (
                    len(concepts)
                    - len(
                        eligible_concepts
                    )
                )

                for (
                    concept_index,
                    concept,
                ) in enumerate(
                    eligible_concepts,
                    start=1,
                ):
                    items.append(
                        concept_to_knowledge_item(
                            concept,
                            document_id=(
                                document_id
                            ),
                            page_number=(
                                page_number
                            ),
                            concept_index=(
                                concept_index
                            ),
                        )
                    )

                processed_pages.append(
                    page_number
                )

                print(
                    "[PAGE] "
                    f"{page_number} "
                    f"concepts="
                    f"{len(concepts)} "
                    f"eligible="
                    f"{len(eligible_concepts)}"
                )

        return {
            "exam": "webdesign",
            "materialType": (
                "knowledge_draft"
            ),
            "documentId": (
                document_id
            ),
            "source": str(
                pdf_path
            ),
            "processedPages": (
                processed_pages
            ),
            "skippedPages": (
                skipped_pages
            ),
            "totalConceptCount": (
                total_concepts
            ),
            "excludedConceptCount": (
                excluded_concepts
            ),
            "itemCount": len(
                items
            ),
            "apiCalls": api_calls,
            "items": items,
        }
    finally:
        document.close()


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Build WebDesign "
            "Knowledge drafts "
            "from image PDFs."
        )
    )

    parser.add_argument(
        "--pdf",
        required=True,
    )

    parser.add_argument(
        "--document-id",
        required=True,
    )

    parser.add_argument(
        "--start-page",
        type=int,
        default=1,
    )

    parser.add_argument(
        "--max-pages",
        type=int,
        default=1,
    )

    parser.add_argument(
        "--allow-api",
        action="store_true",
    )

    parser.add_argument(
        "--max-api-calls",
        type=int,
        default=1,
    )

    parser.add_argument(
        "--output-dir",
        default=str(
            DEFAULT_OUTPUT_DIR
        ),
    )

    args = parser.parse_args()

    result = build_knowledge_draft(
        Path(args.pdf),
        document_id=(
            args.document_id
        ),
        start_page=(
            args.start_page
        ),
        max_pages=(
            args.max_pages
        ),
        allow_api=(
            args.allow_api
        ),
        max_api_calls=(
            args.max_api_calls
        ),
    )

    output_dir = Path(
        args.output_dir
    )

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_path = (
        output_dir
        / (
            sanitize_id(
                args.document_id
            )
            + ".json"
        )
    )

    output_path.write_text(
        json.dumps(
            result,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print()
    print(
        "==================================="
    )
    print(
        "WEBDESIGN KNOWLEDGE DRAFT"
    )
    print(
        "==================================="
    )
    print(
        "Processed pages :",
        len(
            result[
                "processedPages"
            ]
        ),
    )
    print(
        "Skipped pages   :",
        len(
            result[
                "skippedPages"
            ]
        ),
    )
    print(
        "Concepts        :",
        result[
            "totalConceptCount"
        ],
    )
    print(
        "Excluded        :",
        result[
            "excludedConceptCount"
        ],
    )
    print(
        "Knowledge items :",
        result[
            "itemCount"
        ],
    )
    print(
        "API calls       :",
        result[
            "apiCalls"
        ],
    )
    print(
        "Output          :",
        output_path,
    )


if __name__ == "__main__":
    main()
