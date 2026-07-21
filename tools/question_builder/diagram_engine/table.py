from html import escape
from typing import Any, Dict, List


def _split_header_lines(
    text: str,
) -> List[str]:
    """
    表ヘッダーを読みやすい行に分割する。

    単位表記は可能な限り2行目へ送る。
    """

    text = str(text).strip()

    unit_patterns = [
        "（mg/L）",
        "(mg/L)",
        "（mg/mL）",
        "(mg/mL)",
        "（μg/mL）",
        "(μg/mL)",
        "（ng/mL）",
        "(ng/mL)",
    ]

    for unit in unit_patterns:
        if text.endswith(unit):
            main_text = text[
                : -len(unit)
            ].strip()

            if main_text:
                return [
                    main_text,
                    unit,
                ]

            return [
                unit
            ]

    max_chars = 14

    if len(text) <= max_chars:
        return [
            text
        ]

    return [
        text[:max_chars],
        text[max_chars:],
    ]


def _estimate_column_width(
    header_lines: List[str],
    column_cells: List[str],
) -> int:
    """
    ヘッダーとデータ内容から列幅を推定する。

    完全な文字幅計測ではなく、
    Diagram Engine v1向けの簡易推定。
    """

    longest_header = max(
        (
            len(line)
            for line in header_lines
        ),
        default=0,
    )

    longest_cell = max(
        (
            len(str(cell))
            for cell in column_cells
        ),
        default=0,
    )

    longest_content = max(
        longest_header,
        longest_cell,
    )

    estimated_width = (
        longest_content * 16
        + 48
    )

    return max(
        130,
        min(
            estimated_width,
            300,
        ),
    )


