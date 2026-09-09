import base64
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from config import OPENAI_VISION_MODEL
from parsers.pdf_image_exporter import (
    export_pdf_pages_to_images,
)

load_dotenv()


QUESTION_RANGES = {
    "required": (1, 90),
    "theory": (91, 195),
    "practical": (196, 345),
}


SUBJECTS = (
    "物理",
    "化学",
    "生物",
    "衛生",
    "薬理",
    "薬剤",
    "病態",
    "法規",
    "実務",
)


def image_to_data_url(image_path: Path) -> str:
    image_bytes = image_path.read_bytes()
    encoded = base64.b64encode(
        image_bytes
    ).decode("utf-8")

    return f"data:image/png;base64,{encoded}"


def get_answer_cache_path(
    exam_number: int,
    category: str = "required",
) -> Path:
    return Path(
        "tools/question_builder/cache/"
        f"pharmacy/{category}/answers/"
        f"{exam_number}.json"
    )


def normalize_answer_data(
    data,
    category: str,
):
    if category not in QUESTION_RANGES:
        raise ValueError(
            f"未対応カテゴリです: {category}"
        )

    if (
        isinstance(data, dict)
        and "answers" in data
    ):
        data = data["answers"]

    if not isinstance(data, list):
        return {}

    start_no, end_no = QUESTION_RANGES[
        category
    ]

    answers = {}

    for item in data:
        try:
            question_no = int(
                item["question_no"]
            )

            if not (
                start_no
                <= question_no
                <= end_no
            ):
                continue

            raw_answer = item["answer"]

            if isinstance(raw_answer, list):
                values = [
                    int(value) - 1
                    for value in raw_answer
                ]

                if not values:
                    continue

                answer = (
                    values[0]
                    if len(values) == 1
                    else values
                )
            else:
                answer = int(raw_answer) - 1

            field = str(
                item.get("field", "")
            ).strip()

            if (
                field
                and field not in SUBJECTS
            ):
                field = ""

        except Exception:
            continue

        answer_info = {
            "field": field,
            "answer": answer,
        }

        required_selections = item.get(
            "requiredSelections"
        )

        if required_selections is not None:
            try:
                required_selections = int(
                    required_selections
                )

                if (
                    isinstance(answer, list)
                    and 1 <= required_selections
                    < len(answer)
                ):
                    answer_info[
                        "requiredSelections"
                    ] = required_selections
            except (TypeError, ValueError):
                pass

        answers[question_no] = answer_info

    return answers


def apply_special_scoring_overrides(
    answers: dict,
    exam_number: int,
    category: str,
):
    override_path = (
        Path(__file__).resolve().parents[1]
        / "manual"
        / "special_scoring_overrides.json"
    )

    if not override_path.exists():
        return answers

    override_data = json.loads(
        override_path.read_text(
            encoding="utf-8"
        )
    )

    exam_overrides = override_data.get(
        str(exam_number),
        {},
    )

    category_overrides = exam_overrides.get(
        category,
        {},
    )

    for question_no_text, override in (
        category_overrides.items()
    ):
        try:
            question_no = int(
                question_no_text
            )
        except (TypeError, ValueError):
            continue

        if question_no not in answers:
            continue

        override_answer = override.get(
            "answer"
        )

        if isinstance(override_answer, list):
            try:
                override_answer = [
                    int(value)
                    for value in override_answer
                ]
            except (TypeError, ValueError):
                override_answer = None

            if override_answer:
                answers[question_no][
                    "answer"
                ] = override_answer

        required_selections = override.get(
            "requiredSelections"
        )

        if required_selections is None:
            continue

        try:
            required_selections = int(
                required_selections
            )
        except (TypeError, ValueError):
            continue

        answer = answers[
            question_no
        ].get("answer")

        if (
            isinstance(answer, list)
            and 1 <= required_selections
            < len(answer)
        ):
            answers[question_no][
                "requiredSelections"
            ] = required_selections

    return answers


