from __future__ import annotations

import argparse
import json
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tools.question_builder.continuous_planner import (
    block_knowledge,
    create_planner_state,
    record_difficulty_ceiling,
    record_difficulty_pass,
    record_knowledge_use,
    select_next_knowledge,
    select_target_difficulty,
)
from tools.question_builder.continuous_question_cycle import (
    run_webdesign_question_cycle,
)
from tools.question_builder.continuous_semantic_gate import (
    build_app_comparison_records,
    build_comparison_record,
    evaluate_webdesign_semantic_gate,
)
from tools.question_builder.exam_generation_profiles import (
    get_exam_generation_profile,
)
from tools.question_builder.knowledge.loader import (
    load_knowledge,
)
from tools.question_builder.webdesign_question_pool_loader import (
    load_webdesign_question_pool,
)


SESSION_STATE_VERSION = 4

DEFAULT_STATE_ROOT = Path(
    "generated_materials"
)


def now_iso() -> str:
    return datetime.now(
        timezone.utc
    ).isoformat()


def normalize_question_types(
    raw_value: str | None,
    *,
    profile: dict[str, Any],
) -> list[str]:
    supported = profile.get(
        "questionTypes",
        {}
    )

    if raw_value is None:
        return list(
            supported.keys()
        )

    values = [
        item.strip().lower()
        for item in raw_value.split(",")
        if item.strip()
    ]

    if len(values) != len(set(values)):
        raise ValueError(
            "question types must not contain duplicates"
        )

    if not supported and values:
        raise ValueError(
            "this exam profile does not define "
            "question types"
        )

    unknown = [
        item
        for item in values
        if item not in supported
    ]

    if unknown:
        raise ValueError(
            "unsupported question types: "
            f"{unknown}. "
            "supported: "
            f"{sorted(supported)}"
        )

    return values


def validate_session_config(
    *,
    exam: str,
    section: str,
    difficulty_min: int,
    difficulty_max: int,
    question_types: str | None,
) -> dict[str, Any]:
    normalized_exam = (
        exam.strip().lower()
    )

    normalized_section = (
        section.strip().lower()
    )

    profile = (
        get_exam_generation_profile(
            normalized_exam
        )
    )

    if normalized_section not in (
        profile["sections"]
    ):
        raise ValueError(
            f"unsupported section for "
            f"{normalized_exam}: "
            f"{normalized_section}. "
            f"supported: "
            f"{sorted(profile['sections'])}"
        )

    if not isinstance(
        difficulty_min,
        int,
    ):
        raise ValueError(
            "difficulty_min must be an integer"
        )

    if not isinstance(
        difficulty_max,
        int,
    ):
        raise ValueError(
            "difficulty_max must be an integer"
        )

    profile_min = int(
        profile["difficultyMin"]
    )

    profile_max = int(
        profile["difficultyMax"]
    )

    if not (
        profile_min
        <= difficulty_min
        <= profile_max
    ):
        raise ValueError(
            "difficulty_min must be between "
            f"{profile_min} and {profile_max}"
        )

    if not (
        profile_min
        <= difficulty_max
        <= profile_max
    ):
        raise ValueError(
            "difficulty_max must be between "
            f"{profile_min} and {profile_max}"
        )

    if difficulty_min > difficulty_max:
        raise ValueError(
            "difficulty_min must not exceed "
            "difficulty_max"
        )

    normalized_question_types = (
        normalize_question_types(
            question_types,
            profile=profile,
        )
    )

    return {
        "exam": normalized_exam,
        "section": normalized_section,
        "difficultyMin": difficulty_min,
        "difficultyMax": difficulty_max,
        "questionTypes": (
            normalized_question_types
        ),
        "profile": profile,
    }


def build_session_id() -> str:
    timestamp = datetime.now(
        timezone.utc
    ).strftime(
        "%Y%m%dT%H%M%SZ"
    )

    suffix = uuid.uuid4().hex[:8]

    return (
        f"{timestamp}-{suffix}"
    )


