from html import escape
from typing import Any, Dict, List, Tuple


def render_flowchart_svg(
    figure_data: Dict[str, Any],
) -> str:
    """
    上から下へ流れる基本フローチャートのSVGを生成する。

    想定形式:
    {
        "title": "薬物の代謝経路",
        "nodes": [
            {
                "id": "a",
                "label": "薬物A"
            },
            {
                "id": "b",
                "label": "代謝物B"
            },
            {
                "id": "c",
                "label": "尿中排泄"
            }
        ],
        "edges": [
            ["a", "b"],
            ["b", "c"]
        ]
    }
    """

    title = str(
        figure_data.get("title", "")
    ).strip()

    nodes = figure_data.get("nodes", [])
    edges = figure_data.get("edges", [])

    if not isinstance(nodes, list) or not nodes:
        raise ValueError(
            "flowchart figureData requires "
            "a non-empty 'nodes' list"
        )

    if not isinstance(edges, list):
        raise ValueError(
            "flowchart figureData 'edges' "
            "must be a list"
        )

    normalized_nodes: List[Dict[str, str]] = []
    node_ids = set()

    for index, node in enumerate(nodes):
        if not isinstance(node, dict):
            raise ValueError(
                f"flowchart node {index} "
                "must be an object"
            )

        node_id = str(
            node.get("id", "")
        ).strip()

        label = str(
            node.get("label", "")
        ).strip()

        if not node_id:
            raise ValueError(
                f"flowchart node {index} "
                "requires a non-empty 'id'"
            )

        if not label:
            raise ValueError(
                f"flowchart node {index} "
                "requires a non-empty 'label'"
            )

        if node_id in node_ids:
            raise ValueError(
                f"duplicate flowchart node id: "
                f"'{node_id}'"
            )

        node_ids.add(node_id)

        normalized_nodes.append(
            {
                "id": node_id,
                "label": label,
            }
        )

    normalized_edges: List[Tuple[str, str]] = []

    for index, edge in enumerate(edges):
        if (
            not isinstance(edge, list)
            or len(edge) != 2
        ):
            raise ValueError(
                f"flowchart edge {index} "
                "must be [source_id, target_id]"
            )

        source_id = str(edge[0])
        target_id = str(edge[1])

        if source_id not in node_ids:
            raise ValueError(
                f"flowchart edge {index} "
                f"references unknown source "
                f"node '{source_id}'"
            )

        if target_id not in node_ids:
            raise ValueError(
                f"flowchart edge {index} "
                f"references unknown target "
                f"node '{target_id}'"
            )

        normalized_edges.append(
            (
                source_id,
                target_id,
            )
        )

    width = 760

    node_width = 320
    node_height = 72
    node_gap = 70

    margin_top = 90 if title else 40
    margin_bottom = 50

    total_nodes_height = (
        len(normalized_nodes) * node_height
    )

    total_gaps_height = (
        max(
            len(normalized_nodes) - 1,
            0,
        )
        * node_gap
    )

    height = (
        margin_top
        + total_nodes_height
        + total_gaps_height
        + margin_bottom
    )

    center_x = width / 2
    node_x = center_x - node_width / 2

    node_positions = {}

    for index, node in enumerate(
        normalized_nodes
    ):
        y = (
            margin_top
            + index
            * (
                node_height
                + node_gap
            )
        )

        node_positions[
            node["id"]
        ] = {
            "x": node_x,
            "y": y,
            "center_x": center_x,
            "center_y": (
                y
                + node_height / 2
            ),
        }

    parts = [
        (
            f'<svg '
            f'xmlns="http://www.w3.org/2000/svg" '
            f'width="{width}" '
            f'height="{height}" '
            f'viewBox="0 0 {width} {height}">'
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
            ".node-label { "
            "font-size: 18px; "
            "font-weight: 600; "
            "}"
        ),
        "</style>",
        (
            f'<rect '
            f'width="{width}" '
            f'height="{height}" '
            f'fill="white"/>'
        ),
        "<defs>",
        (
            '<marker '
            'id="arrow" '
            'markerWidth="10" '
            'markerHeight="10" '
            'refX="9" '
            'refY="3" '
            'orient="auto" '
            'markerUnits="strokeWidth">'
        ),
        (
            '<path '
            'd="M0,0 L0,6 L9,3 z" '
            'fill="#222"/>'
        ),
        "</marker>",
        "</defs>",
    ]

    if title:
        parts.append(
            f'<text '
            f'x="{center_x}" '
            f'y="40" '
            f'text-anchor="middle" '
            f'class="title">'
            f'{escape(title)}'
            f'</text>'
        )

    # エッジを先に描画
    for source_id, target_id in normalized_edges:
        source = node_positions[
            source_id
        ]

        target = node_positions[
            target_id
        ]

        x1 = source["center_x"]
        y1 = (
            source["y"]
            + node_height
        )

        x2 = target["center_x"]
        y2 = (
            target["y"]
            - 8
        )

        parts.append(
            f'<line '
            f'x1="{x1}" '
            f'y1="{y1}" '
            f'x2="{x2}" '
            f'y2="{y2}" '
            f'stroke="#222" '
            f'stroke-width="2.5" '
            f'marker-end="url(#arrow)"/>'
        )

    # ノード描画
    for node in normalized_nodes:
        position = node_positions[
            node["id"]
        ]

        x = position["x"]
        y = position["y"]

        parts.append(
            f'<rect '
            f'x="{x}" '
            f'y="{y}" '
            f'width="{node_width}" '
            f'height="{node_height}" '
            f'rx="12" '
            f'ry="12" '
            f'fill="#eeeeee" '
            f'stroke="#222" '
            f'stroke-width="2"/>'
        )

        parts.append(
            f'<text '
            f'x="{center_x}" '
            f'y="{y + node_height / 2 + 6}" '
            f'text-anchor="middle" '
            f'class="node-label">'
            f'{escape(node["label"])}'
            f'</text>'
        )

    parts.append("</svg>")

    return "\n".join(parts)
