import base64
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from config import OPENAI_VISION_MODEL, PHARMACY_FIELD_ALIASES

load_dotenv()


CATEGORY_LABELS = {
    "required": "必須問題",
    "theory": "一般理論問題",
    "practical": "一般実践問題",
}


EXAM_MARKUP_INSTRUCTIONS = """
問題文中の下線・空欄について:
- 元画像で、ア・イ・ウ・エ・オなどのラベルに対応する
  下線が実際に引かれている場合、その範囲を次の専用記法で
  question に記録してください。

  [[ラベル|下線部分]]

  例:
  [[ア|0.5 mol/L硫酸]]
  [[イ|液の赤色が消えたとき]]
  [[ウ|A（mL）]]

- ラベル付きの空欄が実際に存在する場合は、
  次のように内容を空にしてください。

  [[ラベル|]]

  例:
  [[オ|]]

- ラベルは元画像に表示されている文字をそのまま使用してください。
- 下線の範囲は、元画像で実際に下線が引かれている文字だけにしてください。
- 下線の前後にある通常の文章まで記法の中へ含めないでください。
- 元画像に下線・空欄が存在しない箇所へ、
  文脈や選択肢から推測してこの記法を追加してはいけません。
- 選択肢に「下線部ア」「空欄オ」などと書かれているだけでは、
  対応する下線・空欄が画像上で確認できない限り、
  推測で記法を作ってはいけません。
- 「下線部ア：○○」のような説明文へ置き換えず、
  元の問題文の位置に [[ア|○○]] を埋め込んでください。
- choices 内の「下線部ア」「空欄オ」などの参照表現は、
  原文どおり保持してください。
- HTMLタグは使用しないでください。
- [[...|...]] の内部へ別の [[...|...]] を入れないでください。
"""


def normalize_field(field: str) -> str:
    return PHARMACY_FIELD_ALIASES.get(field, field)


def validate_exam_markup(text: str) -> bool:
    """
    [[ラベル|内容]] 形式の試験用マークアップが
    壊れていないか確認する。
    """

    if not isinstance(text, str):
        return False

    open_count = text.count("[[")
    close_count = text.count("]]")

    if open_count != close_count:
        return False

    if open_count == 0:
        return True

    import re

    pattern = re.compile(
        r"\[\[([^|\[\]]+)\|([^\[\]]*)\]\]"
    )

    matches = list(pattern.finditer(text))

    if len(matches) != open_count:
        return False

    for match in matches:
        label = match.group(1).strip()

        if not label:
            return False

    return True


def image_to_data_url(image_path: Path) -> str:
    image_bytes = image_path.read_bytes()
    encoded = base64.b64encode(image_bytes).decode("utf-8")
    return f"data:image/png;base64,{encoded}"

def detect_image_choice_count(
    image_path: Path,
    question_no: int,
) -> int:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY が設定されていません")

    client = OpenAI()
    image_data_url = image_to_data_url(image_path)

    prompt = f"""
薬剤師国家試験の問題ページ画像です。

問{question_no}について確認してください。

この問題の選択肢が、文章ではなく図・グラフ・構造式・画像などで
表現されている場合、画像内で確認できる選択肢の個数だけを数えてください。

必ずJSONのみで返してください。

形式:
{{
  "choice_count": 5
}}

ルール:
- 実際に確認できる選択肢だけを数えてください。
- 推測で個数を補わないでください。
- 選択肢を確認できない場合は 0 を返してください。
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
                        "image_url": image_data_url,
                    },
                ],
            }
        ],
    )

    data = json.loads(response.output_text)

    try:
        return int(data.get("choice_count", 0))
    except Exception:
        return 0

def analyze_page(
    image_path,
    category: str = "required",
):
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY が設定されていません")

    if category not in CATEGORY_LABELS:
        raise ValueError(
            f"未対応カテゴリです: {category}"
        )

    client = OpenAI()
    image_path = Path(image_path)
    image_data_url = image_to_data_url(image_path)

    category_label = CATEGORY_LABELS[category]

    prompt = f"""
薬剤師国家試験の{category_label}ページ画像です。

画像内に見えている問題をすべて抽出してください。

