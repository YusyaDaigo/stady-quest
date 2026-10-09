from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path
from typing import Any


ROOT_DIR = Path(
    __file__
).resolve().parents[2]

DEFAULT_THEORY_PATH = (
    ROOT_DIR
    / "src"
    / "exams"
    / "webdesign"
    / "questions"
    / "theory.js"
)

DEFAULT_CATEGORIES_PATH = (
    ROOT_DIR
    / "src"
    / "exams"
    / "webdesign"
    / "questions"
    / "categories.js"
)


def validate_webdesign_question_pool(
    questions: list[dict[str, Any]],
) -> None:
    if not isinstance(
        questions,
        list,
    ):
        raise ValueError(
            "WebDesign question pool "
            "must be an array"
        )

    seen_ids: set[str] = set()

    for index, question in enumerate(
        questions,
        start=1,
    ):
        if not isinstance(
            question,
            dict,
        ):
            raise ValueError(
                "WebDesign question pool "
                f"item {index} must be an object"
            )

        question_id = str(
            question.get(
                "id",
                "",
            )
        ).strip()

        if not question_id:
            raise ValueError(
                f"question {index} requires id"
            )

        if question_id in seen_ids:
            raise ValueError(
                "duplicate WebDesign question id: "
                f"{question_id}"
            )

        seen_ids.add(
            question_id
        )

        if (
            question.get(
                "subject"
            )
            != "webdesign"
        ):
            raise ValueError(
                "unexpected subject for "
                f"{question_id}"
            )

        question_text = str(
            question.get(
                "question",
                "",
            )
        ).strip()

        if not question_text:
            raise ValueError(
                f"{question_id} requires question"
            )

        choices = question.get(
            "choices"
        )

        if (
            not isinstance(
                choices,
                list,
            )
            or len(choices) < 2
            or any(
                not isinstance(
                    choice,
                    str,
                )
                or not choice.strip()
                for choice in choices
            )
        ):
            raise ValueError(
                f"{question_id} has invalid choices"
            )

        answer = question.get(
            "answer"
        )

        if (
            not isinstance(
                answer,
                int,
            )
            or not 0
            <= answer
            < len(choices)
        ):
            raise ValueError(
                f"{question_id} has invalid answer"
            )

        explanation = str(
            question.get(
                "explanation",
                "",
            )
        ).strip()

        if not explanation:
            raise ValueError(
                f"{question_id} "
                "requires explanation"
            )


def load_webdesign_question_pool(
    *,
    theory_path: Path = (
        DEFAULT_THEORY_PATH
    ),
    categories_path: Path = (
        DEFAULT_CATEGORIES_PATH
    ),
) -> list[dict[str, Any]]:
    theory_path = Path(
        theory_path
    )

    categories_path = Path(
        categories_path
    )

    if not theory_path.is_file():
        raise FileNotFoundError(
            f"theory file not found: "
            f"{theory_path}"
        )

    if not categories_path.is_file():
        raise FileNotFoundError(
            f"categories file not found: "
            f"{categories_path}"
        )

    theory_text = theory_path.read_text(
        encoding="utf-8"
    )

    categories_text = (
        categories_path.read_text(
            encoding="utf-8"
        )
    )

    import_marker = (
        'from "./categories";'
    )

    if theory_text.count(
        import_marker
    ) != 1:
        raise ValueError(
            "Expected exactly one "
            "./categories import in theory.js"
        )

    theory_module = theory_text.replace(
        import_marker,
        'from "./categories.mjs";',
        1,
    )

    runner_text = """
import {
  theoryQuestions
} from "./theory.mjs";

process.stdout.write(
  JSON.stringify(theoryQuestions)
);
""".strip()

    with tempfile.TemporaryDirectory(
        prefix=(
            "study-quest-"
            "webdesign-pool-"
        )
    ) as temporary_directory:
        temporary_path = Path(
            temporary_directory
        )

        (
            temporary_path
            / "categories.mjs"
        ).write_text(
            categories_text,
            encoding="utf-8",
        )

        (
            temporary_path
            / "theory.mjs"
        ).write_text(
            theory_module,
            encoding="utf-8",
        )

        runner_path = (
            temporary_path
            / "runner.mjs"
        )

        runner_path.write_text(
            runner_text + "\n",
            encoding="utf-8",
        )

        completed = subprocess.run(
            [
                "node",
                str(
                    runner_path
                ),
            ],
            cwd=temporary_path,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )

    if completed.returncode != 0:
        raise RuntimeError(
            "Failed to load WebDesign "
            "question pool with Node:\n"
            + completed.stderr.strip()
        )

    stdout = completed.stdout.strip()

    if not stdout:
        raise RuntimeError(
            "Node returned empty "
            "WebDesign question pool"
        )

    try:
        questions = json.loads(
            stdout
        )
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            "Node returned invalid JSON "
            "for WebDesign question pool"
        ) from exc

    validate_webdesign_question_pool(
        questions
    )

    return questions