def parse_answers_with_vision(
    answer_pdf_path: Path,
    exam_number: int,
    category: str = "required",
):
    if category not in QUESTION_RANGES:
        raise ValueError(
            f"未対応カテゴリです: {category}"
        )

    cache_path = get_answer_cache_path(
        exam_number=exam_number,
        category=category,
    )

    if cache_path.exists():
        print(
            f"📦 解答cache使用: "
            f"{cache_path}"
        )

        cached_data = json.loads(
            cache_path.read_text(
                encoding="utf-8"
            )
        )

        answers = {
            int(key): value
            for key, value
            in cached_data.items()
        }

        return apply_special_scoring_overrides(
            answers=answers,
            exam_number=exam_number,
            category=category,
        )

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError(
            "OPENAI_API_KEY が設定されていません"
        )

    start_no, end_no = QUESTION_RANGES[
        category
    ]

    output_dir = Path(
        f"source_materials/pharmacy/"
        f"{category}/answer_images/"
        f"{exam_number}"
    )

    image_paths = export_pdf_pages_to_images(
        pdf_path=answer_pdf_path,
        output_dir=output_dir,
        max_pages=3,
    )

    client = OpenAI()
    answers = {}

    for image_path in image_paths:
        print(
            f"📄 解答表解析中: "
            f"{image_path}"
        )

        prompt = f"""
薬剤師国家試験の公式正答表画像です。

問{start_no}〜問{end_no}について、
問番号、科目、正答を抽出してください。

必ずJSONのみで返してください。

形式:
[
  {{
    "question_no": {start_no},
    "field": "物理",
    "answer": 1
  }},
  {{
    "question_no": {start_no + 1},
    "field": "化学",
    "answer": [2, 4]
  }},
  {{
    "question_no": {start_no + 2},
    "field": "生物",
    "answer": [1, 3, 5],
    "requiredSelections": 2
  }}
]

field は次のいずれかを使用してください。

物理
化学
生物
衛生
薬理
薬剤
病態
法規
実務

注意:
- answer は選択肢番号そのまま、
  1始まりで返してください。
- 正答が1つなら整数にしてください。
- 正答が複数なら配列にしてください。
- 正答欄に複数の候補が記載され、
  注記や脚注で
  「いずれかNつ選択で正解」
  と明示されている場合のみ、
  "requiredSelections": N
  を追加してください。
- requiredSelections は、
  正答候補数より少ない選択数を
  公式に要求している場合だけ使用してください。
- 注記がない通常の複数正答では
  requiredSelections を付けないでください。
- 読み取れない脚注や注記を推測して
  requiredSelections を付けないでください。
- 問{start_no}未満と問{end_no}を超える問題は
  含めないでください。
- 「解なし」など正答が存在しない問題は
  含めないでください。
- 読み取れない内容は推測せず省略してください。
"""

        response = client.responses.create(
            model=OPENAI_VISION_MODEL,
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
                            "image_url":
                                image_to_data_url(
                                    image_path
                                ),
                        },
                    ],
                }
            ],
        )

        data = json.loads(
            response.output_text
        )

        answers.update(
            normalize_answer_data(
                data=data,
                category=category,
            )
        )

    answers = apply_special_scoring_overrides(
        answers=answers,
        exam_number=exam_number,
        category=category,
    )

    cache_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    cache_path.write_text(
        json.dumps(
            answers,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(
        f"💾 解答cache保存: "
        f"{cache_path}"
    )

    expected_count = (
        end_no - start_no + 1
    )

    print(
        f"📘 Vision解答抽出: "
        f"{category} "
        f"{len(answers)}/"
        f"{expected_count}問"
    )

    return answers


def parse_required_answers_with_vision(
    answer_pdf_path: Path,
    exam_number: int,
):
    """
    既存コードとの互換用。
    """

    return parse_answers_with_vision(
        answer_pdf_path=answer_pdf_path,
        exam_number=exam_number,
        category="required",
    )
