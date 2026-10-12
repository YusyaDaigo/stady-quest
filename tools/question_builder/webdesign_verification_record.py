from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from tools.question_builder.webdesign_factual_verifier import (
    build_fact_targets,
    validate_evidence,
    validate_factual_result,
)


MUTABLE_REVIEW_FIELDS = {
    "reviewStatus",
    "humanReview",
    "knowledgeQa",
    "factualGate",
    "factualVerificationRecord",
    "verificationStatus",
}

REQUIRED_ARTIFACTS = {
    "knowledge_snapshot.json",
    "evidence.json",
    "factual_result_legacy.json",
    "factual_context_result.json",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_json(path: Path) -> dict | list:
    return json.loads(
        path.read_text(encoding="utf-8")
    )


def content_fields(item: dict[str, Any]) -> dict:
    return {
        key: value
        for key, value in item.items()
        if key not in MUTABLE_REVIEW_FIELDS
    }


def inspect_verification_record(
    *,
    knowledge: dict[str, Any],
    record_dir: Path,
) -> dict[str, Any]:
    record_dir = Path(record_dir)

    manifest = read_json(
        record_dir / "manifest.json"
    )

    if not isinstance(manifest, dict):
        raise ValueError("Invalid verification manifest")

    if manifest.get("recordVersion") != 1:
        raise ValueError(
            "Unsupported verification record version"
        )

    artifacts = manifest.get("artifactSha256")

    if (
        not isinstance(artifacts, dict)
        or set(artifacts) != REQUIRED_ARTIFACTS
    ):
        raise ValueError(
            "Verification artifact list mismatch"
        )

    for filename, expected_digest in artifacts.items():
        raw = (record_dir / filename).read_bytes()

        if sha256(raw) != expected_digest:
            raise ValueError(
                f"Verification artifact changed: {filename}"
            )

    snapshot = read_json(
        record_dir / "knowledge_snapshot.json"
    )

    if not isinstance(snapshot, dict):
        raise ValueError("Invalid Knowledge snapshot")

    if knowledge.get("id") != manifest.get("knowledgeId"):
        raise ValueError("Knowledge ID mismatch")

    if snapshot.get("id") != knowledge.get("id"):
        raise ValueError("Snapshot Knowledge ID mismatch")

    if content_fields(snapshot) != content_fields(knowledge):
        raise ValueError(
            "Knowledge content differs from "
            "verification snapshot"
        )

    evidence_raw = (
        record_dir / "evidence.json"
    ).read_bytes()

    evidence = json.loads(
        evidence_raw.decode("utf-8")
    )

    validate_evidence(evidence)

    record = read_json(
        record_dir / "factual_context_result.json"
    )

    if not isinstance(record, dict):
        raise ValueError("Invalid factual result")

    if record.get("knowledgeId") != knowledge["id"]:
        raise ValueError(
            "Factual result Knowledge ID mismatch"
        )

    if record.get("evidenceSha256") != sha256(evidence_raw):
        raise ValueError(
            "Factual result Evidence hash mismatch"
        )

    for result_key, manifest_key in [
        ("draftSha256", "sourceDraftSha256"),
        ("verifierSha256", "verifierSha256"),
    ]:
        if record.get(result_key) != manifest.get(
            manifest_key
        ):
            raise ValueError(
                f"Verification provenance mismatch: {result_key}"
            )

    result = record.get("verification")

    if not isinstance(result, dict):
        raise ValueError(
            "Missing factual verification result"
        )

    targets = build_fact_targets(knowledge)

    validate_factual_result(
        result,
        fact_count=len(targets),
        evidence_count=len(evidence),
    )

    if result.get("factTargets") != targets:
        raise ValueError(
            "Verified facts differ from current Knowledge"
        )

    context_status = result[
        "contextAssessment"
    ]["status"]

    expected_gate = (
        "pass"
        if (
            result["decision"] == "verified"
            and context_status == "supported"
        )
        else "hold"
    )

    if result.get("factualGate") != expected_gate:
        raise ValueError(
            "Factual gate contradicts verification result"
        )

    if (
        manifest.get("factualDecision") != result["decision"]
        or manifest.get("contextDecision") != context_status
        or manifest.get("factualGate") != expected_gate
    ):
        raise ValueError(
            "Manifest contradicts factual verification"
        )

    return {
        "knowledgeId": knowledge["id"],
        "factualDecision": result["decision"],
        "contextDecision": context_status,
        "factualGate": expected_gate,
        "factCount": len(targets),
        "evidenceCount": len(evidence),
    }
