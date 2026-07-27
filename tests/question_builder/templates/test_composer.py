from pathlib import Path

import pytest

from tools.question_builder.templates.engine.composer import (
    compose_prompt,
)


def write_template(
    path: Path,
    content: str,
) -> Path:
    path.write_text(
        content,
        encoding="utf-8",
    )
    return path


def test_compose_prompt_combines_files_in_order(
    tmp_path: Path,
):
    system_path = write_template(
        tmp_path / "system.md",
        "# System",
    )
    output_path = write_template(
        tmp_path / "output.md",
        "# Output",
    )
    task_path = write_template(
        tmp_path / "task.md",
        "# Task",
    )

    result = compose_prompt(
        partial_paths=[
            system_path,
            output_path,
        ],
        template_path=task_path,
        variables={},
    )

    assert result == (
        "# System\n\n"
        "# Output\n\n"
        "# Task"
    )


def test_compose_prompt_renders_variables(
    tmp_path: Path,
):
    system_path = write_template(
        tmp_path / "system.md",
        "Exam: {{EXAM}}",
    )
    task_path = write_template(
        tmp_path / "task.md",
        "Count: {{COUNT}}",
    )

    result = compose_prompt(
        partial_paths=[system_path],
        template_path=task_path,
        variables={
            "EXAM": "pharmacy",
            "COUNT": 10,
        },
    )

    assert result == (
        "Exam: pharmacy\n\n"
        "Count: 10"
    )


def test_compose_prompt_rejects_unresolved_variable(
    tmp_path: Path,
):
    task_path = write_template(
        tmp_path / "task.md",
        "{{QUESTION}} {{ANSWER}}",
    )

    with pytest.raises(
        ValueError,
        match="Unresolved template variables",
    ):
        compose_prompt(
            template_path=task_path,
            variables={
                "QUESTION": "question",
            },
        )


def test_compose_prompt_rejects_missing_partial(
    tmp_path: Path,
):
    task_path = write_template(
        tmp_path / "task.md",
        "task",
    )

    with pytest.raises(FileNotFoundError):
        compose_prompt(
            partial_paths=[
                tmp_path / "missing.md",
            ],
            template_path=task_path,
            variables={},
        )


def test_compose_prompt_rejects_missing_main_template(
    tmp_path: Path,
):
    with pytest.raises(FileNotFoundError):
        compose_prompt(
            template_path=tmp_path / "missing.md",
            variables={},
        )


def test_compose_prompt_skips_empty_sections(
    tmp_path: Path,
):
    empty_path = write_template(
        tmp_path / "empty.md",
        "",
    )
    task_path = write_template(
        tmp_path / "task.md",
        "Task",
    )

    result = compose_prompt(
        partial_paths=[empty_path],
        template_path=task_path,
        variables={},
    )

    assert result == "Task"


def test_compose_prompt_rejects_completely_empty_prompt(
    tmp_path: Path,
):
    task_path = write_template(
        tmp_path / "task.md",
        "   \n",
    )

    with pytest.raises(
        ValueError,
        match="Composed prompt must not be empty",
    ):
        compose_prompt(
            template_path=task_path,
            variables={},
        )


def test_compose_prompt_supports_custom_separator(
    tmp_path: Path,
):
    partial_path = write_template(
        tmp_path / "partial.md",
        "A",
    )
    task_path = write_template(
        tmp_path / "task.md",
        "B",
    )

    result = compose_prompt(
        partial_paths=[partial_path],
        template_path=task_path,
        variables={},
        separator="\n---\n",
    )

    assert result == "A\n---\nB"


def test_compose_prompt_rejects_non_string_separator(
    tmp_path: Path,
):
    task_path = write_template(
        tmp_path / "task.md",
        "Task",
    )

    with pytest.raises(
        TypeError,
        match="separator must be a string",
    ):
        compose_prompt(
            template_path=task_path,
            variables={},
            separator=None,
        )
