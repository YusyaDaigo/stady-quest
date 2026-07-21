from pathlib import Path
from typing import Any, Dict, Optional

from .flowchart import render_flowchart_svg
from .graph import (
    render_bar_chart_svg,
    render_line_chart_svg,
)
from .schema import validate_figure_spec
from .table import render_table_svg


def render_figure(
    figure_type: str,
    figure_data: Optional[Dict[str, Any]],
    output_path: str,
) -> Optional[str]:
    """
    Study QUEST Diagram Engine の共通エントリーポイント。
    """

    validate_figure_spec(
        figure_type=figure_type,
        figure_data=figure_data,
    )

    if figure_type == "none":
        return None

    output = Path(output_path)

    if output.suffix.lower() not in {".svg", ".png"}:
        raise ValueError(
            "output_path must end with '.svg' or '.png'"
        )

    output.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    if output.suffix.lower() != ".svg":
        raise ValueError(
            "PNG output is not implemented yet. "
            "Use an '.svg' output path for now."
        )

    if figure_type == "table":
        svg = render_table_svg(
            figure_data
        )

    elif figure_type == "line_chart":
        svg = render_line_chart_svg(
            figure_data
        )

    elif figure_type == "bar_chart":
        svg = render_bar_chart_svg(
            figure_data
        )

    elif figure_type == "flowchart":
        svg = render_flowchart_svg(
            figure_data
        )

    else:
        raise NotImplementedError(
            f"Renderer for figure_type "
            f"'{figure_type}' is not implemented yet."
        )

    output.write_text(
        svg,
        encoding="utf-8",
    )

    return str(output)