def render_table_svg(
    figure_data: Dict[str, Any],
) -> str:
    """
    figureData から表形式の SVG を生成する。
    """

    title = str(
        figure_data.get(
            "title",
            "",
        )
    ).strip()

    headers = figure_data.get(
        "headers",
        [],
    )

    rows = figure_data.get(
        "rows",
        [],
    )

    if (
        not isinstance(
            headers,
            list,
        )
        or not headers
    ):
        raise ValueError(
            "table figureData requires "
            "a non-empty 'headers' list"
        )

    if not isinstance(
        rows,
        list,
    ):
        raise ValueError(
            "table figureData 'rows' "
            "must be a list"
        )

    column_count = len(
        headers
    )

    normalized_rows: List[
        List[str]
    ] = []

    for row_index, row in enumerate(
        rows
    ):
        if not isinstance(
            row,
            list,
        ):
            raise ValueError(
                f"table row {row_index} "
                "must be a list"
            )

        if len(row) != column_count:
            raise ValueError(
                f"table row {row_index} "
                f"has {len(row)} cells, "
                f"but {column_count} "
                "headers were provided"
            )

        normalized_rows.append(
            [
                str(cell)
                for cell in row
            ]
        )

    cell_height = 52

    title_height = (
        70
        if title
        else 20
    )

    margin = 20

    wrapped_headers = [
        _split_header_lines(
            str(header)
        )
        for header in headers
    ]

    max_header_lines = max(
        len(lines)
        for lines in wrapped_headers
    )

    header_line_height = 24

    header_height = max(
        cell_height,
        max_header_lines
        * header_line_height
        + 20,
    )

    # 列ごとの幅を自動計算
    column_widths: List[int] = []

    for column_index in range(
        column_count
    ):
        column_cells = [
            row[column_index]
            for row in normalized_rows
        ]

        width = _estimate_column_width(
            header_lines=wrapped_headers[
                column_index
            ],
            column_cells=column_cells,
        )

        column_widths.append(
            width
        )

    table_width = sum(
        column_widths
    )

    data_height = (
        len(normalized_rows)
        * cell_height
    )

    table_height = (
        header_height
        + data_height
    )

    svg_width = (
        table_width
        + margin * 2
    )

    svg_height = (
        title_height
        + table_height
        + margin
    )

    table_x = margin
    table_y = title_height

    column_starts: List[float] = []
    current_x = table_x

    for width in column_widths:
        column_starts.append(
            current_x
        )

        current_x += width

    parts = [
        (
            f'<svg '
            f'xmlns="http://www.w3.org/2000/svg" '
            f'width="{svg_width}" '
            f'height="{svg_height}" '
            f'viewBox="0 0 '
            f'{svg_width} {svg_height}">'
        ),
        "<style>",
        (
            "text { "
            "font-family: -apple-system, "
            "BlinkMacSystemFont, "
            "'Hiragino Sans', "
            "'Yu Gothic', "
            "sans-serif; "
            "fill: #111; "
            "}"
        ),
        (
            ".title { "
            "font-size: 24px; "
            "font-weight: 700; "
            "}"
        ),
        (
            ".header { "
            "font-size: 17px; "
            "font-weight: 700; "
            "}"
        ),
        (
            ".cell { "
            "font-size: 17px; "
            "}"
        ),
        "</style>",
        (
            f'<rect '
            f'width="{svg_width}" '
            f'height="{svg_height}" '
            f'fill="white"/>'
        ),
    ]

    if title:
        parts.append(
            f'<text '
            f'x="{svg_width / 2}" '
            f'y="40" '
            f'text-anchor="middle" '
            f'class="title">'
            f'{escape(title)}'
            f'</text>'
        )

    parts.append(
        f'<rect '
        f'x="{table_x}" '
        f'y="{table_y}" '
        f'width="{table_width}" '
        f'height="{header_height}" '
        f'fill="#eeeeee"/>'
    )

    header_bottom_y = (
        table_y
        + header_height
    )

    parts.append(
        f'<line '
        f'x1="{table_x}" '
        f'y1="{table_y}" '
        f'x2="{table_x + table_width}" '
        f'y2="{table_y}" '
        f'stroke="#222" '
        f'stroke-width="1.5"/>'
    )

    parts.append(
        f'<line '
        f'x1="{table_x}" '
        f'y1="{header_bottom_y}" '
        f'x2="{table_x + table_width}" '
        f'y2="{header_bottom_y}" '
        f'stroke="#222" '
        f'stroke-width="1.5"/>'
    )

    for row_index in range(
        len(normalized_rows) + 1
    ):
        y = (
            header_bottom_y
            + row_index
            * cell_height
        )

        parts.append(
            f'<line '
            f'x1="{table_x}" '
            f'y1="{y}" '
            f'x2="{table_x + table_width}" '
            f'y2="{y}" '
            f'stroke="#222" '
            f'stroke-width="1.5"/>'
        )

    # 縦線
    vertical_x = table_x

    parts.append(
        f'<line '
        f'x1="{vertical_x}" '
        f'y1="{table_y}" '
        f'x2="{vertical_x}" '
        f'y2="{table_y + table_height}" '
        f'stroke="#222" '
        f'stroke-width="1.5"/>'
    )

    for width in column_widths:
        vertical_x += width

        parts.append(
            f'<line '
            f'x1="{vertical_x}" '
            f'y1="{table_y}" '
            f'x2="{vertical_x}" '
            f'y2="{table_y + table_height}" '
            f'stroke="#222" '
            f'stroke-width="1.5"/>'
        )

    # ヘッダー文字
    for column_index, lines in enumerate(
        wrapped_headers
    ):
        x = (
            column_starts[
                column_index
            ]
            + column_widths[
                column_index
            ] / 2
        )

        total_text_height = (
            len(lines)
            * header_line_height
        )

        first_line_y = (
            table_y
            + header_height / 2
            - total_text_height / 2
            + header_line_height
            - 4
        )

        for line_index, line in enumerate(
            lines
        ):
            y = (
                first_line_y
                + line_index
                * header_line_height
            )

            parts.append(
                f'<text '
                f'x="{x}" '
                f'y="{y}" '
                f'text-anchor="middle" '
                f'class="header">'
                f'{escape(line)}'
                f'</text>'
            )

    # データ行
    for row_index, row in enumerate(
        normalized_rows
    ):
        for column_index, cell in enumerate(
            row
        ):
            x = (
                column_starts[
                    column_index
                ]
                + column_widths[
                    column_index
                ] / 2
            )

            y = (
                header_bottom_y
                + row_index
                * cell_height
                + cell_height / 2
                + 6
            )

            parts.append(
                f'<text '
                f'x="{x}" '
                f'y="{y}" '
                f'text-anchor="middle" '
                f'class="cell">'
                f'{escape(cell)}'
                f'</text>'
            )

    parts.append(
        "</svg>"
    )

    return "\n".join(
        parts
    )
