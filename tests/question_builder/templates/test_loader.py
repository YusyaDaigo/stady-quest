from pathlib import Path

import pytest

from tools.question_builder.templates.engine.loader import (
    load_template,
)


def test_load_template_reads_utf8_file(
    tmp_path: Path,
):
    path = tmp_path / "template.md"
    path.write_text(
        "日本語テンプレート",
        encoding="utf-8",
    )

    assert load_template(path) == "日本語テンプレート"


def test_load_template_accepts_string_path(
    tmp_path: Path,
):
    path = tmp_path / "template.md"
    path.write_text("content", encoding="utf-8")

    assert load_template(str(path)) == "content"


def test_load_template_rejects_missing_file(
    tmp_path: Path,
):
    with pytest.raises(
        FileNotFoundError,
        match="Template file not found",
    ):
        load_template(tmp_path / "missing.md")


def test_load_template_rejects_directory(
    tmp_path: Path,
):
    with pytest.raises(
        ValueError,
        match="Template path is not a file",
    ):
        load_template(tmp_path)
