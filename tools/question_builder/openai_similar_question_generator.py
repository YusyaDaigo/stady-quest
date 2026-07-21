from typing import Any, Dict

from tools.question_builder.generators import (
    PharmacySimilarGenerator,
)


_generator = PharmacySimilarGenerator()


def generate_similar_question(
    source_question: Dict[str, Any],
    *,
    allow_api: bool = False,
    use_cache: bool = True,
) -> Dict[str, Any]:
    """
    元問題1問から薬剤師国家試験の類題を1問生成する。

    安全仕様:
    - キャッシュがあればAPIを呼ばず再利用する
    - allow_api=False がデフォルト
    - allow_api=True の場合のみAPIを呼ぶ
    - 1プロセスあたり最大1回のみAPIを許可する
    """

    return _generator.generate(
        input_data=source_question,
        allow_api=allow_api,
        use_cache=use_cache,
    )
