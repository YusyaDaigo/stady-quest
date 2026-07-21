from html import escape
from typing import Any, Dict, List, Tuple


def _validate_series(
    figure_data: Dict[str, Any],
) -> List[Dict[str, Any]]:
    series = figure_data.get("series", [])

    if not isinstance(series, list) or not series:
        raise ValueError(
            "graph figureData requires a non-empty 'series' list"
        )

    normalized_series = []

    for series_index, item in enumerate(series):
        if not isinstance(item, dict):
            raise ValueError(
                f"series {series_index} must be an object"
            )

        label = str(
            item.get("label", f"Series {series_index + 1}")
        )

        points = item.get("points", [])

        if not isinstance(points, list) or not points:
            raise ValueError(
                f"series {series_index} requires "
                "a non-empty 'points' list"
            )

        normalized_points: List[Tuple[float, float]] = []

        for point_index, point in enumerate(points):
            if (
                not isinstance(point, list)
                or len(point) != 2
            ):
                raise ValueError(
                    f"series {series_index} point "
                    f"{point_index} must be [x, y]"
                )

            try:
                x = float(point[0])
                y = float(point[1])
            except (TypeError, ValueError) as exc:
                raise ValueError(
                    f"series {series_index} point "
                    f"{point_index} must contain numbers"
                ) from exc

            normalized_points.append((x, y))

        normalized_series.append(
            {
                "label": label,
                "points": normalized_points,
            }
        )

    return normalized_series


def _scale_value(
    value: float,
    source_min: float,
    source_max: float,
    target_min: float,
    target_max: float,
) -> float:
    if source_max == source_min:
        return (target_min + target_max) / 2

    ratio = (
        (value - source_min)
        / (source_max - source_min)
    )

    return (
        target_min
        + ratio * (target_max - target_min)
    )


