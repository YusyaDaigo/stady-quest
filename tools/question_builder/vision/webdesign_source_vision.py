import base64
import json
import os
from pathlib import Path
from typing import Any, Dict

from dotenv import load_dotenv
from openai import OpenAI

from tools.question_builder.config import OPENAI_VISION_MODEL


ROOT_DIR = Path(__file__).resolve().parents[3]

load_dotenv(
    dotenv_path=ROOT_DIR / ".env"
)


ALLOWED_SECTIONS = {
    "internet",
    "html_css",
    "design",
    "accessibility",
    "operation",
}


def image_to_data_url(
    image_path: Path,
) -> str:
    image_bytes = image_path.read_bytes()
    encoded = base64.b64encode(
        image_bytes
    ).decode("utf-8")

    suffix = image_path.suffix.lower()

    media_type = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }.get(
        suffix,
        "image/png",
    )

    return (
        f"data:{media_type};"
        f"base64,{encoded}"
    )


def build_webdesign_source_prompt(
    page_number: int,
) -> str:
    if page_number < 1:
        raise ValueError(
            "page_number must be at least 1"
        )

    return f"""
あなたはウェブデザイン技能検定3級の
学習用Knowledgeを構築するための解析担当です。

添付画像は教材・過去問題・試験資料などの
ページ画像です。

対象ページ:
{page_number}

目的:
画像の文章を全文OCRして保存することではありません。
このページから学習すべき知識・概念・技能・
出題論点を抽象化して整理してください。

重要なルール:
- 原文全文を書き起こさないでください。
- 問題文をそのまま転記しないでください。
- 選択肢をそのまま転記しないでください。
- 解説文を長文のまま転記しないでください。
- 元資料特有の表現を再現しないでください。
- 学習上必要な事実・概念・技能へ抽象化してください。
- 同じ概念を重複して出力しないでください。
- 画像から確認できない知識を推測で補足しないでください。
- 1ページ内に複数の論点があれば複数conceptに分けてください。
- 学習論点が存在しない表紙・空白ページ等では
  conceptsを空配列にしてください。

sectionは必ず次のいずれかです:
- internet
- html_css
- design
- accessibility
- operation

sectionの目安:
internet:
インターネット、Web、HTTP、URL、
ネットワーク、セキュリティ、関連技術

html_css:
HTML、CSS、文書構造、要素、属性、
スタイル、レイアウト、Web標準

design:
色彩、画像、レイアウト、視覚表現、
デザイン原則、ユーザーインターフェース

accessibility:
アクセシビリティ、ユーザビリティ、
支援技術、代替テキスト、利用者配慮

operation:
制作作業、ファイル管理、ソフトウェア操作、
公開作業、実務上の手順

必ずJSONのみを返してください。

形式:
{{
  "page": {page_number},
  "concepts": [
    {{
      "section": "html_css",
      "title": "短い学習論点名",
      "keywords": [
        "keyword1",
        "keyword2"
      ],
      "summary": "原文を複製しない簡潔な概念要約",
      "learningObjectives": [
        "学習者ができるようになること"
      ],
      "sourcePages": [
        {page_number}
      ]
    }}
  ]
}}
""".strip()


def _parse_json_response(
    response_text: str,
) -> Dict[str, Any]:
    text = response_text.strip()

    if text.startswith("```"):
        lines = text.splitlines()

        if lines:
            lines = lines[1:]

        if (
            lines
            and lines[-1].strip() == "```"
        ):
            lines = lines[:-1]

        text = "\n".join(lines).strip()

    data = json.loads(text)

    if not isinstance(data, dict):
        raise ValueError(
            "Vision response must be a JSON object"
        )

    return data


