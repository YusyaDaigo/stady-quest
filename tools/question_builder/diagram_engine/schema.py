from typing import Any, Dict, Optional


SUPPORTED_FIGURE_TYPES = {
    "none",
    "table",
    "line_chart",
    "bar_chart",
    "flowchart",
}


def validate_figure_spec(
    figure_type: str,
    figure_data: Optional[Dict[str, Any]],
) -> None:
    """
    Diagram Engine v1 の共通入力仕様を検証する。

    この関数は描画前の入口で使う。
    各描画モジュール側では、より詳細な検証を行う。
    """

    if figure_type not in SUPPORTED_FIGURE_TYPES:
        raise ValueError(
            f"Unsupported figure_type: {figure_type}. "
            f"Supported types: {sorted(SUPPORTED_FIGURE_TYPES)}"
        )

    if figure_type == "none":
        if figure_data not in (None, {}):
            raise ValueError(
                "figure_data must be None or {} "
                "when figure_type is 'none'"
            )

        return

    if not isinstance(figure_data, dict):
        raise ValueError(
            f"figure_data must be an object "
            f"when figure_type is '{figure_type}'"
        )

    if not figure_data:
        raise ValueError(
            f"figure_data must not be empty "
            f"when figure_type is '{figure_type}'"
        )


def build_figure_spec(
    figure_type: str,
    figure_data: Optional[Dict[str, Any]],
) -> Dict[str, Any]:
    """
    検証済みの共通figure仕様を返す。
    """

    validate_figure_spec(
        figure_type=figure_type,
        figure_data=figure_data,
    )

    return {
        "figureType": figure_type,
        "figureData": figure_data,
    }