def get_session_path(
    *,
    state_root: Path,
    exam: str,
    session_id: str,
) -> Path:
    return (
        state_root
        / exam
        / "continuous_sessions"
        / f"{session_id}.json"
    )


def save_session_state(
    *,
    path: Path,
    state: dict[str, Any],
) -> None:
    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    state["updatedAt"] = now_iso()

    temporary_path = (
        path.with_suffix(
            path.suffix + ".tmp"
        )
    )

    temporary_path.write_text(
        json.dumps(
            state,
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    temporary_path.replace(
        path
    )


def save_json_atomic(
    *,
    path: Path,
    payload: dict[str, Any],
) -> None:
    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    temporary_path = (
        path.with_suffix(
            path.suffix + ".tmp"
        )
    )

    temporary_path.write_text(
        json.dumps(
            payload,
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    temporary_path.replace(
        path
    )


def get_cycle_result_path(
    *,
    state_path: Path,
    session_id: str,
    iteration: int,
) -> Path:
    exam_root = (
        state_path.parent.parent
    )

    return (
        exam_root
        / "continuous_results"
        / session_id
        / (
            f"iteration-"
            f"{iteration:06d}.json"
        )
    )


def get_candidate_path(
    *,
    state_path: Path,
    session_id: str,
    iteration: int,
) -> Path:
    exam_root = (
        state_path.parent.parent
    )

    return (
        exam_root
        / "continuous_candidates"
        / session_id
        / (
            f"candidate-"
            f"{iteration:06d}.json"
        )
    )


def load_session_state(
    *,
    path: Path,
) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(
            f"session file not found: {path}"
        )

    try:
        state = json.loads(
            path.read_text(
                encoding="utf-8"
            )
        )
    except json.JSONDecodeError as exc:
        raise ValueError(
            "session state is invalid JSON"
        ) from exc

    if not isinstance(
        state,
        dict,
    ):
        raise ValueError(
            "session state must be an object"
        )

    return state


def validate_resume_state(
    *,
    state: dict[str, Any],
    session_id: str,
    config: dict[str, Any],
) -> None:
    if state.get(
        "stateVersion"
    ) != SESSION_STATE_VERSION:
        raise ValueError(
            "unsupported session state version: "
            f'{state.get("stateVersion")}. '
            f"expected={SESSION_STATE_VERSION}"
        )

    if state.get(
        "sessionId"
    ) != session_id:
        raise ValueError(
            "sessionId does not match "
            "checkpoint"
        )

    expected = {
        "exam": config["exam"],
        "section": config["section"],
        "difficultyMin": (
            config["difficultyMin"]
        ),
        "difficultyMax": (
            config["difficultyMax"]
        ),
        "questionTypes": list(
            config["questionTypes"]
        ),
    }

    actual = {
        key: state.get(
            key
        )
        for key in expected
    }

    if actual != expected:
        raise ValueError(
            "resume configuration does "
            "not match checkpoint. "
            f"expected={expected}, "
            f"actual={actual}"
        )

    planner = state.get(
        "planner"
    )

    if not isinstance(
        planner,
        dict,
    ):
        raise ValueError(
            "checkpoint planner state "
            "is invalid"
        )


def prepare_resumed_session_state(
    *,
    state: dict[str, Any],
    session_id: str,
    config: dict[str, Any],
) -> dict[str, Any]:
    validate_resume_state(
        state=state,
        session_id=session_id,
        config=config,
    )

    state[
        "status"
    ] = "running"

    state[
        "lastEvent"
    ] = {
        "type": "session_resumed",
        "iteration": state.get(
            "iterationCount",
            0,
        ),
        "at": now_iso(),
    }

    return state


def load_session_comparison_records(
    *,
    state_path: Path,
    session_id: str,
) -> list[dict[str, Any]]:
    candidate_directory = (
        get_candidate_path(
            state_path=state_path,
            session_id=session_id,
            iteration=1,
        ).parent
    )

    if not candidate_directory.exists():
        return []

    records = []

    for candidate_path in sorted(
        candidate_directory.glob(
            "candidate-*.json"
        )
    ):
        try:
            payload = json.loads(
                candidate_path.read_text(
                    encoding="utf-8"
                )
            )
        except json.JSONDecodeError as exc:
            raise ValueError(
                "invalid candidate JSON: "
                f"{candidate_path}"
            ) from exc

        if not isinstance(
            payload,
            dict,
        ):
            raise ValueError(
                "candidate must be an object: "
                f"{candidate_path}"
            )

        if payload.get(
            "sessionId"
        ) != session_id:
            raise ValueError(
                "candidate sessionId mismatch: "
                f"{candidate_path}"
            )

        question = payload.get(
            "question"
        )

        if not isinstance(
            question,
            dict,
        ):
            raise ValueError(
                "candidate question missing: "
                f"{candidate_path}"
            )

        records.append(
            build_comparison_record(
                question=question,
                source="session",
                record_id=(
                    f"{session_id}:"
                    f"{candidate_path.stem}"
                ),
            )
        )

    return records


def create_session_state(
    *,
    session_id: str,
    config: dict[str, Any],
) -> dict[str, Any]:
    created_at = now_iso()

    return {
        "stateVersion": (
            SESSION_STATE_VERSION
        ),
        "sessionId": session_id,
        "status": "running",
        "exam": config["exam"],
        "section": config["section"],
        "difficultyMin": (
            config["difficultyMin"]
        ),
        "difficultyMax": (
            config["difficultyMax"]
        ),
        "questionTypes": list(
            config["questionTypes"]
        ),
        "autoPublish": False,
        "createdAt": created_at,
        "updatedAt": created_at,
        "iterationCount": 0,
        "plannedCount": 0,
        "generatedCount": 0,
        "approvedCount": 0,
        "reviewCount": 0,
        "rejectedCount": 0,
        "semanticDuplicateCount": 0,
        "semanticReviewCount": 0,
        "planner": create_planner_state(),
        "currentKnowledge": None,
        "currentQuestion": None,
        "lastEvent": {
            "type": "session_created",
            "at": created_at,
        },
    }


def run_continuous_session(
    *,
    state: dict[str, Any],
    state_path: Path,
    max_iterations: int | None,
    poll_seconds: float,
    allow_api: bool = False,
    max_attempts: int = 3,
    cycle_runner: Any = None,
    semantic_gate_runner: Any = None,
) -> dict[str, Any]:
    print(
        "SESSION START"
    )

    print(
        "session:",
        state["sessionId"],
    )

    print(
        "exam:",
        state["exam"],
    )

    print(
        "section:",
        state["section"],
    )

    print(
        "difficulty:",
        f'{state["difficultyMin"]}'
        f'-{state["difficultyMax"]}',
    )

    print(
        "question types:",
        state["questionTypes"],
    )

    print(
        "checkpoint:",
        state_path,
    )

    print()

    save_session_state(
        path=state_path,
        state=state,
    )

    try:
        knowledge_items = load_knowledge(
            state["exam"]
        )

        print(
            "Knowledge loaded:",
            len(knowledge_items),
        )

        print()

        if cycle_runner is None:
            cycle_runner = (
                run_webdesign_question_cycle
            )

        if semantic_gate_runner is None:
            semantic_gate_runner = (
                evaluate_webdesign_semantic_gate
            )

        app_comparison_records = []
        session_comparison_records = []

        if (
            allow_api
            and state["exam"]
            == "webdesign"
        ):
            app_questions = (
                load_webdesign_question_pool()
            )

            app_comparison_records = (
                build_app_comparison_records(
                    app_questions
                )
            )

            print(
                "Semantic app pool:",
                len(
                    app_comparison_records
                ),
            )

            session_comparison_records = (
                load_session_comparison_records(
                    state_path=state_path,
                    session_id=state[
                        "sessionId"
                    ],
                )
            )

            print(
                "Semantic session pool:",
                len(
                    session_comparison_records
                ),
            )

            print()

        while True:
            try:
                selected = select_next_knowledge(
                    knowledge_items,
                    section=state["section"],
                    planner_state=state[
                        "planner"
                    ],
                )

            except ValueError as exc:
                if (
                    "No plannable Knowledge found"
                    not in str(exc)
                ):
                    raise

                state[
                    "status"
                ] = "stopped"

                state[
                    "currentKnowledge"
                ] = None

                state[
                    "currentQuestion"
                ] = None

                state[
                    "lastEvent"
                ] = {
                    "type": (
                        "no_plannable_knowledge"
                    ),
                    "iteration": state[
                        "iterationCount"
                    ],
                    "at": now_iso(),
                }

                save_session_state(
                    path=state_path,
                    state=state,
                )

                print()
                print(
                    "SESSION STOP"
                )

                print(
                    "reason: "
                    "no plannable Knowledge"
                )

                return state

            state[
                "iterationCount"
            ] += 1

            iteration = state[
                "iterationCount"
            ]

            state[
                "planner"
            ] = record_knowledge_use(
                state["planner"],
                selected["id"],
            )

            state[
                "plannedCount"
            ] += 1

            state[
                "currentKnowledge"
            ] = {
                "id": selected["id"],
                "section": selected[
                    "section"
                ],
                "title": selected[
                    "title"
                ],
                "sourceQuestionNumbers": (
                    selected.get(
                        "sourceQuestionNumbers",
                        [],
                    )
                ),
            }

            state[
                "lastEvent"
            ] = {
                "type": (
                    "knowledge_selected"
                ),
                "iteration": iteration,
                "knowledgeId": (
                    selected["id"]
                ),
                "at": now_iso(),
            }

            save_session_state(
                path=state_path,
                state=state,
            )

            print(
                "[PLAN]",
                f"iteration={iteration}",
            )

            print(
                " knowledge:",
                selected["id"],
            )

            print(
                " title:",
                selected["title"],
            )

            if not allow_api:
                state[
                    "lastEvent"
                ] = {
                    "type": (
                        "generation_skipped_"
                        "api_disabled"
                    ),
                    "iteration": iteration,
                    "knowledgeId": (
                        selected["id"]
                    ),
                    "at": now_iso(),
                }

                save_session_state(
                    path=state_path,
                    state=state,
                )

                print(
                    " generation skipped: "
                    "API disabled"
                )

            else:
                if (
                    state["exam"]
                    != "webdesign"
                ):
                    state[
                        "status"
                    ] = "stopped"

                    state[
                        "lastEvent"
                    ] = {
                        "type": (
                            "unsupported_"
                            "generation_exam"
                        ),
                        "iteration": (
                            iteration
                        ),
                        "exam": state[
                            "exam"
                        ],
                        "at": now_iso(),
                    }

                    save_session_state(
                        path=state_path,
                        state=state,
                    )

                    print()
                    print(
                        "SESSION STOP"
                    )

                    print(
                        "reason: generation "
                        "currently supports "
                        "webdesign only"
                    )

                    return state

                question_types = (
                    state[
                        "questionTypes"
                    ]
                )

                if not question_types:
                    raise ValueError(
                        "questionTypes "
                        "must not be empty"
                    )

                question_type = (
                    question_types[
                        (
                            iteration - 1
                        )
                        % len(
                            question_types
                        )
                    ]
                )

                target_difficulty = (
                    select_target_difficulty(
                        state["planner"],
                        selected["id"],
                        difficulty_min=state[
                            "difficultyMin"
                        ],
                        difficulty_max=state[
                            "difficultyMax"
                        ],
                    )
                )

                print(
                    "[CYCLE]",
                    f"question_type="
                    f"{question_type}",
                    f"difficulty="
                    f"{target_difficulty}",
                )

                cycle_result = (
                    cycle_runner(
                        knowledge=selected,
                        section=state[
                            "section"
                        ],
                        difficulty_min=state[
                            "difficultyMin"
                        ],
                        difficulty_max=state[
                            "difficultyMax"
                        ],
                        target_difficulty=(
                            target_difficulty
                        ),
                        question_type=(
                            question_type
                        ),
                        max_attempts=(
                            max_attempts
                        ),
                        allow_api=True,
                        use_cache=False,
                    )
                )

                cycle_result_path = (
                    get_cycle_result_path(
                        state_path=state_path,
                        session_id=state[
                            "sessionId"
                        ],
                        iteration=iteration,
                    )
                )

                save_json_atomic(
                    path=cycle_result_path,
                    payload={
                        "sessionId": state[
                            "sessionId"
                        ],
                        "iteration": (
                            iteration
                        ),
                        "savedAt": now_iso(),
                        "result": (
                            cycle_result
                        ),
                    },
                )

                cycle_status = (
                    cycle_result.get(
                        "status"
                    )
                )

                if (
                    cycle_status
                    == "pass"
                ):
                    final_question = (
                        cycle_result[
                            "finalQuestion"
                        ]
                    )

                    final_review = (
                        cycle_result[
                            "finalReview"
                        ]
                    )

                    comparison_records = [
                        *app_comparison_records,
                        *session_comparison_records,
                    ]

                    semantic_result = (
                        semantic_gate_runner(
                            candidate=(
                                final_question
                            ),
                            comparison_records=(
                                comparison_records
                            ),
                            allow_api=True,
                        )
                    )

                    semantic_status = (
                        semantic_result.get(
                            "status"
                        )
                    )

                    save_json_atomic(
                        path=cycle_result_path,
                        payload={
                            "sessionId": state[
                                "sessionId"
                            ],
                            "iteration": (
                                iteration
                            ),
                            "savedAt": (
                                now_iso()
                            ),
                            "result": (
                                cycle_result
                            ),
                            "semanticGate": (
                                semantic_result
                            ),
                        },
                    )

                    if (
                        semantic_status
                        == "duplicate"
                    ):
                        state[
                            "planner"
                        ] = block_knowledge(
                            state[
                                "planner"
                            ],
                            selected["id"],
                        )

                        state[
                            "semanticDuplicateCount"
                        ] += 1

                        state[
                            "currentQuestion"
                        ] = None

                        state[
                            "lastEvent"
                        ] = {
                            "type": (
                                "semantic_duplicate_"
                                "blocked"
                            ),
                            "iteration": (
                                iteration
                            ),
                            "knowledgeId": (
                                selected["id"]
                            ),
                            "topMatch": (
                                semantic_result.get(
                                    "topMatch"
                                )
                            ),
                            "cycleResultPath": (
                                str(
                                    cycle_result_path
                                )
                            ),
                            "at": now_iso(),
                        }

                        print(
                            " semantic gate: "
                            "DUPLICATE"
                        )

                        top_match = (
                            semantic_result.get(
                                "topMatch"
                            )
                        )

                        if top_match:
                            print(
                                " top match:",
                                top_match.get(
                                    "id"
                                ),
                            )

                    elif (
                        semantic_status
                        in {
                            "pass",
                            "review",
                        }
                    ):
                        review_status = (
                            "semantic_review"
                            if semantic_status
                            == "review"
                            else "pending"
                        )

                        candidate_path = (
                            get_candidate_path(
                                state_path=(
                                    state_path
                                ),
                                session_id=state[
                                    "sessionId"
                                ],
                                iteration=(
                                    iteration
                                ),
                            )
                        )

                        candidate = {
                            "reviewStatus": (
                                review_status
                            ),
                            "sessionId": state[
                                "sessionId"
                            ],
                            "iteration": (
                                iteration
                            ),
                            "exam": state[
                                "exam"
                            ],
                            "section": state[
                                "section"
                            ],
                            "knowledgeId": (
                                selected["id"]
                            ),
                            "questionType": (
                                question_type
                            ),
                            "targetDifficulty": (
                                target_difficulty
                            ),
                            "attemptsUsed": (
                                cycle_result[
                                    "attemptsUsed"
                                ]
                            ),
                            "question": (
                                final_question
                            ),
                            "qualityReview": (
                                final_review
                            ),
                            "semanticGate": (
                                semantic_result
                            ),
                            "cycleResultPath": (
                                str(
                                    cycle_result_path
                                )
                            ),
                            "createdAt": (
                                now_iso()
                            ),
                        }

                        save_json_atomic(
                            path=candidate_path,
                            payload=candidate,
                        )

                        state[
                            "planner"
                        ] = record_difficulty_pass(
                            state["planner"],
                            selected["id"],
                            target_difficulty,
                        )

                        state[
                            "generatedCount"
                        ] += 1

                        state[
                            "reviewCount"
                        ] += 1

                        if (
                            semantic_status
                            == "review"
                        ):
                            state[
                                "semanticReviewCount"
                            ] += 1

                        state[
                            "currentQuestion"
                        ] = {
                            "reviewStatus": (
                                review_status
                            ),
                            "candidatePath": (
                                str(
                                    candidate_path
                                )
                            ),
                            "question": (
                                final_question
                            ),
                        }

                        record_id = (
                            f'{state["sessionId"]}:'
                            f'candidate-'
                            f'{iteration:06d}'
                        )

                        session_comparison_records.append(
                            build_comparison_record(
                                question=(
                                    final_question
                                ),
                                source="session",
                                record_id=(
                                    record_id
                                ),
                            )
                        )

                        event_type = (
                            "candidate_semantic_"
                            "review"
                            if semantic_status
                            == "review"
                            else
                            "candidate_pending_"
                            "review"
                        )

                        state[
                            "lastEvent"
                        ] = {
                            "type": event_type,
                            "iteration": (
                                iteration
                            ),
                            "knowledgeId": (
                                selected["id"]
                            ),
                            "candidatePath": (
                                str(
                                    candidate_path
                                )
                            ),
                            "cycleResultPath": (
                                str(
                                    cycle_result_path
                                )
                            ),
                            "semanticTopMatch": (
                                semantic_result.get(
                                    "topMatch"
                                )
                            ),
                            "at": now_iso(),
                        }

                        print(
                            " cycle result: PASS"
                        )

                        print(
                            " semantic gate:",
                            semantic_status.upper(),
                        )

                        print(
                            " candidate:",
                            candidate_path,
                        )

                    else:
                        raise ValueError(
                            "unsupported semantic "
                            "gate status: "
                            f"{semantic_status}"
                        )

                elif cycle_status in {
                    "rejected",
                    "exhausted",
                }:
                    if (
                        cycle_status
                        == "exhausted"
                    ):
                        block_reason = (
                            cycle_result.get(
                                "exhaustedReason",
                                "quality_exhausted",
                            )
                        )
                    else:
                        block_reason = (
                            "cycle_rejected"
                        )

                    is_difficulty_ceiling = (
                        cycle_status
                        == "exhausted"
                        and block_reason
                        == "knowledge_difficulty_ceiling"
                    )

                    ceiling_recorded = False

                    if is_difficulty_ceiling:
                        state[
                            "planner"
                        ] = record_difficulty_ceiling(
                            state["planner"],
                            selected["id"],
                            target_difficulty,
                            difficulty_min=state[
                                "difficultyMin"
                            ],
                        )

                        difficulty_record = (
                            state[
                                "planner"
                            ]
                            .get(
                                "knowledgeDifficulty",
                                {},
                            )
                            .get(
                                selected["id"],
                                {},
                            )
                        )

                        blocked_from = (
                            difficulty_record.get(
                                "blockedFrom"
                            )
                            if isinstance(
                                difficulty_record,
                                dict,
                            )
                            else None
                        )

                        ceiling_recorded = (
                            isinstance(
                                blocked_from,
                                int,
                            )
                            and blocked_from
                            <= target_difficulty
                        )

                    else:
                        state[
                            "planner"
                        ] = block_knowledge(
                            state["planner"],
                            selected["id"],
                        )

                    raw_blocked_ids = (
                        state[
                            "planner"
                        ].get(
                            "blockedKnowledgeIds",
                            [],
                        )
                    )

                    blocked_ids = (
                        raw_blocked_ids
                        if isinstance(
                            raw_blocked_ids,
                            list,
                        )
                        else []
                    )

                    knowledge_blocked = (
                        selected["id"]
                        in blocked_ids
                    )

                    if knowledge_blocked:
                        event_type = (
                            "knowledge_blocked"
                        )
                    elif ceiling_recorded:
                        event_type = (
                            "difficulty_ceiling_recorded"
                        )
                    else:
                        event_type = (
                            "difficulty_ceiling_ignored"
                        )

                    state[
                        "rejectedCount"
                    ] += 1

                    state[
                        "currentQuestion"
                    ] = None

                    state[
                        "lastEvent"
                    ] = {
                        "type": event_type,
                        "iteration": (
                            iteration
                        ),
                        "knowledgeId": (
                            selected["id"]
                        ),
                        "cycleStatus": (
                            cycle_status
                        ),
                        "targetDifficulty": (
                            target_difficulty
                        ),
                        "blockReason": (
                            block_reason
                        ),
                        "cycleResultPath": (
                            str(
                                cycle_result_path
                            )
                        ),
                        "at": now_iso(),
                    }

                    print(
                        " cycle result:",
                        cycle_status,
                    )

                    if knowledge_blocked:
                        print(
                            " Knowledge blocked:",
                            block_reason,
                        )
                    elif ceiling_recorded:
                        print(
                            " Difficulty ceiling "
                            "recorded:",
                            target_difficulty,
                        )

                        print(
                            " Knowledge remains "
                            "available below "
                            "difficulty",
                            target_difficulty,
                        )
                    else:
                        print(
                            " Difficulty ceiling "
                            "ignored:",
                            target_difficulty,
                        )

                        print(
                            " prior successful "
                            "difficulty result "
                            "preserved"
                        )

                else:
                    raise ValueError(
                        "unsupported cycle status: "
                        f"{cycle_status}"
                    )

                save_session_state(
                    path=state_path,
                    state=state,
                )

            if (
                max_iterations
                is not None
                and iteration
                >= max_iterations
            ):
                state[
                    "status"
                ] = "stopped"

                state[
                    "lastEvent"
                ] = {
                    "type": (
                        "max_iterations_reached"
                    ),
                    "iteration": iteration,
                    "at": now_iso(),
                }

                save_session_state(
                    path=state_path,
                    state=state,
                )

                print()
                print(
                    "SESSION STOP"
                )

                print(
                    "reason: "
                    "max iterations reached"
                )

                return state

            time.sleep(
                poll_seconds
            )

    except KeyboardInterrupt:
        state[
            "status"
        ] = "stopped"

        state[
            "lastEvent"
        ] = {
            "type": (
                "keyboard_interrupt"
            ),
            "iteration": state[
                "iterationCount"
            ],
            "at": now_iso(),
        }

        save_session_state(
            path=state_path,
            state=state,
        )

        print()
        print(
            "SESSION STOP"
        )

        print(
            "reason: keyboard interrupt"
        )

        print(
            "checkpoint saved:",
            state_path,
        )

        return state


def build_parser() -> (
    argparse.ArgumentParser
):
    parser = argparse.ArgumentParser(
        description=(
            "Continuously build Study QUEST "
            "questions until stopped."
        )
    )

    parser.add_argument(
        "--exam",
        required=True,
    )

    parser.add_argument(
        "--section",
        required=True,
    )

    parser.add_argument(
        "--difficulty-min",
        type=int,
        required=True,
    )

    parser.add_argument(
        "--difficulty-max",
        type=int,
        required=True,
    )

    parser.add_argument(
        "--question-types",
        default=None,
        help=(
            "Comma-separated question types. "
            "If omitted, all types defined "
            "by the exam profile are used."
        ),
    )

    parser.add_argument(
        "--session-id",
        default=None,
    )

    parser.add_argument(
        "--state-root",
        default=str(
            DEFAULT_STATE_ROOT
        ),
    )

    parser.add_argument(
        "--max-iterations",
        type=int,
        default=None,
        help=(
            "Testing option. "
            "Omit for an unlimited session."
        ),
    )

    parser.add_argument(
        "--poll-seconds",
        type=float,
        default=1.0,
    )

    parser.add_argument(
        "--max-attempts",
        type=int,
        default=3,
        help=(
            "Maximum generate-review "
            "attempts per Knowledge."
        ),
    )

    parser.add_argument(
        "--allow-api",
        action="store_true",
        help=(
            "Explicitly allow question "
            "generation API calls."
        ),
    )

    parser.add_argument(
        "--resume",
        action="store_true",
        help=(
            "Resume an existing session "
            "checkpoint. Requires "
            "--session-id."
        ),
    )

    return parser


def main() -> None:
    parser = build_parser()

    args = parser.parse_args()

    if (
        args.max_iterations
        is not None
        and args.max_iterations <= 0
    ):
        parser.error(
            "--max-iterations "
            "must be greater than zero"
        )

    if args.poll_seconds < 0:
        parser.error(
            "--poll-seconds "
            "must not be negative"
        )

    if args.max_attempts <= 0:
        parser.error(
            "--max-attempts "
            "must be greater than zero"
        )

    try:
        config = (
            validate_session_config(
                exam=args.exam,
                section=args.section,
                difficulty_min=(
                    args.difficulty_min
                ),
                difficulty_max=(
                    args.difficulty_max
                ),
                question_types=(
                    args.question_types
                ),
            )
        )
    except ValueError as exc:
        parser.error(
            str(exc)
        )

    if (
        args.resume
        and not args.session_id
    ):
        parser.error(
            "--resume requires "
            "--session-id"
        )

    session_id = (
        args.session_id
        or build_session_id()
    )

    state_root = Path(
        args.state_root
    )

    state_path = get_session_path(
        state_root=state_root,
        exam=config["exam"],
        session_id=session_id,
    )

    if args.resume:
        if not state_path.exists():
            parser.error(
                "session does not exist: "
                f"{state_path}"
            )

        try:
            state = load_session_state(
                path=state_path
            )

            state = (
                prepare_resumed_session_state(
                    state=state,
                    session_id=session_id,
                    config=config,
                )
            )
        except (
            FileNotFoundError,
            ValueError,
        ) as exc:
            parser.error(
                str(exc)
            )

        save_session_state(
            path=state_path,
            state=state,
        )

        print(
            "RESUMING SESSION"
        )

        print(
            "iteration:",
            state[
                "iterationCount"
            ],
        )

    else:
        if state_path.exists():
            parser.error(
                "session already exists: "
                f"{state_path}"
            )

        state = create_session_state(
            session_id=session_id,
            config=config,
        )

    run_continuous_session(
        state=state,
        state_path=state_path,
        max_iterations=(
            args.max_iterations
        ),
        poll_seconds=(
            args.poll_seconds
        ),
        allow_api=(
            args.allow_api
        ),
        max_attempts=(
            args.max_attempts
        ),
    )


if __name__ == "__main__":
    main()