{EXAM_MARKUP_INSTRUCTIONS}

必ずJSONのみで返してください。

形式:
[
  {{
    "question_no": 1,
    "field": "物理",
    "question": "問題文",
    "choices": [
      "選択肢1",
      "選択肢2",
      "選択肢3",
      "選択肢4",
      "選択肢5"
    ],
    "has_image": false
  }}
]

fieldは次のいずれかに正規化してください:
物理, 化学, 生物, 衛生, 薬理, 薬剤, 病態・薬物治療, 法規・制度・倫理, 実務

has_image は、問題を解くために図、表、グラフ、写真、構造式、
波形、模式図などの画像情報が必要な場合は true にしてください。
問題文と文字の選択肢だけで解ける場合は false にしてください。

重要:
- 選択肢が文章の場合は、choices に選択肢本文をそのまま入れてください。
- 選択肢そのものが図、グラフ、構造式、画像などの場合でも、
  choices を空配列にしないでください。
- 画像選択肢の場合は、画像内に見える選択肢の個数を数え、
  次のような文字列を choices に入れてください。
  例:
  [
    "選択肢1（画像）",
    "選択肢2（画像）",
    "選択肢3（画像）",
    "選択肢4（画像）",
    "選択肢5（画像）"
  ]
- 「1つ選べ」「2つ選べ」などの指示から正答数を推測して
  choices の個数を決めないでください。
- 実際に画像内で確認できる選択肢番号・選択肢数に従ってください。
- 問題がページ途中で切れており、選択肢を確認できない場合は
  見えていない選択肢を作らないでください。
- 見えていない問題は作らないでください。
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
                        "image_url": image_data_url,
                    },
                ],
            }
        ],
    )

    data = json.loads(response.output_text)

    if isinstance(data, dict):
        if "questions" in data:
            questions = data["questions"]
        else:
            questions = [data]
    elif isinstance(data, list):
        questions = data
    else:
        raise ValueError(
            f"OpenAI Visionの返答形式が不正です: {type(data)}"
        )

    normalized_questions = []

    for question in questions:
        if not isinstance(question, dict):
            print(
                f"⚠️ 不正な問題データをスキップ: {question}"
            )
            continue

        question["field"] = normalize_field(
            question.get("field", "")
        )

        question["has_image"] = bool(
            question.get("has_image", False)
        )

        choices = question.get("choices")

        if not isinstance(choices, list):
            choices = []

        if (
            len(choices) < 2
            and question["has_image"]
        ):
            question_no = question.get("question_no")

            if isinstance(question_no, int):
                choice_count = detect_image_choice_count(
                    image_path=image_path,
                    question_no=question_no,
                )

                if choice_count >= 2:
                    choices = [
                        f"選択肢{index}（画像）"
                        for index in range(
                            1,
                            choice_count + 1,
                        )
                    ]

        question["choices"] = choices

        question_text = question.get(
            "question",
            "",
        )

        if not validate_exam_markup(
            question_text
        ):
            question_no = question.get(
                "question_no",
                "?",
            )

            raise ValueError(
                "試験マークアップ形式が不正です: "
                f"問{question_no}"
            )

        normalized_questions.append(question)

    return normalized_questions


