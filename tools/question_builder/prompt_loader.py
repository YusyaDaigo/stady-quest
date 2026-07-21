from pathlib import Path
from typing import Any, Dict


TEMPLATE_DIR = Path(__file__).resolve().parent / "templates"


def load_prompt_template(
    template_name: str,
) -> str:
    """
    templatesディレクトリからMarkdownテンプレートを読み込む。

    Example:
        load_prompt_template("pharmacy_similar")
    """

    if not isinstance(template_name, str):
        raise ValueError(
            "template_name must be a string"
        )

    normalized_name = template_name.strip()

    if not normalized_name:
        raise ValueError(
            "template_name must not be empty"
        )

    if any(
        token in normalized_name
        for token in ("/", "\\", "..")
    ):
        raise ValueError(
            "template_name contains invalid characters"
        )

    template_path = (
        TEMPLATE_DIR
        / f"{normalized_name}.md"
    )

    if not template_path.exists():
        raise FileNotFoundError(
            f"Prompt template was not found: "
            f"{template_path}"
        )

    template = template_path.read_text(
        encoding="utf-8"
    ).strip()

    if not template:
        raise ValueError(
            f"Prompt template is empty: "
            f"{template_path}"
        )

    return template


def render_prompt_template(
    template_name: str,
    variables: Dict[str, Any],
) -> str:
    """
    Markdownテンプレート内の
    {{VARIABLE_NAME}} を置換して返す。
    """

    if not isinstance(variables, dict):
        raise ValueError(
            "variables must be a dictionary"
        )

    rendered = load_prompt_template(
        template_name
    )

    for key, value in variables.items():
        placeholder = (
            "{{"
            + str(key)
            + "}}"
        )

        rendered = rendered.replace(
            placeholder,
            str(value),
        )

    if "{{" in rendered or "}}" in rendered:
        raise ValueError(
            "Unresolved placeholder remains "
            f"in template: {template_name}"
        )

    return rendered.strip()
