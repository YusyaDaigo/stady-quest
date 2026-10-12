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


from tools.question_builder.webdesign_verification_record import (
    inspect_verification_record,
)


DEFAULT_OUTPUT = (
    ROOT_DIR
    / "generated_materials"
    / "webdesign"
    / "knowledge"
    / "knowledge.json"
)


REQUIRED_FIELDS = {
    "id",
    "section",
    "title",
    "pages",
    "keywords",
    "text",
}


def load_draft_files(
    input_dir: Path,
) -> List[Dict[str, Any]]:
    input_dir = Path(
        input_dir
    ).resolve()

    if not input_dir.exists():
        raise FileNotFoundError(
            input_dir
        )

    if not input_dir.is_dir():
        raise ValueError(
            "input_dir must be a directory"
        )

    paths = sorted(
        input_dir.glob("*.json")
    )

    if not paths:
        raise FileNotFoundError(
            "No draft JSON files found: "
            f"{input_dir}"
        )

    drafts = []

    for path in paths:
        try:
            data = json.loads(
                path.read_text(
                    encoding="utf-8"
                )
            )
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Invalid JSON: {path}"
            ) from exc

        if not isinstance(
            data,
            dict,
        ):
            raise ValueError(
                "Draft file must contain "
                f"an object: {path}"
            )

        items = data.get(
            "items"
        )

        if not isinstance(
            items,
            list,
        ):
            raise ValueError(
                "Draft file requires "
                f"items array: {path}"
            )

        drafts.append(
            {
                "path": str(path),
                "documentId": data.get(
                    "documentId"
                ),
                "items": items,
            }
        )

    return drafts


def validate_item(
    item: Dict[str, Any],
) -> None:
    if not isinstance(
        item,
        dict,
    ):
        raise ValueError(
            "Knowledge item must be an object"
        )

    missing = (
        REQUIRED_FIELDS
        - item.keys()
    )

    if missing:
        raise ValueError(
            "Knowledge item is missing "
            f"fields: {sorted(missing)}"
        )

    if (
        not isinstance(
            item["id"],
            str,
        )
        or not item["id"].strip()
    ):
        raise ValueError(
            "Knowledge item has invalid id"
        )

    if (
        not isinstance(
            item["section"],
            str,
        )
        or not item["section"].strip()
    ):
        raise ValueError(
            f"{item['id']}: invalid section"
        )

    if (
        not isinstance(
            item["title"],
            str,
        )
        or not item["title"].strip()
    ):
        raise ValueError(
            f"{item['id']}: invalid title"
        )

    if not isinstance(
        item["pages"],
        list,
    ):
        raise ValueError(
            f"{item['id']}: invalid pages"
        )

    if not isinstance(
        item["keywords"],
        list,
    ):
        raise ValueError(
            f"{item['id']}: invalid keywords"
        )

    if (
        not isinstance(
            item["text"],
            str,
        )
        or not item["text"].strip()
    ):
        raise ValueError(
            f"{item['id']}: invalid text"
        )


def validate_new_knowledge_gate(
    item: Dict[str, Any],
) -> None:
    knowledge_id = item["id"]

    qa = item.get("knowledgeQa")

    if (
        not isinstance(qa, dict)
        or qa.get("decision") != "pass"
    ):
        raise ValueError(
            f"{knowledge_id}: Knowledge QA "
            "must pass before publication"
        )

    human = item.get("humanReview")

    if (
        not isinstance(human, dict)
        or human.get("status") != "approved"
        or human.get("approved") is not True
    ):
        raise ValueError(
            f"{knowledge_id}: human approval "
            "is required"
        )

    record_ref = item.get(
        "factualVerificationRecord"
    )

    if (
        not isinstance(record_ref, str)
        or not record_ref.strip()
    ):
        raise ValueError(
            f"{knowledge_id}: verification "
            "record reference is required"
        )

    relative_path = Path(record_ref)

    if relative_path.is_absolute():
        raise ValueError(
            f"{knowledge_id}: absolute record "
            "paths are not allowed"
        )

    record_root = (
        ROOT_DIR
        / "generated_materials"
        / "webdesign"
        / "verification_records"
    ).resolve()

    record_dir = (
        ROOT_DIR / relative_path
    ).resolve()

    if record_root not in record_dir.parents:
        raise ValueError(
            f"{knowledge_id}: verification record "
            "must be inside the approved directory"
        )

    result = inspect_verification_record(
        knowledge=item,
        record_dir=record_dir,
    )

    if result["factualGate"] != "pass":
        raise ValueError(
            f"{knowledge_id}: factual "
            f"verification is {result['factualGate']}"
        )