def analyze_question_across_pages(
    current_image_path,
    next_image_path,
    question_no: int,
    category: str = "required",
):
    """
    1問が2ページにまたがる場合のフォールバック解析。

    current_image_path:
        問題文が始まるページ

    next_image_path:
        問題文・選択肢の続きがある次ページ

    question_no:
        完成させたい対象問題番号
    """

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY が設定されていません")

    if category not in CATEGORY_LABELS:
        raise ValueError(
            f"未対応カテゴリです: {category}"
        )

    current_image_path = Path(current_image_path)
    next_image_path = Path(next_image_path)

    client = OpenAI()

    current_image_data_url = image_to_data_url(
        current_image_path
    )
    next_image_data_url = image_to_data_url(
        next_image_path
    )

    category_label = CATEGORY_LABELS[category]

    prompt = f"""
薬剤師国家試験の{category_label}です。

以下の2枚の画像は連続したページです。

対象は問{question_no}だけです。

1枚目で始まった問{question_no}が2枚目へ続いている可能性があります。
2ページを合わせて読み、問{question_no}を1つの完全な問題として抽出してください。

{EXAM_MARKUP_INSTRUCTIONS}

必ずJSONのみで返してください。

形式:
{{
  "question_no": {question_no},
  "field": "科目",
  "question": "2ページを統合した完全な問題文",
  "choices": [
    "選択肢1",
    "選択肢2",
    "選択肢3",
    "選択肢4",
    "選択肢5"
  ],
  "has_image": true
}}

ルール:
- 問{question_no}以外の問題は返さないでください。
- 1枚目と2枚目の内容を時系列どおり統合してください。
- 問題文が2ページ目へ続いている場合は、その文章もquestionへ含めてください。
- 対象問題が「前問」「前の問題」「前ページ」「上記」など、
  他の問題やページを参照している場合は、
  問題を単独で理解して解答するために必要な前提本文を
  周辺ページからquestionへ統合してください。
- 必要な前提をquestionへ統合した場合は、
  「前問の定量法において」のような参照表現をそのまま残さず、
  「この定量法において」など、
  統合後の文章だけで意味が通る自然な表現へ置き換えてください。
- 参照表現を書き換える場合も、
  元問題の意味・数値・条件・問い方を変更してはいけません。
- 問題を解くために不要な前問の設問文や選択肢は
  questionへ追加しないでください。
- 選択肢が2ページ目にある場合は、必ずchoicesへ含めてください。
- 選択肢本文は省略せず、画像から読み取れる内容を入れてください。
- 選択肢に構造式・グラフ・図などが含まれる場合、
  文字で表現できる部分は文字として記録してください。
- 問題を解くために図・表・グラフ・構造式などが必要なら
  has_imageをtrueにしてください。
- 見えていない内容を推測で追加しないでください。

fieldは次のいずれかに正規化してください:
物理, 化学, 生物, 衛生, 薬理, 薬剤,
病態・薬物治療, 法規・制度・倫理, 実務
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
                        "image_url": current_image_data_url,
                    },
                    {
                        "type": "input_image",
                        "image_url": next_image_data_url,
                    },
                ],
            }
        ],
    )

    data = json.loads(response.output_text)

    if isinstance(data, dict) and "questions" in data:
        questions = data["questions"]

        if not questions:
            return None

        data = questions[0]

    if not isinstance(data, dict):
        raise ValueError(
            "2ページVisionの返答形式が不正です"
        )

    try:
        returned_question_no = int(
            data.get("question_no")
        )
    except (TypeError, ValueError):
        return None

    if returned_question_no != question_no:
        return None

    data["question_no"] = returned_question_no

    data["field"] = normalize_field(
        data.get("field", "")
    )

    data["has_image"] = bool(
        data.get("has_image", False)
    )

    choices = data.get("choices")

    if not isinstance(choices, list):
        choices = []

    data["choices"] = choices

    question_text = data.get(
        "question",
        "",
    )

    if not validate_exam_markup(
        question_text
    ):
        raise ValueError(
            "試験マークアップ形式が不正です: "
            f"問{question_no}"
        )

    return data


def analyze_question_across_page_set(
    image_paths,
    question_no: int,
    category: str = "required",
):
    """
    1問が複数ページにまたがる場合のフォールバック解析。

    image_paths:
        問題開始ページから連続した最大3ページ程度を渡す。
    """

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY が設定されていません")

    if category not in CATEGORY_LABELS:
        raise ValueError(
            f"未対応カテゴリです: {category}"
        )

    image_paths = [
        Path(image_path)
        for image_path in image_paths
    ]

    if not image_paths:
        return None

    client = OpenAI()
    category_label = CATEGORY_LABELS[category]

    prompt = f"""
薬剤師国家試験の{category_label}です。

以下の画像は連続したページです。

対象は問{question_no}だけです。

問{question_no}が複数ページにまたがっている可能性があります。
すべてのページを合わせて読み、
問{question_no}を1つの完全な問題として抽出してください。

{EXAM_MARKUP_INSTRUCTIONS}

必ずJSONのみで返してください。

