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
    sanitize_id,
)
from tools.question_builder.vision.webdesign_answer_vision import (
    validate_webdesign_answers,
)
from tools.question_builder.vision.webdesign_source_vision import (
    validate_webdesign_knowledge,
)


def load_json_object(
    path: Path,
) -> Dict[str, Any]:
    path = Path(
        path
    )

    if not path.exists():
        raise FileNotFoundError(
            path
        )

    data = json.loads(
        path.read_text(
            encoding="utf-8"
        )
    )

    if not isinstance(
        data,
        dict,
    ):
        raise ValueError(
            f"JSON must contain an object: {path}"
        )

    return data


def build_reconciled_text(
    concept: Dict[str, Any],
    answer: Dict[str, Any],
) -> str:
    parts = [
        concept["summary"],
    ]

    verified_facts = answer[
        "verifiedFacts"
    ]

    if verified_facts:
        parts.append(
            "確認済み事項: "
            + " / ".join(
                verified_facts
            )
        )

    explanation_summary = answer[
        "explanationSummary"
    ]

    if explanation_summary:
        parts.append(
            "解答解説要約: "
            + explanation_summary
        )

    learning_objectives = concept[
        "learningObjectives"
    ]

    if learning_objectives:
        parts.append(
            "学習目標: "
            + " / ".join(
                learning_objectives
            )
        )

    return "\n".join(
        parts
    )


def build_reconciled_item(
    concept: Dict[str, Any],
    answer: Dict[str, Any],
    *,
    document_id: str,
    concept_index: int,
) -> Dict[str, Any]:
    question_numbers = concept[
        "sourceQuestionNumbers"
    ]

    if len(question_numbers) != 1:
        raise ValueError(
            "Reconciliation requires exactly "
            "one source question number"
        )

    question_no = question_numbers[0]

    if answer["questionNo"] != question_no:
        raise ValueError(
            "Question number mismatch"
        )

    item_id = (
        "webdesign-"
        f"{sanitize_id(document_id)}-"
        f"q{question_no:03d}-"
        f"c{concept_index:02d}"
    )

    section_match = (
        concept["section"]
        == answer["section"]
    )

    return {
        "id": item_id,
        "section": concept["section"],
        "title": concept["title"],
        "pages": concept["sourcePages"],
        "keywords": concept["keywords"],
        "facts": answer[
            "verifiedFacts"
        ],
        "candidateFacts": concept[
            "facts"
        ],
        "text": build_reconciled_text(
            concept,
            answer,
        ),
        "learningObjectives": concept[
            "learningObjectives"
        ],
        "knowledgeType": "exam_content",
        "questionGenerationEligible": True,
        "sourceQuestionNumbers": [
            question_no
        ],
        "correctAnswer": answer[
            "correctAnswer"
        ],
        "answerExplanationSummary": answer[
            "explanationSummary"
        ],
        "answerSourcePages": answer[
            "sourcePages"
        ],
        "answerSection": answer[
            "section"
        ],
        "sectionMatch": (
            section_match
        ),
        "verificationStatus": (
            "verified_from_answer"
        ),
        "reviewStatus": "pending",
        "sourceDocument": document_id,
    }


def reconcile_question_and_answer(
    question_data: Dict[str, Any],
    answer_data: Dict[str, Any],
    *,
    document_id: str,
) -> Dict[str, Any]:
    question_page = question_data.get(
        "page"
    )

    answer_page = answer_data.get(
        "page"
    )

    validated_questions = (
        validate_webdesign_knowledge(
            question_data,
            expected_page=question_page,
        )
    )

    validated_answers = (
        validate_webdesign_answers(
            answer_data,
            expected_page=answer_page,
        )
    )

    answer_map = {
        item["questionNo"]: item
        for item
        in validated_answers[
            "answers"
        ]
    }

    items: List[
        Dict[str, Any]
    ] = []

    unmatched_question_numbers = set()
    ambiguous_concept_count = 0
    skipped_concept_count = 0
    section_mismatch_count = 0

    for concept_index, concept in enumerate(
        validated_questions[
            "concepts"
        ],
        start=1,
    ):
        if (
            concept["knowledgeType"]
            != "exam_content"
            or concept[
                "questionGenerationEligible"
            ]
            is not True
        ):
            skipped_concept_count += 1
            continue

        question_numbers = concept[
            "sourceQuestionNumbers"
        ]

        if len(question_numbers) != 1:
            ambiguous_concept_count += 1

            for question_no in (
                question_numbers
            ):
                unmatched_question_numbers.add(
                    question_no
                )

            continue

        question_no = (
            question_numbers[0]
        )

        answer = answer_map.get(
            question_no
        )

        if answer is None:
            unmatched_question_numbers.add(
                question_no
            )
            continue

        item = build_reconciled_item(
            concept,
            answer,
            document_id=document_id,
            concept_index=concept_index,
        )

        if not item[
            "sectionMatch"
        ]:
            section_mismatch_count += 1

        items.append(
            item
        )

    matched_question_numbers = sorted(
        {
            item[
                "sourceQuestionNumbers"
            ][0]
            for item in items
        }
    )

    return {
        "exam": "webdesign",
        "materialType": (
            "reconciled_knowledge_draft"
        ),
        "documentId": document_id,
        "questionPage": question_page,
        "answerPage": answer_page,
        "matchedCount": len(
            items
        ),
        "matchedQuestionNumbers": (
            matched_question_numbers
        ),
        "unmatchedQuestionNumbers": sorted(
            unmatched_question_numbers
        ),
        "skippedConceptCount": (
            skipped_concept_count
        ),
        "ambiguousConceptCount": (
            ambiguous_concept_count
        ),
        "sectionMismatchCount": (
            section_mismatch_count
        ),
        "items": items,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Reconcile WebDesign question "
            "concepts with answer explanations."
        )
    )

    parser.add_argument(
        "--question-json",
        required=True,
    )

    parser.add_argument(
        "--answer-json",
        required=True,
    )

    parser.add_argument(
        "--document-id",
        required=True,
    )

    parser.add_argument(
        "--output",
        required=True,
    )

    args = parser.parse_args()

    question_data = load_json_object(
        Path(
            args.question_json
        )
    )

    answer_data = load_json_object(
        Path(
            args.answer_json
        )
    )

    result = (
        reconcile_question_and_answer(
            question_data,
            answer_data,
            document_id=(
                args.document_id
            ),
        )
    )

    output_path = Path(
        args.output
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_path.write_text(
        json.dumps(
            result,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(
        "==================================="
    )
    print(
        "WEBDESIGN KNOWLEDGE RECONCILE"
    )
    print(
        "==================================="
    )
    print(
        "Matched          :",
        result["matchedCount"],
    )
    print(
        "Matched questions:",
        result[
            "matchedQuestionNumbers"
        ],
    )
    print(
        "Unmatched        :",
        result[
            "unmatchedQuestionNumbers"
        ],
    )
    print(
        "Skipped concepts :",
        result[
            "skippedConceptCount"
        ],
    )
    print(
        "Ambiguous        :",
        result[
            "ambiguousConceptCount"
        ],
    )
    print(
        "Section mismatch :",
        result[
            "sectionMismatchCount"
        ],
    )
    print(
        "Output           :",
        output_path,
    )


if __name__ == "__main__":
    main()