def render_line_chart_svg(
    figure_data: Dict[str, Any],
) -> str:
    """
    折れ線グラフのSVGを生成する。
    """

    title = str(
        figure_data.get("title", "")
    ).strip()

    x_label = str(
        figure_data.get("xLabel", "")
    ).strip()

    y_label = str(
        figure_data.get("yLabel", "")
    ).strip()

    series = _validate_series(figure_data)

    all_points = [
        point
        for item in series
        for point in item["points"]
    ]

    x_values = [point[0] for point in all_points]
    y_values = [point[1] for point in all_points]

    x_min = min(x_values)
    x_max = max(x_values)

    y_min = min(0.0, min(y_values))
    y_max = max(y_values)

    if y_min == y_max:
        y_max = y_min + 1

    width = 760
    height = 520

    margin_left = 100
    margin_right = 50
    margin_top = 80
    margin_bottom = 90

    plot_left = margin_left
    plot_right = width - margin_right
    plot_top = margin_top
    plot_bottom = height - margin_bottom

    plot_width = plot_right - plot_left
    plot_height = plot_bottom - plot_top

    parts = [
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}">'
        ),
        "<style>",
        (
            "text { "
            "font-family: -apple-system, BlinkMacSystemFont, "
            "'Hiragino Sans', 'Yu Gothic', sans-serif; "
            "fill: #111; "
            "}"
        ),
        ".title { font-size: 24px; font-weight: 700; }",
        ".axis-label { font-size: 17px; font-weight: 600; }",
        ".tick { font-size: 14px; }",
        ".legend { font-size: 14px; }",
        "</style>",
        f'<rect width="{width}" height="{height}" fill="white"/>',
    ]

    if title:
        parts.append(
            f'<text x="{width / 2}" y="38" '
            f'text-anchor="middle" class="title">'
            f'{escape(title)}</text>'
        )

    # 軸
    parts.extend(
        [
            (
                f'<line x1="{plot_left}" y1="{plot_bottom}" '
                f'x2="{plot_right}" y2="{plot_bottom}" '
                f'stroke="#222" stroke-width="2"/>'
            ),
            (
                f'<line x1="{plot_left}" y1="{plot_top}" '
                f'x2="{plot_left}" y2="{plot_bottom}" '
                f'stroke="#222" stroke-width="2"/>'
            ),
        ]
    )

    tick_count = 5

    # X軸目盛
    for i in range(tick_count + 1):
        ratio = i / tick_count

        x = plot_left + ratio * plot_width
        value = x_min + ratio * (x_max - x_min)

        parts.append(
            f'<line x1="{x}" y1="{plot_bottom}" '
            f'x2="{x}" y2="{plot_bottom + 6}" '
            f'stroke="#222"/>'
        )

        parts.append(
            f'<text x="{x}" y="{plot_bottom + 25}" '
            f'text-anchor="middle" class="tick">'
            f'{value:g}</text>'
        )

    # Y軸目盛と補助線
    for i in range(tick_count + 1):
        ratio = i / tick_count

        y = plot_bottom - ratio * plot_height
        value = y_min + ratio * (y_max - y_min)

        parts.append(
            f'<line x1="{plot_left - 6}" y1="{y}" '
            f'x2="{plot_left}" y2="{y}" '
            f'stroke="#222"/>'
        )

        parts.append(
            f'<line x1="{plot_left}" y1="{y}" '
            f'x2="{plot_right}" y2="{y}" '
            f'stroke="#dddddd" stroke-width="1"/>'
        )

        parts.append(
            f'<text x="{plot_left - 12}" y="{y + 5}" '
            f'text-anchor="end" class="tick">'
            f'{value:g}</text>'
        )

    # 軸ラベル
    if x_label:
        parts.append(
            f'<text x="{plot_left + plot_width / 2}" '
            f'y="{height - 25}" '
            f'text-anchor="middle" class="axis-label">'
            f'{escape(x_label)}</text>'
        )

    if y_label:
        parts.append(
            f'<text x="25" '
            f'y="{plot_top + plot_height / 2}" '
            f'text-anchor="middle" '
            f'transform="rotate(-90 25 '
            f'{plot_top + plot_height / 2})" '
            f'class="axis-label">'
            f'{escape(y_label)}</text>'
        )

    # 系列描画
    dash_patterns = [
        "",
        ' stroke-dasharray="10 6"',
        ' stroke-dasharray="3 5"',
    ]

    for series_index, item in enumerate(series):
        scaled_points = []

        for x_value, y_value in item["points"]:
            x = _scale_value(
                x_value,
                x_min,
                x_max,
                plot_left,
                plot_right,
            )

            y = _scale_value(
                y_value,
                y_min,
                y_max,
                plot_bottom,
                plot_top,
            )

            scaled_points.append((x, y))

        point_string = " ".join(
            f"{x},{y}"
            for x, y in scaled_points
        )

        dash = dash_patterns[
            series_index % len(dash_patterns)
        ]

        parts.append(
            f'<polyline points="{point_string}" '
            f'fill="none" stroke="#222" '
            f'stroke-width="3"{dash}/>'
        )

        for x, y in scaled_points:
            parts.append(
                f'<circle cx="{x}" cy="{y}" r="5" '
                f'fill="white" stroke="#222" '
                f'stroke-width="2"/>'
            )

    # 凡例
    if len(series) > 1:
        legend_x = plot_right - 150
        legend_y = plot_top + 20

        for series_index, item in enumerate(series):
            y = legend_y + series_index * 28

            dash = dash_patterns[
                series_index % len(dash_patterns)
            ]

            parts.append(
                f'<line x1="{legend_x}" y1="{y}" '
                f'x2="{legend_x + 35}" y2="{y}" '
                f'stroke="#222" '
                f'stroke-width="3"{dash}/>'
            )

            parts.append(
                f'<text x="{legend_x + 45}" '
                f'y="{y + 5}" class="legend">'
                f'{escape(item["label"])}</text>'
            )

    parts.append("</svg>")

    return "\n".join(parts)


