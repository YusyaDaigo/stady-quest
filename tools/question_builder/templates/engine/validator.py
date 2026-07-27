import re
from typing import List


_VARIABLE_PATTERN = re.compile(
    r"\{\{\s*([A-Za-z_][A-Za-z0-9_]*)\s*\}\}"
)


def find_unresolved_variables(rendered: str) -> List[str]:
    """
    未置換のテンプレート変数を重複なしで返す。
    """

    if not isinstance(rendered, str):
        raise TypeError("rendered must be a string")

    return sorted(
        set(_VARIABLE_PATTERN.findall(rendered))
    )


def validate_rendered_template(
    rendered: str,
) -> None:
    """
    未置換変数が残っていないことを検証する。
    """

    unresolved = find_unresolved_variables(rendered)

    if unresolved:
        raise ValueError(
            "Unresolved template variables: "
            + ", ".join(unresolved)
        )
