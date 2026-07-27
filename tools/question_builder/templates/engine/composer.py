from pathlib import Path
from typing import Any, Mapping, Sequence, Union

from tools.question_builder.templates.engine.loader import (
    load_template,
)
from tools.question_builder.templates.engine.renderer import (
    render_template,
)
from tools.question_builder.templates.engine.validator import (
    validate_rendered_template,
)


PathLike = Union[str, Path]


def compose_prompt(
    *,
    template_path: PathLike,
    variables: Mapping[str, Any],
    partial_paths: Sequence[PathLike] = (),
    separator: str = "\n\n",
) -> str:
    """
    Partialとメインテンプレートを結合し、
    変数置換と未置換変数検証を行う。

    結合順:
        partial_paths
        ↓
        template_path
    """

    if not isinstance(separator, str):
        raise TypeError("separator must be a string")

    paths = [
        *partial_paths,
        template_path,
    ]

    sections = []

    for path in paths:
        content = load_template(path).strip()

        if content:
            sections.append(content)

    if not sections:
        raise ValueError(
            "Composed prompt must not be empty"
        )

    combined = separator.join(sections)

    rendered = render_template(
        combined,
        variables,
    )

    validate_rendered_template(rendered)

    return rendered