def render_bar_chart_svg(
    figure_data: Dict[str, Any],
) -> str:
    """
    棒グラフのSVGを生成する。

    v1では1系列の棒グラフを対象とする。
    categories がある場合はX軸にカテゴリ名を表示する。
    """

    title = str(
        figure_data.get("title", "")
    ).strip()

    x_label = str(
        figure_data.get("xLabel", "")
    ).strip()

    y_label = str(
        figure_data.get("yLabel", "")
    ).strip()

    categories = figure_data.get(
        "categories"
    )

    series = _validate_series(
        figure_data
    )

    if len(series) != 1:
        raise ValueError(
            "bar_chart v1 currently supports exactly one series"
        )

    points = series[0]["points"]

    if categories is not None:
        if not isinstance(categories, list):
            raise ValueError(
                "bar_chart 'categories' must be a list"
            )

        if len(categories) != len(points):
            raise ValueError(
                "bar_chart 'categories' length must match "
                "the number of points"
            )

        categories = [
            str(category)
            for category in categories
        ]

    y_values = [
        point[1]
        for point in points
    ]

    y_min = min(
        0.0,
        min(y_values),
    )

    y_max = max(
        y_values
    )

    if y_min == y_max:
        y_max = y_min + 1

    width = 760
    height = 520

    margin_left = 100
    margin_right = 50
    margin_top = 80
    margin_bottom = 110

    plot_left = margin_left
    plot_right = width - margin_right
    plot_top = margin_top
    plot_bottom = height - margin_bottom

    plot_width = (
        plot_right
        - plot_left
    )

    plot_height = (
        plot_bottom
        - plot_top
    )

    parts = [
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}">'
        ),
        "<style>",
        (
            "text { "
            "font-family: -apple-system, BlinkMacSystemFont, "
            "'Hiragino Sans', 'Yu Gothic', sans-serif; "
            "fill: #111; "
            "}"
        ),
        ".title { font-size: 24px; font-weight: 700; }",
        ".axis-label { font-size: 17px; font-weight: 600; }",
        ".tick { font-size: 14px; }",
        "</style>",
        (
            f'<rect width="{width}" '
            f'height="{height}" '
            f'fill="white"/>'
        ),
    ]

    if title:
        parts.append(
            f'<text x="{width / 2}" y="38" '
            f'text-anchor="middle" class="title">'
            f'{escape(title)}</text>'
        )

    parts.extend(
        [
            (
                f'<line x1="{plot_left}" '
                f'y1="{plot_bottom}" '
                f'x2="{plot_right}" '
                f'y2="{plot_bottom}" '
                f'stroke="#222" '
                f'stroke-width="2"/>'
            ),
            (
                f'<line x1="{plot_left}" '
                f'y1="{plot_top}" '
                f'x2="{plot_left}" '
                f'y2="{plot_bottom}" '
                f'stroke="#222" '
                f'stroke-width="2"/>'
            ),
        ]
    )

    tick_count = 5

    for i in range(
        tick_count + 1
    ):
        ratio = (
            i
            / tick_count
        )

        y = (
            plot_bottom
            - ratio
            * plot_height
        )

        value = (
            y_min
            + ratio
            * (
                y_max
                - y_min
            )
        )

        parts.append(
            f'<line x1="{plot_left}" '
            f'y1="{y}" '
            f'x2="{plot_right}" '
            f'y2="{y}" '
            f'stroke="#dddddd" '
            f'stroke-width="1"/>'
        )

        parts.append(
            f'<text x="{plot_left - 12}" '
            f'y="{y + 5}" '
            f'text-anchor="end" '
            f'class="tick">'
            f'{value:g}</text>'
        )

    bar_slot_width = (
        plot_width
        / len(points)
    )

    bar_width = (
        bar_slot_width
        * 0.55
    )

    zero_y = _scale_value(
        0,
        y_min,
        y_max,
        plot_bottom,
        plot_top,
    )

    for index, (
        x_value,
        y_value,
    ) in enumerate(points):
        center_x = (
            plot_left
            + index
            * bar_slot_width
            + bar_slot_width / 2
        )

        value_y = _scale_value(
            y_value,
            y_min,
            y_max,
            plot_bottom,
            plot_top,
        )

        rect_y = min(
            zero_y,
            value_y,
        )

        rect_height = abs(
            zero_y
            - value_y
        )

        parts.append(
            f'<rect '
            f'x="{center_x - bar_width / 2}" '
            f'y="{rect_y}" '
            f'width="{bar_width}" '
            f'height="{rect_height}" '
            f'fill="#eeeeee" '
            f'stroke="#222" '
            f'stroke-width="2"/>'
        )

        if categories is not None:
            x_tick_label = categories[
                index
            ]
        else:
            x_tick_label = (
                f"{x_value:g}"
            )

        parts.append(
            f'<text '
            f'x="{center_x}" '
            f'y="{plot_bottom + 25}" '
            f'text-anchor="middle" '
            f'class="tick">'
            f'{escape(x_tick_label)}'
            f'</text>'
        )

    if x_label:
        parts.append(
            f'<text '
            f'x="{plot_left + plot_width / 2}" '
            f'y="{height - 25}" '
            f'text-anchor="middle" '
            f'class="axis-label">'
            f'{escape(x_label)}'
            f'</text>'
        )

    if y_label:
        parts.append(
            f'<text x="25" '
            f'y="{plot_top + plot_height / 2}" '
            f'text-anchor="middle" '
            f'transform="rotate(-90 25 '
            f'{plot_top + plot_height / 2})" '
            f'class="axis-label">'
            f'{escape(y_label)}</text>'
        )

    parts.append("</svg>")

    return "\n".join(parts)