形式:
{{
  "question_no": {question_no},
  "field": "科目",
  "question": "複数ページを統合した完全な問題文",
  "choices": [
    "選択肢1",
    "選択肢2",
    "選択肢3",
    "選択肢4",
    "選択肢5"
  ],
  "has_image": true
}}

ルール:
- 問{question_no}以外の問題は返さないでください。
- ページ順に内容を統合してください。
- 問題文の続きもquestionへ含めてください。
- 対象問題の設問が「この定量法」「この方法」「この操作」
  「この反応」「この実験」「この図」「この表」「前問」
  「前の問題」「前ページ」「上記」など、
  前ページや周辺ページの内容を前提としている場合は、
  問題を単独で理解して解答するために必要な前提本文も
  questionへ統合してください。
- 必要な前提をquestionへ統合した場合は、
  「前問の定量法において」のような参照表現をそのまま残さず、
  「この定量法において」など、
  統合後の文章だけで意味が通る自然な表現へ置き換えてください。
- 参照表現を書き換える場合も、
  元問題の意味・数値・条件・問い方を変更してはいけません。
- 問題を解くために不要な前問の設問文や選択肢は
  questionへ追加しないでください。
- 選択肢中に「下線部ア」「下線部イ」「下線部ウ」
  「下線部エ」「空欄オ」などの参照表現がある場合は、
  それらが何を指しているか理解できるよう、
  対応する本文・式・操作・条件をquestionへ含めてください。
- ただし、対象問題と無関係な前問や次問の本文は
  questionへ混入させないでください。
- 元画像に存在しない説明や情報を補完・推測してはいけません。
- 選択肢が後続ページにある場合は必ずchoicesへ含めてください。
- 選択肢本文は省略しないでください。
- 構造式・図・グラフなど文字だけで完全に表現できない選択肢でも、
  選択肢番号ごとの区別ができる形でchoicesへ登録してください。
- 問題を解くために図・表・グラフ・構造式などが必要なら
  has_imageをtrueにしてください。
- 見えていない内容を推測で追加しないでください。

fieldは次のいずれかに正規化してください:
物理, 化学, 生物, 衛生, 薬理, 薬剤,
病態・薬物治療, 法規・制度・倫理, 実務
"""

    content = [
        {
            "type": "input_text",
            "text": prompt,
        }
    ]

    for image_path in image_paths:
        content.append(
            {
                "type": "input_image",
                "image_url": image_to_data_url(image_path),
            }
        )

    response = client.responses.create(
        model=OPENAI_VISION_MODEL,
        input=[
            {
                "role": "user",
                "content": content,
            }
        ],
    )

    data = json.loads(response.output_text)

    if isinstance(data, dict) and "questions" in data:
        questions = data["questions"]

        if not questions:
            return None

        data = questions[0]

    if not isinstance(data, dict):
        return None

    try:
        returned_question_no = int(
            data.get("question_no")
        )
    except (TypeError, ValueError):
        return None

    if returned_question_no != question_no:
        return None

    data["question_no"] = returned_question_no
    data["field"] = normalize_field(
        data.get("field", "")
    )
    data["has_image"] = bool(
        data.get("has_image", False)
    )

    choices = data.get("choices")

    if not isinstance(choices, list):
        choices = []

    data["choices"] = choices

    question_text = data.get(
        "question",
        "",
    )

    if not validate_exam_markup(
        question_text
    ):
        raise ValueError(
            "試験マークアップ形式が不正です: "
            f"問{question_no}"
        )

    return data


def analyze_practical_case(
    image_paths,
    first_question_no: int,
    second_question_no: int,
):
    """
    薬剤師国家試験・実践問題の
    2問1組ケースを複数ページから解析する。

    目的:
    - 2問に共通する症例・処方・状況を case_context として抽出
    - 各問題固有の設問文と選択肢を分離
    - ケース単位で再構築できる情報を返す

    API実行専用関数。
    """

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError(
            "OPENAI_API_KEY が設定されていません"
        )

    image_paths = [
        Path(image_path)
        for image_path in image_paths
    ]

    if not image_paths:
        raise ValueError(
            "解析対象画像がありません"
        )

    client = OpenAI()

    image_contents = []

    for image_path in image_paths:
        image_contents.append(
            {
                "type": "input_image",
                "image_url": image_to_data_url(
                    image_path
                ),
            }
        )

    case_id = (
        f"111-"
        f"{first_question_no}-"
        f"{second_question_no}"
    )

    prompt = f"""
