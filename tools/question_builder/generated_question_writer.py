import json
from pathlib import Path
from typing import Any, Dict, List


def _to_js_value(
    value: Any,
    indent: int = 0,
) -> str:
    """
    Python値をJavaScriptリテラルへ変換する。
    """

    if value is None:
        return "null"

    if isinstance(value, bool):
        return (
            "true"
            if value
            else "false"
        )

    if isinstance(
        value,
        (int, float),
    ):
        return str(value)

    if isinstance(value, str):
        return json.dumps(
            value,
            ensure_ascii=False,
        )

    if isinstance(value, list):
        if not value:
            return "[]"

        item_indent = " " * (
            indent + 2
        )

        items = [
            (
                item_indent
                + _to_js_value(
                    item,
                    indent + 2,
                )
            )
            for item in value
        ]

        return (
            "[\n"
            + ",\n".join(items)
            + "\n"
            + " " * indent
            + "]"
        )

    if isinstance(value, dict):
        if not value:
            return "{}"

        item_indent = " " * (
            indent + 2
        )

        items = []

        for key, item in value.items():
            js_key = (
                key
                if key.isidentifier()
                else json.dumps(
                    key,
                    ensure_ascii=False,
                )
            )

            items.append(
                item_indent
                + f"{js_key}: "
                + _to_js_value(
                    item,
                    indent + 2,
                )
            )

        return (
            "{\n"
            + ",\n".join(items)
            + "\n"
            + " " * indent
            + "}"
        )

    raise TypeError(
        f"Unsupported value type: {type(value)}"
    )


def write_generated_questions_js(
    questions: List[Dict[str, Any]],
    output_path: str,
    export_name: str,
) -> str:
    """
    Study QUEST形式の問題一覧を
    JavaScriptファイルとして書き出す。
    """

    if not isinstance(
        questions,
        list,
    ):
        raise ValueError(
            "questions must be a list"
        )

    path = Path(
        output_path
    )

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    question_blocks = [
        _to_js_value(
            question,
            indent=2,
        )
        for question in questions
    ]

    content = (
        'import { CATEGORIES } from "./categories";\n\n'
        f"export const {export_name} = [\n"
    )

    if question_blocks:
        content += (
            ",\n".join(
                (
                    "  "
                    + block.replace(
                        "\n",
                        "\n  ",
                    )
                )
                for block in question_blocks
            )
            + "\n"
        )

    content += "];\n"

    # categoryだけはJS定数へ置換
    content = content.replace(
        '"REQUIRED"',
        "CATEGORIES.REQUIRED",
    )

    path.write_text(
        content,
        encoding="utf-8",
    )

    return str(path)
