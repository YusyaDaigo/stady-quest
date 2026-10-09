from __future__ import annotations

import argparse
import json
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tools.question_builder.continuous_planner import (
    create_planner_state,
    record_knowledge_use,
    select_next_knowledge,
)
from tools.question_builder.exam_generation_profiles import (
    get_exam_generation_profile,
)
from tools.question_builder.knowledge.loader import (
    load_knowledge,
)


SESSION_STATE_VERSION = 2

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

        while True:
            state[
                "iterationCount"
            ] += 1

            iteration = state[
                "iterationCount"
            ]

            selected = select_next_knowledge(
                knowledge_items,
                section=state["section"],
                planner_state=state[
                    "planner"
                ],
            )

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

            event_time = now_iso()

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
                "at": event_time,
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

            print(
                " generation stage "
                "not connected yet",
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
    )


if __name__ == "__main__":
    main()