def validate_webdesign_knowledge(
    data: Dict[str, Any],
    *,
    expected_page: int,
) -> Dict[str, Any]:
    if not isinstance(data, dict):
        raise ValueError(
            "data must be an object"
        )

    page = data.get("page")

    if page != expected_page:
        raise ValueError(
            "Vision response page mismatch: "
            f"expected={expected_page}, "
            f"actual={page}"
        )

    concepts = data.get("concepts")

    if not isinstance(concepts, list):
        raise ValueError(
            "concepts must be an array"
        )

    normalized_concepts = []

    for index, concept in enumerate(
        concepts,
        start=1,
    ):
        if not isinstance(concept, dict):
            raise ValueError(
                f"concept {index} must be an object"
            )

        section = concept.get("section")

        if section not in ALLOWED_SECTIONS:
            raise ValueError(
                f"concept {index} has invalid "
                f"section: {section}"
            )

        title = concept.get("title")

        if (
            not isinstance(title, str)
            or not title.strip()
        ):
            raise ValueError(
                f"concept {index} requires title"
            )

        summary = concept.get("summary")

        if (
            not isinstance(summary, str)
            or not summary.strip()
        ):
            raise ValueError(
                f"concept {index} requires summary"
            )

        keywords = concept.get("keywords")

        if (
            not isinstance(keywords, list)
            or any(
                not isinstance(item, str)
                or not item.strip()
                for item in keywords
            )
        ):
            raise ValueError(
                f"concept {index} has invalid keywords"
            )

        learning_objectives = concept.get(
            "learningObjectives"
        )

        if (
            not isinstance(
                learning_objectives,
                list,
            )
            or not learning_objectives
            or any(
                not isinstance(item, str)
                or not item.strip()
                for item in learning_objectives
            )
        ):
            raise ValueError(
                f"concept {index} has invalid "
                "learningObjectives"
            )

        source_pages = concept.get(
            "sourcePages"
        )

        if (
            not isinstance(source_pages, list)
            or expected_page
            not in source_pages
        ):
            raise ValueError(
                f"concept {index} must include "
                f"source page {expected_page}"
            )

        normalized_concepts.append(
            {
                "section": section,
                "title": title.strip(),
                "keywords": [
                    item.strip()
                    for item in keywords
                ],
                "summary": summary.strip(),
                "learningObjectives": [
                    item.strip()
                    for item
                    in learning_objectives
                ],
                "sourcePages": sorted(
                    {
                        int(item)
                        for item
                        in source_pages
                    }
                ),
            }
        )

    return {
        "page": expected_page,
        "concepts": normalized_concepts,
    }


def analyze_webdesign_page(
    image_path: Path,
    *,
    page_number: int,
    allow_api: bool = False,
    model: str = OPENAI_VISION_MODEL,
) -> Dict[str, Any]:
    image_path = Path(image_path)

    if page_number < 1:
        raise ValueError(
            "page_number must be at least 1"
        )

    if not image_path.exists():
        raise FileNotFoundError(
            image_path
        )

    if not allow_api:
        raise RuntimeError(
            "OpenAI API呼び出しは無効です。"
            "実行する場合は allow_api=True を"
            "明示してください。"
        )

    if (
        os.getenv("STUDY_QUEST_NO_API")
        == "1"
    ):
        raise RuntimeError(
            "STUDY_QUEST_NO_API=1 のため"
            "OpenAI APIを呼びません"
        )

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError(
            "OPENAI_API_KEY が設定されていません"
        )

    prompt = build_webdesign_source_prompt(
        page_number
    )

    image_data_url = image_to_data_url(
        image_path
    )

    print(
        "[API CALL] "
        f"webdesign source vision "
        f"page={page_number} "
        f"model={model}"
    )

    client = OpenAI()

    response = client.responses.create(
        model=model,
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": prompt,
                    },
                    {
                        "type": "input_image",
                        "image_url": (
                            image_data_url
                        ),
                    },
                ],
            }
        ],
    )

    response_text = response.output_text

    if not response_text:
        raise ValueError(
            "OpenAI APIから空のレスポンスが"
            "返されました"
        )

    parsed = _parse_json_response(
        response_text
    )

    return validate_webdesign_knowledge(
        parsed,
        expected_page=page_number,
    )


def get_cache_path(
    document_id: str,
    page_number: int,
    *,
    cache_root: Path = (
        ROOT_DIR
        / "generated_materials"
        / "webdesign"
        / "vision_cache"
    ),
) -> Path:
    if not document_id.strip():
        raise ValueError(
            "document_id must not be empty"
        )

    if page_number < 1:
        raise ValueError(
            "page_number must be at least 1"
        )

    safe_document_id = (
        document_id
        .replace("/", "_")
        .replace("\\", "_")
    )

    return (
        Path(cache_root)
        / safe_document_id
        / f"page_{page_number:03d}.json"
    )


def analyze_webdesign_page_cached(
    image_path: Path,
    *,
    document_id: str,
    page_number: int,
    allow_api: bool = False,
    model: str = OPENAI_VISION_MODEL,
) -> Dict[str, Any]:
    cache_path = get_cache_path(
        document_id,
        page_number,
    )

    if cache_path.exists():
        print(
            "[CACHE] "
            f"{cache_path}"
        )

        data = json.loads(
            cache_path.read_text(
                encoding="utf-8"
            )
        )

        return validate_webdesign_knowledge(
            data,
            expected_page=page_number,
        )

    result = analyze_webdesign_page(
        image_path,
        page_number=page_number,
        allow_api=allow_api,
        model=model,
    )

    cache_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    cache_path.write_text(
        json.dumps(
            result,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(
        "[CACHE SAVED] "
        f"{cache_path}"
    )

    return result
