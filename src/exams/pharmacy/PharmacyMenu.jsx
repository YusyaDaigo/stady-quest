import MenuButton from "../../components/MenuButton";
import MenuSection from "../../components/MenuSection";


function PharmacyMenu({
  onStartRequiredPractice,
  onStartTheoryPractice,
  onStartPracticalPractice,
  onStartRequiredMock,
  onStartTheoryPart1Mock,
  onStartTheoryPart2Mock,
  onStartPracticalPart1Mock,
  onStartPracticalPart2Mock,
  onStartPracticalPart3CaseMock,
  onStartPracticalPart3SingleMock,
  onStartReview,
  onClearReview,
  mistakeCount,
}) {
  const fields = [
    { label: "全範囲", value: "ALL" },
    { label: "物理", value: "物理" },
    { label: "化学", value: "化学" },
    { label: "生物", value: "生物" },
    { label: "衛生", value: "衛生" },
    { label: "薬理", value: "薬理" },
    { label: "薬剤", value: "薬剤" },
    { label: "病態", value: "病態" },
    { label: "法規", value: "法規" },
    { label: "実務", value: "実務" },
  ];

  const theoryFields = fields.filter(
    (field) => field.value !== "実務"
  );

  const hasMistakes = mistakeCount > 0;

  return (
    <div className="menu-page">
      <h2 className="menu-page__title">
        💊 薬剤師国家試験
      </h2>

      <p className="menu-page__description">
        必須問題に対応中
      </p>

      <MenuSection
        title="📖 必須問題 練習"
        description="学習したい科目を選択してください"
        grid
      >
        {fields.map((field) => (
          <MenuButton
            key={field.value}
            onClick={() =>
              onStartRequiredPractice(field.value)
            }
          >
            {field.label}
          </MenuButton>
        ))}
      </MenuSection>

      <MenuSection
        title="📘 理論問題 練習"
        description="学習したい科目を選択してください"
        grid
      >
        {theoryFields.map((field) => (
          <MenuButton
            key={field.value}
            onClick={() =>
              onStartTheoryPractice(field.value)
            }
          >
            {field.label}
          </MenuButton>
        ))}
      </MenuSection>

      <MenuSection
        title="🩺 実践問題 練習"
        description="学習したい科目を選択してください"
        grid
      >
        {fields.map((field) => (
          <MenuButton
            key={field.value}
            onClick={() =>
              onStartPracticalPractice(field.value)
            }
          >
            {field.label}
          </MenuButton>
        ))}
      </MenuSection>

      <MenuSection
        title="📝 必須問題 模試"
        description="本番と同じ科目配分で90問を出題します"
      >
        <MenuButton
          onClick={onStartRequiredMock}
          variant="primary"
          wide
        >
          本番形式 90問
        </MenuButton>
      </MenuSection>

      <MenuSection
        title="🧠 理論問題 模試"
        description="本番形式のPart構成で出題します"
      >
        <MenuButton
          onClick={onStartTheoryPart1Mock}
          variant="primary"
          wide
        >
          Part1 60問・150分
        </MenuButton>

        <MenuButton
          onClick={onStartTheoryPart2Mock}
          variant="primary"
          wide
        >
          Part2 45問・115分
        </MenuButton>
      </MenuSection>

      <MenuSection
        title="🩺 実践問題 模試"
        description="本番形式のPart構成で出題します"
      >
        <MenuButton
          onClick={onStartPracticalPart1Mock}
          variant="primary"
          wide
        >
          Part1 50問・125分
        </MenuButton>

        <MenuButton
          onClick={onStartPracticalPart2Mock}
          variant="primary"
          wide
        >
          Part2 40問・100分
        </MenuButton>

        <MenuButton
          onClick={onStartPracticalPart3CaseMock}
          variant="primary"
          wide
        >
          Part3① 症例問題 40問・100分
        </MenuButton>

        <MenuButton
          onClick={onStartPracticalPart3SingleMock}
          variant="primary"
          wide
        >
          Part3② 単問 20問・50分
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
            復習問題数：{mistakeCount}問
          </p>

          <p className="review-status-card__message">
            {hasMistakes
              ? "復習できる問題があります"
              : "現在、復習問題はありません"}
          </p>
        </div>

        <MenuButton
          onClick={onStartReview}
          disabled={!hasMistakes}
          variant="primary"
          wide
        >
          間違えた問題を復習
          （{mistakeCount}問）
        </MenuButton>

        <MenuButton
          onClick={onClearReview}
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

export default PharmacyMenu;