薬剤師国家試験の実践問題を解析してください。

対象は次の2問1組のケースです。

問{first_question_no}
問{second_question_no}

実践問題では、症例、患者背景、処方内容、検査値、
薬歴、医療現場の状況などが2問に共通して提示され、
その共通情報を前提として2つの設問が出題されることがあります。

今回の最重要目的は、
2問に共通して必要となる情報を
case_context として正確に復元することです。

複数画像はPDF上の連続ページです。
ページをまたいでいる場合も含め、
画像全体を時系列順に読んでください。

必ずJSONのみで返してください。

形式:

{{
  "case_id": "{case_id}",
  "case_context": "2問に共通する症例・処方・状況など",
  "questions": [
    {{
      "question_no": {first_question_no},
      "field": "科目",
      "question": "問{first_question_no}固有の設問文",
      "choices": [
        "選択肢1",
        "選択肢2",
        "選択肢3",
        "選択肢4",
        "選択肢5"
      ],
      "has_image": false
    }},
    {{
      "question_no": {second_question_no},
      "field": "科目",
      "question": "問{second_question_no}固有の設問文",
      "choices": [
        "選択肢1",
        "選択肢2",
        "選択肢3",
        "選択肢4",
        "選択肢5"
      ],
      "has_image": false
    }}
  ]
}}

重要ルール:

- case_contextには、2問を理解するために必要な共通情報だけを入れてください。
- 患者背景、年齢、性別、症状、既往歴、薬歴、処方内容、
  検査値、経過、医療者の行動などは必要に応じて省略せず含めてください。
- 各questionには、その問題固有の問いだけを入れてください。
- case_contextとquestionを重複させないでください。
- 処方内容の薬剤名、用量、用法、日数を勝手に省略しないでください。
- 数値、単位、薬剤名を推測で変更しないでください。
- 選択肢は画像に存在する内容を省略せず記録してください。
- 問{first_question_no}または問{second_question_no}の情報が
  画像内に存在しない場合、推測で補完しないでください。
- 2問共通の図・表・構造式などが問題を解くために必要な場合、
  該当問題のhas_imageをtrueにしてください。
- 見えていない情報は絶対に推測しないでください。

fieldは次のいずれかに正規化してください:

物理
化学
生物
衛生
薬理
薬剤
病態・薬物治療
法規・制度・倫理
実務
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
                    *image_contents,
                ],
            }
        ],
    )

    data = json.loads(
        response.output_text
    )

    if not isinstance(data, dict):
        raise ValueError(
            "ケースVisionの返答形式が不正です"
        )

    case_context = data.get(
        "case_context",
        "",
    )

    if not isinstance(case_context, str):
        raise ValueError(
            "case_contextの形式が不正です"
        )

    case_context = case_context.strip()

    if not case_context:
        raise ValueError(
            "case_contextが空です"
        )

    questions = data.get(
        "questions",
        [],
    )

    if not isinstance(questions, list):
        raise ValueError(
            "questionsの形式が不正です"
        )

    normalized_questions = []

    allowed_question_numbers = {
        first_question_no,
        second_question_no,
    }

    for question in questions:

        if not isinstance(question, dict):
            continue

        try:
            question_no = int(
                question.get("question_no")
            )
        except (TypeError, ValueError):
            continue

        if question_no not in allowed_question_numbers:
            continue

        normalized_question = dict(
            question
        )

        normalized_question[
            "question_no"
        ] = question_no

        normalized_question[
            "field"
        ] = normalize_field(
            question.get("field", "")
        )

        normalized_question[
            "has_image"
        ] = bool(
            question.get(
                "has_image",
                False,
            )
        )

        normalized_questions.append(
            normalized_question
        )

    return {
        "case_id": case_id,
        "case_context": case_context,
        "questions": normalized_questions,
    }
