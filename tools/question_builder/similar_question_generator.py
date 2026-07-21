import json
from typing import Any, Dict


def build_similar_question_prompt(
    source_question: Dict[str, Any],
) -> str:
    """
    元問題1問分から、類題生成AIへ渡すプロンプトを作る。
    """

    if not isinstance(
        source_question,
        dict,
    ):
        raise ValueError(
            "source_question must be a dictionary"
        )

    required_fields = {
        "question",
        "choices",
        "answer",
        "explanation",
    }

    missing_fields = (
        required_fields
        - source_question.keys()
    )

    if missing_fields:
        raise ValueError(
            "source_question is missing required fields: "
            f"{sorted(missing_fields)}"
        )

    source_json = json.dumps(
        source_question,
        ensure_ascii=False,
        indent=2,
    )

    return f"""
あなたは薬剤師国家試験対策問題を作成する専門AIです。

以下の元問題を参考に、知識領域と難易度を維持しながら、
新しい類題を1問作成してください。

【重要ルール】

1. 元問題の文章や選択肢をそのままコピーしないこと。
2. 正答に必要な知識領域は維持すること。
3. 問題文、数値、条件、選択肢は適切に変更すること。
4. 正答は必ず1つにすること。
5. choices は文字列の配列にすること。
6. answer は0から始まる選択肢インデックスにすること。
7. explanation には正答理由を簡潔かつ正確に書くこと。
8. 出力はJSONのみとし、Markdownや説明文を付けないこと。

【図表について】

図表が不要な問題:
"figureType": "none"
"figureData": null

表:
"figureType": "table"

figureData:
{{
  "title": "表のタイトル",
  "headers": [
    "列1",
    "列2"
  ],
  "rows": [
    [
      "値1",
      "値2"
    ]
  ]
}}

折れ線グラフ:
"figureType": "line_chart"

figureData:
{{
  "title": "グラフタイトル",
  "xLabel": "X軸名",
  "yLabel": "Y軸名",
  "series": [
    {{
      "label": "系列名",
      "points": [
        [0, 0],
        [1, 5],
        [2, 3]
      ]
    }}
  ]
}}

棒グラフ:
"figureType": "bar_chart"

figureData:
{{
  "title": "グラフタイトル",
  "xLabel": "X軸名",
  "yLabel": "Y軸名",
  "categories": [
    "カテゴリA",
    "カテゴリB",
    "カテゴリC"
  ],
  "series": [
    {{
      "label": "系列名",
      "points": [
        [1, 10],
        [2, 20],
        [3, 15]
      ]
    }}
  ]
}}

フローチャート:
"figureType": "flowchart"

figureData:
{{
  "title": "フローチャートタイトル",
  "nodes": [
    {{
      "id": "a",
      "label": "開始"
    }},
    {{
      "id": "b",
      "label": "次の処理"
    }}
  ],
  "edges": [
    [
      "a",
      "b"
    ]
  ]
}}

figureType と figureData は必ず対応させること。

対応していない複雑な図を無理に生成しないこと。
その場合は、可能であれば文章問題へ変換すること。

【出力JSON形式】

{{
  "question": "問題文",
  "choices": [
    "選択肢1",
    "選択肢2",
    "選択肢3",
    "選択肢4",
    "選択肢5"
  ],
  "answer": 0,
  "explanation": "解説",
  "figureType": "none",
  "figureData": null
}}

【元問題】

{source_json}
""".strip()
