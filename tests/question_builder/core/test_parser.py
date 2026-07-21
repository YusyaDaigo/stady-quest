import pytest

from tools.question_builder.core.parser import (
    parse_json_array,
    parse_json_object,
    parse_json_response,
    strip_code_fence,
)


def test_strip_json_code_fence():
    response = """```json
{"question": "test"}
```"""

    assert strip_code_fence(response) == '{"question": "test"}'


def test_strip_plain_code_fence():
    response = """```
[{"question": "test"}]
```"""

    assert strip_code_fence(response) == '[{"question": "test"}]'


def test_strip_code_fence_preserves_plain_json():
    response = '{"question": "test"}'

    assert strip_code_fence(response) == response


def test_strip_code_fence_rejects_empty_response():
    with pytest.raises(
        ValueError,
        match="AI response is empty",
    ):
        strip_code_fence("   ")


def test_strip_code_fence_rejects_non_string():
    with pytest.raises(
        ValueError,
        match="response_text must be a string",
    ):
        strip_code_fence(None)


def test_parse_json_response_rejects_invalid_json():
    with pytest.raises(
        ValueError,
        match="AI response is not valid JSON",
    ):
        parse_json_response("{invalid json}")


def test_parse_json_object_returns_dictionary():
    result = parse_json_object(
        '{"question": "test"}'
    )

    assert result == {
        "question": "test",
    }


def test_parse_json_object_rejects_array():
    with pytest.raises(
        ValueError,
        match="JSON must be an object",
    ):
        parse_json_object("[]")


def test_parse_json_array_returns_object_list():
    result = parse_json_array(
        '[{"id": 1}, {"id": 2}]',
        expected_count=2,
    )

    assert result == [
        {"id": 1},
        {"id": 2},
    ]


def test_parse_json_array_rejects_object_root():
    with pytest.raises(
        ValueError,
        match="JSON must be an array",
    ):
        parse_json_array("{}")


def test_parse_json_array_rejects_wrong_count():
    with pytest.raises(
        ValueError,
        match="Generated item count does not match",
    ):
        parse_json_array(
            '[{"id": 1}]',
            expected_count=2,
        )


def test_parse_json_array_rejects_non_object_items():
    with pytest.raises(
        ValueError,
        match="only JSON objects",
    ):
        parse_json_array(
            '[{"id": 1}, "invalid"]'
        )


@pytest.mark.parametrize(
    "expected_count",
    [
        0,
        -1,
    ],
)
def test_parse_json_array_rejects_invalid_expected_count(
    expected_count,
):
    with pytest.raises(
        ValueError,
        match="expected_count must be at least 1",
    ):
        parse_json_array(
            "[]",
            expected_count=expected_count,
        )


def test_parse_json_array_rejects_non_integer_count():
    with pytest.raises(
        ValueError,
        match="expected_count must be an integer",
    ):
        parse_json_array(
            "[]",
            expected_count="2",
        )
