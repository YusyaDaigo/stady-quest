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
