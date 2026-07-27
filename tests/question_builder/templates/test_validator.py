import pytest

from tools.question_builder.templates.engine.validator import (
    find_unresolved_variables,
    validate_rendered_template,
)


def test_find_unresolved_variables_returns_empty_list():
    assert find_unresolved_variables(
        "completed prompt"
    ) == []


def test_find_unresolved_variables_returns_sorted_unique_names():
    result = find_unresolved_variables(
        "{{B}} {{A}} {{B}}"
    )

    assert result == ["A", "B"]


def test_find_unresolved_variables_supports_spaces():
    result = find_unresolved_variables(
        "{{ QUESTION }}"
    )

    assert result == ["QUESTION"]


def test_validate_rendered_template_accepts_complete_prompt():
    validate_rendered_template(
        "No unresolved variables"
    )


def test_validate_rendered_template_rejects_unresolved_variables():
    with pytest.raises(
        ValueError,
        match=(
            "Unresolved template variables: "
            "ANSWER, QUESTION"
        ),
    ):
        validate_rendered_template(
            "{{QUESTION}} {{ANSWER}}"
        )


def test_find_unresolved_variables_rejects_non_string():
    with pytest.raises(
        TypeError,
        match="rendered must be a string",
    ):
        find_unresolved_variables(None)
