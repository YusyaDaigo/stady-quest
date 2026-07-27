import re
from typing import Any, Mapping


_VARIABLE_PATTERN = re.compile(
    r"\{\{\s*([A-Za-z_][A-Za-z0-9_]*)\s*\}\}"
)


def render_template(
    template: str,
    variables: Mapping[str, Any],
) -> str:
    """
    テンプレート内の変数を置換する。

    渡されなかった変数は置換せずに残し、
    後続のValidatorで検出する。
    """

    if not isinstance(template, str):
        raise TypeError("template must be a string")

    if not isinstance(variables, Mapping):
        raise TypeError("variables must be a mapping")

    def replace(match: re.Match) -> str:
        variable_name = match.group(1)

        if variable_name not in variables:
            return match.group(0)

        return str(variables[variable_name])

    return _VARIABLE_PATTERN.sub(replace, template)
