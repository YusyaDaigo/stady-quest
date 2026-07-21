import argparse
import json
from pathlib import Path
from typing import Any, Dict

from .renderer import render_figure
from .schema import validate_figure_spec


def load_figure_spec(
    input_path: Path,
) -> Dict[str, Any]:
    """
    JSONファイルからfigure仕様を読み込む。
    """

    if not input_path.exists():
        raise FileNotFoundError(
            f"Input file not found: {input_path}"
        )

    if input_path.suffix.lower() != ".json":
        raise ValueError(
            "Input file must be a .json file"
        )

    with input_path.open(
        "r",
        encoding="utf-8",
    ) as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError(
            "Figure spec JSON must be an object"
        )

    if "figureType" not in data:
        raise ValueError(
            "Figure spec requires 'figureType'"
        )

    if "figureData" not in data:
        raise ValueError(
            "Figure spec requires 'figureData'"
        )

    return data


def generate_preview(
    input_path: Path,
    output_path: Path,
) -> str:
    """
    JSON仕様からSVGプレビューを生成する。
    """

    spec = load_figure_spec(
        input_path
    )

    figure_type = spec[
        "figureType"
    ]

    figure_data = spec[
        "figureData"
    ]

    validate_figure_spec(
        figure_type=figure_type,
        figure_data=figure_data,
    )

    result = render_figure(
        figure_type=figure_type,
        figure_data=figure_data,
        output_path=str(
            output_path
        ),
    )

    if result is None:
        raise ValueError(
            "Cannot generate a preview "
            "when figureType is 'none'"
        )

    return result


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Generate a Study QUEST "
            "Diagram Engine SVG preview "
            "from a JSON figure specification."
        )
    )

    parser.add_argument(
        "input",
        help=(
            "Path to the input JSON file"
        ),
    )

    parser.add_argument(
        "-o",
        "--output",
        help=(
            "Output SVG path. "
            "If omitted, the input filename "
            "is used with an .svg extension."
        ),
    )

    args = parser.parse_args()

    input_path = Path(
        args.input
    )

    if args.output:
        output_path = Path(
            args.output
        )
    else:
        output_path = (
            input_path
            .with_suffix(".svg")
        )

    result = generate_preview(
        input_path=input_path,
        output_path=output_path,
    )

    print(
        f"Generated: {result}"
    )


if __name__ == "__main__":
    main()
