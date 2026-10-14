import unittest

from tools.question_builder.prompt_builder import (
    build_rag_question_generation_prompt,
)
from tools.question_builder.continuous_quality_reviewer import (
    build_quality_review_prompt,
)


def make_knowledge(approved=True):
    return {
        "id": "webdesign-test-q007",
        "section": "html_css",
        "title": "CSS hsl",
        "text": "hsl()の第1引数は色相である。",
        "knowledgeQa": {"decision": "pass"},
        "factualVerificationRecord": "test-record",
        "humanReview": {
            "status": "approved" if approved else "pending",
            "approved": approved,
            "notes": [
                "TEST_NOTE_負の色相角も正規化する"
            ],
        },
    }


def make_prompt(difficulty, item=None, exam="webdesign"):
    return build_rag_question_generation_prompt(
        exam=exam,
        section="html_css" if exam == "webdesign" else "rule",
        section_display_name="HTML・CSS",
        difficulty=difficulty,
        count=1,
        keywords=["hsl"],
        knowledge_items=[item or make_knowledge()],
        question_type=(
            "multiple_choice"
            if exam == "webdesign"
            else None
        ),
    )


class WebDesignAdvancedPromptTests(unittest.TestCase):

    def test_approved_notes_are_included(self):
        prompt = make_prompt(4)

        self.assertIn(
            "TEST_NOTE_負の色相角も正規化する",
            prompt,
        )
        self.assertIn(
            "最低2種類の条件",
            prompt,
        )

    def test_unapproved_notes_are_excluded(self):
        prompt = make_prompt(
            4, make_knowledge(approved=False)
        )

        self.assertNotIn(
            "TEST_NOTE_負の色相角も正規化する",
            prompt,
        )

    def test_difficulty_five_has_distinct_rules(self):
        prompt = make_prompt(5)

        self.assertIn(
            "原則として複数Knowledge",
            prompt,
        )
        self.assertNotIn(
            "上級作問基準：★4",
            prompt,
        )

    def test_basic_difficulty_has_no_advanced_rules(self):
        prompt = make_prompt(3)

        self.assertNotIn(
            "WebDesign上級作問基準",
            prompt,
        )

    def test_drone_is_unaffected(self):
        item = {
            "id": "drone-test",
            "title": "飛行ルール",
            "text": "テスト用Knowledge",
        }

        prompt = make_prompt(
            4, item, exam="drone"
        )

        self.assertNotIn(
            "WebDesign上級作問基準",
            prompt,
        )

    def test_advanced_review_has_matching_rubric(self):
        prompt = build_quality_review_prompt(
            knowledge=make_knowledge(),
            question={
                "sourceKnowledgeIds": [
                    "webdesign-test-q007"
                ],
                "question": "テスト問題",
            },
            difficulty_min=1,
            difficulty_max=5,
            target_difficulty=4,
        )

        self.assertIn(
            "WebDesign上級問題の追加審査",
            prompt,
        )
        self.assertIn(
            "難易度不足ならdifficultyMatch=false",
            prompt,
        )

    def test_basic_review_has_no_advanced_rubric(self):
        prompt = build_quality_review_prompt(
            knowledge=make_knowledge(),
            question={"question": "テスト問題"},
            difficulty_min=1,
            difficulty_max=5,
            target_difficulty=3,
        )

        self.assertNotIn(
            "WebDesign上級問題の追加審査",
            prompt,
        )


if __name__ == "__main__":
    unittest.main()
