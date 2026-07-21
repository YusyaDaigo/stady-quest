from pathlib import Path

from tools.question_builder.diagram_engine import (
    build_figure_spec,
    render_figure,
    validate_figure_spec,
)


OUTPUT_DIR = Path(
    "tmp/diagram_engine/tests"
)


def test_none() -> None:
    validate_figure_spec(
        figure_type="none",
        figure_data=None,
    )

    result = render_figure(
        figure_type="none",
        figure_data=None,
        output_path=str(
            OUTPUT_DIR
            / "none.svg"
        ),
    )

    assert result is None


def test_build_figure_spec() -> None:
    spec = build_figure_spec(
        figure_type="table",
        figure_data={
            "title": "テスト表",
            "headers": [
                "項目",
                "値",
            ],
            "rows": [
                [
                    "A",
                    "10",
                ],
            ],
        },
    )

    assert (
        spec["figureType"]
        == "table"
    )

    assert (
        spec["figureData"]["title"]
        == "テスト表"
    )


def test_table() -> None:
    output_path = (
        OUTPUT_DIR
        / "table.svg"
    )

    result = render_figure(
        figure_type="table",
        figure_data={
            "title": "薬物A〜Cの性質",
            "headers": [
                "薬物",
                "pKa",
                "分配係数",
            ],
            "rows": [
                [
                    "A",
                    "4.2",
                    "1.5",
                ],
                [
                    "B",
                    "7.4",
                    "2.8",
                ],
                [
                    "C",
                    "9.1",
                    "0.7",
                ],
            ],
        },
        output_path=str(
            output_path
        ),
    )

    assert (
        result
        == str(output_path)
    )

    assert output_path.exists()


def test_line_chart() -> None:
    output_path = (
        OUTPUT_DIR
        / "line_chart.svg"
    )

    result = render_figure(
        figure_type="line_chart",
        figure_data={
            "title": "血中濃度推移",
            "xLabel": "時間",
            "yLabel": "血中濃度",
            "series": [
                {
                    "label": "薬物A",
                    "points": [
                        [0, 0],
                        [1, 8],
                        [2, 5],
                        [4, 2],
                    ],
                }
            ],
        },
        output_path=str(
            output_path
        ),
    )

    assert (
        result
        == str(output_path)
    )

    assert output_path.exists()


def test_bar_chart() -> None:
    output_path = (
        OUTPUT_DIR
        / "bar_chart.svg"
    )

    result = render_figure(
        figure_type="bar_chart",
        figure_data={
            "title": "薬物A〜Dの吸収率",
            "xLabel": "薬物",
            "yLabel": "吸収率",
            "categories": [
                "薬物A",
                "薬物B",
                "薬物C",
                "薬物D",
            ],
            "series": [
                {
                    "label": "吸収率",
                    "points": [
                        [1, 35],
                        [2, 60],
                        [3, 82],
                        [4, 48],
                    ],
                }
            ],
        },
        output_path=str(
            output_path
        ),
    )

    assert (
        result
        == str(output_path)
    )

    assert output_path.exists()


def test_flowchart() -> None:
    output_path = (
        OUTPUT_DIR
        / "flowchart.svg"
    )

    result = render_figure(
        figure_type="flowchart",
        figure_data={
            "title": "薬物の代謝経路",
            "nodes": [
                {
                    "id": "a",
                    "label": "薬物A",
                },
                {
                    "id": "b",
                    "label": "代謝物B",
                },
                {
                    "id": "c",
                    "label": "尿中排泄",
                },
            ],
            "edges": [
                [
                    "a",
                    "b",
                ],
                [
                    "b",
                    "c",
                ],
            ],
        },
        output_path=str(
            output_path
        ),
    )

    assert (
        result
        == str(output_path)
    )

    assert output_path.exists()


def test_invalid_figure_type() -> None:
    try:
        validate_figure_spec(
            figure_type="unknown",
            figure_data={},
        )
    except ValueError:
        return

    raise AssertionError(
        "Expected ValueError "
        "for unsupported figure type"
    )


def run_all_tests() -> None:
    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    tests = [
        test_none,
        test_build_figure_spec,
        test_table,
        test_line_chart,
        test_bar_chart,
        test_flowchart,
        test_invalid_figure_type,
    ]

    for test in tests:
        test()

        print(
            f"[PASS] "
            f"{test.__name__}"
        )

    print()
    print(
        "All Diagram Engine tests passed."
    )


if __name__ == "__main__":
    run_all_tests()