def build_approved_knowledge(
    input_dir: Path,
) -> Dict[str, Any]:
    drafts = load_draft_files(
        input_dir
    )

    approved = []
    pending_count = 0
    rejected_count = 0

    seen_ids = set()

    for draft in drafts:
        for item in draft[
            "items"
        ]:
            validate_item(
                item
            )

            status = item.get(
                "reviewStatus"
            )

            if status == "pending":
                pending_count += 1
                continue

            if status == "rejected":
                rejected_count += 1
                continue

            if status != "approved":
                raise ValueError(
                    f"{item['id']}: invalid "
                    "reviewStatus "
                    f"{status!r}"
                )

            if (
                item.get(
                    "knowledgeType"
                )
                != "exam_content"
            ):
                raise ValueError(
                    f"{item['id']}: approved "
                    "item must be exam_content"
                )

            if (
                item.get(
                    "questionGenerationEligible"
                )
                is not True
            ):
                raise ValueError(
                    f"{item['id']}: approved "
                    "item must be generation eligible"
                )

            validate_new_knowledge_gate(
                item
            )

            knowledge_id = item[
                "id"
            ]

            if knowledge_id in seen_ids:
                raise ValueError(
                    "Duplicate knowledge ID: "
                    f"{knowledge_id}"
                )

            seen_ids.add(
                knowledge_id
            )

            approved.append(
                item
            )

    return {
        "draftFileCount": len(
            drafts
        ),
        "approvedCount": len(
            approved
        ),
        "pendingCount": (
            pending_count
        ),
        "rejectedCount": (
            rejected_count
        ),
        "items": approved,
    }


def write_knowledge(
    items: List[Dict[str, Any]],
    output_path: Path,
) -> None:
    output_path = Path(
        output_path
    )

    existing_ids = set()

    if output_path.exists():
        existing = json.loads(
            output_path.read_text(
                encoding="utf-8"
            )
        )

        if not isinstance(existing, list):
            raise ValueError(
                "Existing published Knowledge "
                "must be an array"
            )

        incoming_by_id = {}

        for item in items:
            validate_item(item)
            knowledge_id = item["id"]

            if knowledge_id in incoming_by_id:
                raise ValueError(
                    "Duplicate incoming Knowledge ID: "
                    f"{knowledge_id}"
                )

            incoming_by_id[knowledge_id] = item

        existing_ids = set()

        for original in existing:
            if not isinstance(original, dict):
                raise ValueError(
                    "Invalid existing Knowledge item"
                )

            knowledge_id = original.get("id")

            if (
                not isinstance(knowledge_id, str)
                or not knowledge_id.strip()
            ):
                raise ValueError(
                    "Invalid existing Knowledge ID"
                )

            if knowledge_id in existing_ids:
                raise ValueError(
                    "Duplicate existing Knowledge ID: "
                    f"{knowledge_id}"
                )

            existing_ids.add(knowledge_id)

            if knowledge_id not in incoming_by_id:
                raise ValueError(
                    "Refusing to remove published "
                    f"Knowledge: {knowledge_id}"
                )

            if incoming_by_id[knowledge_id] != original:
                raise ValueError(
                    "Refusing to modify published "
                    f"Knowledge: {knowledge_id}"
                )

    seen_incoming_ids = set()

    for item in items:
        validate_item(item)

        knowledge_id = item["id"]

        if knowledge_id in seen_incoming_ids:
            raise ValueError(
                "Duplicate incoming Knowledge ID: "
                f"{knowledge_id}"
            )

        seen_incoming_ids.add(knowledge_id)

        if knowledge_id in existing_ids:
            continue

        if item.get("reviewStatus") != "approved":
            raise ValueError(
                f"{knowledge_id}: new Knowledge "
                "must be approved"
            )

        if item.get("knowledgeType") != "exam_content":
            raise ValueError(
                f"{knowledge_id}: new Knowledge "
                "must be exam_content"
            )

        if item.get("questionGenerationEligible") is not True:
            raise ValueError(
                f"{knowledge_id}: new Knowledge "
                "must be generation eligible"
            )

        validate_new_knowledge_gate(item)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_path.write_text(
        json.dumps(
            items,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Publish only approved "
            "WebDesign Knowledge items."
        )
    )

    parser.add_argument(
        "--input-dir",
        required=True,
    )

    parser.add_argument(
        "--output",
        default=str(
            DEFAULT_OUTPUT
        ),
    )

    parser.add_argument(
        "--write",
        action="store_true",
    )

    args = parser.parse_args()

    result = (
        build_approved_knowledge(
            Path(
                args.input_dir
            )
        )
    )

    print(
        "==================================="
    )
    print(
        "WEBDESIGN KNOWLEDGE PUBLISH"
    )
    print(
        "==================================="
    )
    print(
        "Draft files :",
        result["draftFileCount"],
    )
    print(
        "Approved    :",
        result["approvedCount"],
    )
    print(
        "Pending     :",
        result["pendingCount"],
    )
    print(
        "Rejected    :",
        result["rejectedCount"],
    )

    if not args.write:
        print(
            "Write       : DISABLED"
        )
        return

    output_path = Path(
        args.output
    )

    write_knowledge(
        result["items"],
        output_path,
    )

    print(
        "Write       : ENABLED"
    )
    print(
        "Output      :",
        output_path,
    )


if __name__ == "__main__":
    main()
