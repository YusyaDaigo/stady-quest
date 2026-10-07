from typing import Any, Dict


EXAM_GENERATION_PROFILES: Dict[str, Dict[str, Any]] = {
    "drone": {
        "displayName": "二等無人航空機操縦士試験",

        # Study QUEST内部形式
        "subject": "drone",
        "defaultCategory": "COMMON",

        # 問題形式
        "choiceCount": 3,
        "answerIndexBase": 0,

        # 現在対応する難易度
        "difficultyMin": 3,
        "difficultyMax": 5,

        # Diagram Engine
        "supportedFigureTypes": [
            "none",
            "table",
            "line_chart",
            "bar_chart",
            "flowchart",
        ],

        # 問題生成方針
        "generationRules": [
            "教則第5版のみを根拠とする",
            "選択肢は3つとする",
            "正答は必ず1つにする",
            "既存問題と重複させない",
            "単純な用語暗記だけの問題を避ける",
            "複数の知識を組み合わせて判断させる",
            "ケース問題は作らない",
            "知識問題のみを作る",
            "出力はJSONのみにする",
        ],

        # セクション別の表示名
        "sections": {
            "mindset": "操縦者の心構え",
            "rule": "航空法規・飛行ルール",
            "system": "無人航空機のシステム",
            "operation": "運航",
            "risk": "安全管理・リスク",
        },

        # 出力先
        "generatedBaseDir": (
            "generated_questions/drone/common"
        ),
    },

    "webdesign": {
        "displayName": "ウェブデザイン技能検定3級",

        "subject": "webdesign",
        "defaultCategory": "HTML_CSS",

        "answerIndexBase": 0,

        "difficultyMin": 1,
        "difficultyMax": 5,

        "questionTypes": {
            "true_false": {
                "choiceCount": 2,
                "mockCount": 10,
            },
            "multiple_choice": {
                "choiceCount": 4,
                "mockCount": 15,
            },
        },

        "supportedFigureTypes": [
            "none",
            "table",
            "line_chart",
            "bar_chart",
            "flowchart",
        ],

        "generationRules": [
            "ウェブデザイン技能検定3級の出題範囲を逸脱しない",
            "正答は必ず1つにする",
            "既存問題や資料の文章をそのままコピーしない",
            "根拠資料から独立した表現で問題を作成する",
            "曖昧な選択肢を作らない",
            "正答の根拠を説明できる問題だけを作る",
            "出力はJSONのみにする",
        ],

        "sections": {
            "internet": "インターネット概論",
            "html_css": "HTML・CSS",
            "design": "ウェブデザイン",
            "accessibility": "アクセシビリティ",
            "operation": "運用・制作",
        },

        "categoryBySection": {
            "internet": "INTERNET",
            "html_css": "HTML_CSS",
            "design": "DESIGN",
            "accessibility": "ACCESSIBILITY",
            "operation": "OPERATION",
        },

        "generatedBaseDir": (
            "generated_questions/webdesign/theory"
        ),
    },

    "pharmacy": {
        "displayName": "薬剤師国家試験",

        "subject": "pharmacy",
        "defaultCategory": "REQUIRED",

        "choiceCount": 5,
        "answerIndexBase": 0,

        "difficultyMin": 1,
        "difficultyMax": 5,

        "supportedFigureTypes": [
            "none",
            "table",
            "line_chart",
            "bar_chart",
            "flowchart",
        ],

        "generationRules": [
            "薬剤師国家試験の出題範囲を逸脱しない",
            "正答は必ず1つにする",
            "既存問題をそのままコピーしない",
            "出力はJSONのみにする",
        ],

        "sections": {
            "required": "必須問題",
            "theory": "一般問題",
            "practical": "実践問題",
        },

        "generatedBaseDir": (
            "generated_questions/pharmacy"
        ),
    },
}


def get_exam_generation_profile(
    exam: str,
) -> Dict[str, Any]:
    """
    資格名から問題生成プロフィールを取得する。
    """

    if not isinstance(exam, str):
        raise ValueError(
            "exam must be a string"
        )

    normalized_exam = (
        exam.strip().lower()
    )

    if normalized_exam not in EXAM_GENERATION_PROFILES:
        raise ValueError(
            f"Unsupported exam: {exam}. "
            f"Supported exams: "
            f"{sorted(EXAM_GENERATION_PROFILES)}"
        )

    # 呼び出し側で誤って設定を書き換えないようコピーを返す。
    profile = EXAM_GENERATION_PROFILES[
        normalized_exam
    ]

    result = {
        **profile,
        "generationRules": list(
            profile["generationRules"]
        ),
        "supportedFigureTypes": list(
            profile["supportedFigureTypes"]
        ),
        "sections": dict(
            profile["sections"]
        ),
    }

    if "questionTypes" in profile:
        result["questionTypes"] = {
            key: dict(value)
            for key, value
            in profile["questionTypes"].items()
        }

    if "categoryBySection" in profile:
        result["categoryBySection"] = dict(
            profile["categoryBySection"]
        )

    return result


def validate_generation_request(
    exam: str,
    section: str,
    difficulty: int,
    count: int,
) -> Dict[str, Any]:
    """
    問題生成CLIから受け取った条件を検証する。
    """

    profile = get_exam_generation_profile(
        exam
    )

    normalized_section = (
        section.strip().lower()
    )

    if normalized_section not in profile["sections"]:
        raise ValueError(
            f"Unsupported section for {exam}: "
            f"{section}. "
            f"Supported sections: "
            f"{sorted(profile['sections'])}"
        )

    if not isinstance(difficulty, int):
        raise ValueError(
            "difficulty must be an integer"
        )

    if not (
        profile["difficultyMin"]
        <= difficulty
        <= profile["difficultyMax"]
    ):
        raise ValueError(
            "difficulty must be between "
            f"{profile['difficultyMin']} and "
            f"{profile['difficultyMax']}"
        )

    if not isinstance(count, int):
        raise ValueError(
            "count must be an integer"
        )

    if not (
        1
        <= count
        <= 50
    ):
        raise ValueError(
            "count must be between 1 and 50"
        )

    return {
        "exam": exam.strip().lower(),
        "section": normalized_section,
        "difficulty": difficulty,
        "count": count,
        "profile": profile,
    }
