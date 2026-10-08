import json
import os
from pathlib import Path
from typing import Any, Dict, List

from dotenv import load_dotenv
from openai import OpenAI

from tools.question_builder.config import (
    OPENAI_VISION_MODEL,
)
from tools.question_builder.vision.webdesign_source_vision import (
    image_to_data_url,
)


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


def build_webdesign_answer_prompt(
    page_number: int,
) -> str:
    if page_number < 1:
        raise ValueError(
            "page_number must be at least 1"
        )

    return f"""
あなたはウェブデザイン技能検定3級の
解答・解説資料から、
問題生成用Knowledgeの根拠情報を
抽出する解析担当です。

添付画像は解答・解説資料のページです。

対象PDFページ:
{page_number}

画像内に掲載されている各問題について、
次の情報を抽出してください。

重要:
- 問題番号は画像に表示された番号を使用してください。
- correctAnswer は資料に明示された正答番号を
  1始まりの整数で記録してください。
- 正答を画像から確認できない場合は
  その問題を出力しないでください。
- verifiedFacts は解説から直接確認できる、
  正答を支える具体的事実だけを書いてください。
- 一般知識や推測で補完しないでください。
- verifiedFacts は短い独立した事実文にしてください。
- 解説本文を長文のまま転載しないでください。
- explanationSummary は解説の要点を
  独立した表現で簡潔にまとめてください。
- 画像に存在しない問題番号を推測で追加しないでください。
- 同一問題を重複して出力しないでください。

section は必ず次のいずれかです:
- internet
- html_css
- design
- accessibility
- operation

section の目安:
internet:
インターネット、HTTP、IP、DNS、
ネットワーク、セキュリティ、通信技術

html_css:
HTML、CSS、要素、属性、Web標準、
スタイル、DOM、マークアップ

design:
色彩、画像、レイアウト、UI、
デザイン原則

accessibility:
アクセシビリティ、ユーザビリティ、
支援技術、利用者配慮

operation:
制作作業、ファイル管理、公開、
関連法規、作業手順

必ずJSONのみを返してください。

形式:
{{
  "page": {page_number},
  "answers": [
    {{
      "questionNo": 1,
      "correctAnswer": 2,
      "section": "html_css",
      "verifiedFacts": [
        "正答を支える具体的な事実"
      ],
      "explanationSummary": "解説の簡潔な要約",
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

        text = "\n".join(
            lines
        ).strip()

    data = json.loads(
        text
    )

    if not isinstance(
        data,
        dict,
    ):
        raise ValueError(
            "Vision response must be "
            "a JSON object"
        )

    return data


def validate_webdesign_answers(
    data: Dict[str, Any],
    *,
    expected_page: int,
) -> Dict[str, Any]:
    if not isinstance(
        data,
        dict,
    ):
        raise ValueError(
            "data must be an object"
        )

    if data.get("page") != expected_page:
        raise ValueError(
            "Vision response page mismatch"
        )

    answers = data.get(
        "answers"
    )

    if not isinstance(
        answers,
        list,
    ):
        raise ValueError(
            "answers must be an array"
        )

    normalized: List[
        Dict[str, Any]
    ] = []

    seen_question_numbers = set()

    for index, answer in enumerate(
        answers,
        start=1,
    ):
        if not isinstance(
            answer,
            dict,
        ):
            raise ValueError(
                f"answer {index} "
                "must be an object"
            )

        question_no = answer.get(
            "questionNo"
        )

        if (
            not isinstance(
                question_no,
                int,
            )
            or question_no < 1
        ):
            raise ValueError(
                f"answer {index} has "
                "invalid questionNo"
            )

        if (
            question_no
            in seen_question_numbers
        ):
            raise ValueError(
                "duplicate questionNo: "
                f"{question_no}"
            )

        seen_question_numbers.add(
            question_no
        )

        correct_answer = answer.get(
            "correctAnswer"
        )

        if (
            not isinstance(
                correct_answer,
                int,
            )
            or not (
                1
                <= correct_answer
                <= 4
            )
        ):
            raise ValueError(
                f"question {question_no} "
                "has invalid correctAnswer"
            )

        section = answer.get(
            "section"
        )

        if section not in ALLOWED_SECTIONS:
            raise ValueError(
                f"question {question_no} "
                f"has invalid section: "
                f"{section}"
            )

        verified_facts = answer.get(
            "verifiedFacts"
        )

        if (
            not isinstance(
                verified_facts,
                list,
            )
            or not verified_facts
            or any(
                not isinstance(
                    item,
                    str,
                )
                or not item.strip()
                for item
                in verified_facts
            )
        ):
            raise ValueError(
                f"question {question_no} "
                "requires verifiedFacts"
            )

        explanation_summary = (
            answer.get(
                "explanationSummary"
            )
        )

        if (
            not isinstance(
                explanation_summary,
                str,
            )
            or not (
                explanation_summary.strip()
            )
        ):
            raise ValueError(
                f"question {question_no} "
                "requires "
                "explanationSummary"
            )

        source_pages = answer.get(
            "sourcePages"
        )

        if (
            not isinstance(
                source_pages,
                list,
            )
            or expected_page
            not in source_pages
        ):
            raise ValueError(
                f"question {question_no} "
                f"must include source page "
                f"{expected_page}"
            )

        normalized.append(
            {
                "questionNo": (
                    question_no
                ),
                "correctAnswer": (
                    correct_answer
                ),
                "section": section,
                "verifiedFacts": [
                    item.strip()
                    for item
                    in verified_facts
                ],
                "explanationSummary": (
                    explanation_summary
                    .strip()
                ),
                "sourcePages": sorted(
                    {
                        int(item)
                        for item
                        in source_pages
                    }
                ),
            }
        )

    normalized.sort(
        key=lambda item: (
            item["questionNo"]
        )
    )

    return {
        "page": expected_page,
        "answers": normalized,
    }


def analyze_webdesign_answer_page(
    image_path: Path,
    *,
    page_number: int,
    allow_api: bool = False,
    model: str = OPENAI_VISION_MODEL,
) -> Dict[str, Any]:
    image_path = Path(
        image_path
    )

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
        os.getenv(
            "STUDY_QUEST_NO_API"
        )
        == "1"
    ):
        raise RuntimeError(
            "STUDY_QUEST_NO_API=1 のため"
            "OpenAI APIを呼びません"
        )

    if not os.getenv(
        "OPENAI_API_KEY"
    ):
        raise RuntimeError(
            "OPENAI_API_KEY が"
            "設定されていません"
        )

    prompt = (
        build_webdesign_answer_prompt(
            page_number
        )
    )

    print(
        "[API CALL] "
        "webdesign answer vision "
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
                        "type": (
                            "input_text"
                        ),
                        "text": prompt,
                    },
                    {
                        "type": (
                            "input_image"
                        ),
                        "image_url": (
                            image_to_data_url(
                                image_path
                            )
                        ),
                    },
                ],
            }
        ],
    )

    response_text = (
        response.output_text
    )

    if not response_text:
        raise ValueError(
            "OpenAI APIから空の"
            "レスポンスが返されました"
        )

    parsed = _parse_json_response(
        response_text
    )

    return validate_webdesign_answers(
        parsed,
        expected_page=page_number,
    )


def get_answer_cache_path(
    document_id: str,
    page_number: int,
    *,
    cache_root: Path = (
        ROOT_DIR
        / "generated_materials"
        / "webdesign"
        / "answer_vision_cache"
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


def analyze_webdesign_answer_page_cached(
    image_path: Path,
    *,
    document_id: str,
    page_number: int,
    allow_api: bool = False,
    model: str = OPENAI_VISION_MODEL,
) -> Dict[str, Any]:
    cache_path = (
        get_answer_cache_path(
            document_id,
            page_number,
        )
    )

    if cache_path.exists():
        print(
            "[ANSWER CACHE] "
            f"{cache_path}"
        )

        data = json.loads(
            cache_path.read_text(
                encoding="utf-8"
            )
        )

        return validate_webdesign_answers(
            data,
            expected_page=page_number,
        )

    result = (
        analyze_webdesign_answer_page(
            image_path,
            page_number=page_number,
            allow_api=allow_api,
            model=model,
        )
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
        "[ANSWER CACHE SAVED] "
        f"{cache_path}"
    )

    return result
