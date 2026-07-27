import pytest

from tools.question_builder.templates.engine.renderer import (
    render_template,
)


def test_render_template_replaces_variable():
    result = render_template(
        "Question: {{QUESTION}}",
        {"QUESTION": "薬理問題"},
    )

    assert result == "Question: 薬理問題"


def test_render_template_replaces_spaced_variable():
    result = render_template(
        "Question: {{ QUESTION }}",
        {"QUESTION": "薬理問題"},
    )

    assert result == "Question: 薬理問題"


def test_render_template_replaces_same_variable_multiple_times():
    result = render_template(
        "{{VALUE}} / {{VALUE}}",
        {"VALUE": 10},
    )

    assert result == "10 / 10"


def test_render_template_replaces_multiple_variables():
    result = render_template(
        "{{EXAM}}: {{COUNT}} questions",
        {
            "EXAM": "pharmacy",
            "COUNT": 10,
        },
    )

    assert result == "pharmacy: 10 questions"


def test_render_template_leaves_unknown_variable():
    result = render_template(
        "{{KNOWN}} {{UNKNOWN}}",
        {"KNOWN": "ok"},
    )

    assert result == "ok {{UNKNOWN}}"


def test_render_template_ignores_unused_variables():
    result = render_template(
        "{{USED}}",
        {
            "USED": "yes",
            "UNUSED": "no",
        },
    )

    assert result == "yes"


def test_render_template_rejects_non_string_template():
    with pytest.raises(
        TypeError,
        match="template must be a string",
    ):
        render_template(
            None,
            {},
        )


def test_render_template_rejects_non_mapping_variables():
    with pytest.raises(
        TypeError,
        match="variables must be a mapping",
    ):
        render_template(
            "{{VALUE}}",
            [],
        )
