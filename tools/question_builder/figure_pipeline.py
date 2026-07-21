from pathlib import Path
from typing import Any, Dict, Optional

from tools.question_builder.diagram_engine import (
    render_figure,
    validate_figure_spec,
)


def attach_generated_figure(
    question: Dict[str, Any],
    output_path: str,
    public_image_path: Optional[str] = None,
) -> Dict[str, Any]:
    """
    AIが生成した問題データを受け取り、
    figureType / figureData に応じて図表を生成し、
    問題データへ image パスを追加する。

    Parameters
    ----------
    question:
        AIが生成した問題データ。

        例:
        {
            "question": "次の表を見て答えよ。",
            "choices": [...],
            "answer": 2,
            "explanation": "...",
            "figureType": "table",
            "figureData": {...}
        }

    output_path:
        Diagram Engine が実際にSVGを書き出す保存先。

        例:
        public/pharmacy/generated/q001.svg

    public_image_path:
        Study QUEST側の問題データへ保存する公開パス。

        例:
        /pharmacy/generated/q001.svg

        省略した場合は output_path をそのまま使用する。

    Returns
    -------
    Dict[str, Any]
        image が必要な場合は追加された新しい問題データ。
        元の question dict は直接変更しない。
    """

    if not isinstance(question, dict):
        raise ValueError(
            "question must be a dictionary"
        )

    result = dict(question)

    figure_type = result.get(
        "figureType",
        "none",
    )

    figure_data = result.get(
        "figureData"
    )

    validate_figure_spec(
        figure_type=figure_type,
        figure_data=figure_data,
    )

    if figure_type == "none":
        result.pop(
            "image",
            None,
        )

        return result

    output = Path(
        output_path
    )

    if output.suffix.lower() != ".svg":
        raise ValueError(
            "Generated question figures must currently "
            "use an '.svg' output path"
        )

    generated_path = render_figure(
        figure_type=figure_type,
        figure_data=figure_data,
        output_path=str(output),
    )

    if generated_path is None:
        raise RuntimeError(
            "Diagram Engine did not return "
            "a generated file path"
        )

    if public_image_path is None:
        image_path = generated_path
    else:
        image_path = public_image_path

    result["image"] = image_path

    return result
