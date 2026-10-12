from __future__ import annotations

import hashlib
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tools.question_builder.webdesign_knowledge_quality_reviewer import (
    WebDesignKnowledgeQualityReviewer,
    build_knowledge_quality_prompt,
    validate_knowledge_quality_review,
)


REVIEWER_PATH = (
    Path(__file__).resolve().parent
    / "webdesign_knowledge_quality_reviewer.py"
)


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def json_sha256(value: Any) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")

    return sha256(encoded)


def create_qa_record(
    *,
    knowledge: dict[str, Any],
    review: dict[str, Any],
    model: str,
) -> dict[str, Any]:
    if not isinstance(model, str) or not model.strip():
        raise ValueError("QA model is required")

    if not isinstance(knowledge, dict):
        raise ValueError("Knowledge must be an object")

    facts = knowledge.get("facts")
    objectives = knowledge.get("learningObjectives")

    if not isinstance(facts, list) or not isinstance(
        objectives, list
    ):
        raise ValueError(
            "Knowledge facts and objectives must be lists"
        )

    validate_knowledge_quality_review(
        review,
        fact_count=len(facts),
        objective_count=len(objectives),
    )

    prompt = build_knowledge_quality_prompt(
        knowledge=knowledge
    )

    return {
        "recordVersion": 1,
        "knowledgeId": knowledge["id"],
        "model": model,
        "reviewedAtUtc": datetime.now(
            timezone.utc
        ).isoformat(),
        "prompt": prompt,
        "promptSha256": sha256(
            prompt.encode("utf-8")
        ),
        "review": review,
        "reviewSha256": json_sha256(review),
        "reviewerCodeSha256": sha256(
            REVIEWER_PATH.read_bytes()
        ),
    }


def inspect_qa_record(
    *,
    knowledge: dict[str, Any],
    record_path: Path,
) -> dict[str, Any]:
    record = json.loads(
        Path(record_path).read_text(
            encoding="utf-8"
        )
    )

    required = {
        "recordVersion",
        "knowledgeId",
        "model",
        "reviewedAtUtc",
        "prompt",
        "promptSha256",
        "review",
        "reviewSha256",
        "reviewerCodeSha256",
    }

    if not isinstance(record, dict) or set(record) != required:
        raise ValueError("Invalid QA record structure")

    if record["recordVersion"] != 1:
        raise ValueError("Unsupported QA record version")

    if record["knowledgeId"] != knowledge.get("id"):
        raise ValueError("QA Knowledge ID mismatch")

    if (
        not isinstance(record["model"], str)
        or not record["model"].strip()
    ):
        raise ValueError("Invalid QA model")

    datetime.fromisoformat(
        record["reviewedAtUtc"].replace("Z", "+00:00")
    )

    current_prompt = build_knowledge_quality_prompt(
        knowledge=knowledge
    )

    if record["prompt"] != current_prompt:
        raise ValueError(
            "Knowledge QA input differs from recorded input"
        )

    if record["promptSha256"] != sha256(
        current_prompt.encode("utf-8")
    ):
        raise ValueError("QA prompt hash mismatch")

    if record["reviewSha256"] != json_sha256(
        record["review"]
    ):
        raise ValueError("QA review hash mismatch")

    if record["reviewerCodeSha256"] != sha256(
        REVIEWER_PATH.read_bytes()
    ):
        raise ValueError("QA reviewer code has changed")

    review = record["review"]

    validate_knowledge_quality_review(
        review,
        fact_count=len(knowledge["facts"]),
        objective_count=len(
            knowledge["learningObjectives"]
        ),
    )

    if review != knowledge.get("knowledgeQa"):
        raise ValueError(
            "Current Knowledge QA differs from recorded review"
        )

    return {
        "knowledgeId": knowledge["id"],
        "decision": review["decision"],
        "model": record["model"],
        "promptSha256": record["promptSha256"],
        "reviewSha256": record["reviewSha256"],
    }


def review_and_save_qa(
    *,
    knowledge: dict[str, Any],
    record_path: Path,
    model: str = "gpt-5.5",
    allow_api: bool = False,
) -> dict[str, Any]:
    record_path = Path(record_path)

    if record_path.exists():
        raise FileExistsError(
            f"Refusing to overwrite QA record: {record_path}"
        )

    if not allow_api:
        raise RuntimeError(
            "Fresh Knowledge QA requires explicit allow_api=True"
        )

    reviewer = WebDesignKnowledgeQualityReviewer(
        model=model,
        max_api_calls=1,
    )

    review = reviewer.review(
        knowledge=knowledge,
        allow_api=True,
    )

    record = create_qa_record(
        knowledge=knowledge,
        review=review,
        model=model,
    )

    encoded = (
        json.dumps(
            record,
            ensure_ascii=False,
            indent=2,
        ) + "\n"
    ).encode("utf-8")

    record_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    temporary_path = None

    try:
        with tempfile.NamedTemporaryFile(
            dir=record_path.parent,
            prefix=".qa_record_",
            suffix=".tmp",
            delete=False,
        ) as temporary:
            temporary.write(encoded)
            temporary_path = Path(temporary.name)

        os.link(
            temporary_path,
            record_path,
        )
    finally:
        if temporary_path is not None:
            temporary_path.unlink(
                missing_ok=True
            )

    return record
