import { CATEGORIES } from "./questions";
import MenuButton from "../../components/MenuButton";
import MenuSection from "../../components/MenuSection";


function DroneMenu({
  startQuiz,
  mistakeQuestions,
  setMistakeQuestions,
}) {
  const hasMistakes =
    mistakeQuestions.length > 0;

  const practiceCategories = [
    {
      label: "全範囲",
      value: CATEGORIES.ALL,
    },
    {
      label: "規則",
      value: CATEGORIES.RULE,
    },
    {
      label: "システム",
      value: CATEGORIES.SYSTEM,
    },
    {
      label: "リスク管理",
      value: CATEGORIES.RISK,
    },
    {
      label: "計算",
      value: CATEGORIES.CALC,
    },
  ];

  const clearReviewList = () => {
    if (!hasMistakes) {
      return;
    }

    const confirmed = window.confirm(
      "復習リストをすべて削除しますか？"
    );

    if (!confirmed) {
      return;
    }

    setMistakeQuestions([]);
  };

  return (
    <div className="menu-page">
      <h2 className="menu-page__title">
        🚁 ドローン国家資格
      </h2>

      <p className="menu-page__description">
        練習・模試・復習モードを選択してください
      </p>

      <MenuSection
        title="📖 練習モード"
        description="学習したいジャンルを選択してください"
        grid
      >
        {practiceCategories.map((category) => (
          <MenuButton
            key={category.value}
            onClick={() =>
              startQuiz(
                "practice",
                null,
                category.value
              )
            }
          >
            {category.label}
          </MenuButton>
        ))}
      </MenuSection>

      <MenuSection
        title="📝 模試モード"
        description="受験する資格区分を選択してください"
      >
        <MenuButton
          onClick={() =>
            startQuiz("mock", "second")
          }
          variant="primary"
          wide
        >
          二等操縦士 模試
        </MenuButton>

        <MenuButton
          onClick={() =>
            startQuiz("mock", "first")
          }
          variant="primary"
          wide
        >
          一等操縦士 模試
        </MenuButton>
      </MenuSection>

      <MenuSection
        title="🔁 復習モード"
        description="間違えた問題を集中的に解き直します"
      >
        <div
          className={
            hasMistakes
              ? "review-status-card review-status-card--active"
              : "review-status-card"
          }
        >
          <p className="review-status-card__count">
            復習問題数：
            {mistakeQuestions.length}問
          </p>

          <p className="review-status-card__message">
            {hasMistakes
              ? "復習できる問題があります"
              : "現在、復習問題はありません"}
          </p>
        </div>

        <MenuButton
          onClick={() =>
            startQuiz("review")
          }
          disabled={!hasMistakes}
          variant="primary"
          wide
        >
          復習モード
          （{mistakeQuestions.length}問）
        </MenuButton>

        <MenuButton
          onClick={clearReviewList}
          disabled={!hasMistakes}
          variant="danger"
          wide
        >
          🗑 復習リスト削除
        </MenuButton>
      </MenuSection>
    </div>
  );
}

export default DroneMenu;
