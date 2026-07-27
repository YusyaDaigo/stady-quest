from pathlib import Path
from typing import Union


PathLike = Union[str, Path]


def load_template(path: PathLike) -> str:
    """
    UTF-8のテンプレートファイルを読み込む。
    """

    template_path = Path(path)

    if not template_path.exists():
        raise FileNotFoundError(
            f"Template file not found: {template_path}"
        )

    if not template_path.is_file():
        raise ValueError(
            f"Template path is not a file: {template_path}"
        )

    return template_path.read_text(encoding="utf-8")
