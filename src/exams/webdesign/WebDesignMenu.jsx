import MenuButton from "../../components/MenuButton";
import MenuSection from "../../components/MenuSection";

import {
  theoryQuestions
} from "./questions";

import {
  webDesignPracticalTasks
} from "./practical/tasks";

function WebDesignMenu({
  onStartTheoryPractice,
  onStartTheoryMock,
  onStartPracticalPractice,
  onStartPracticalMock
}) {
  const theoryQuestionCount =
    theoryQuestions.length;

  const practicalTaskCount =
    webDesignPracticalTasks.length;

  const canStartTheoryMock =
    theoryQuestionCount >= 25;

  const canStartPracticalMock =
    practicalTaskCount >= 5;

  return (
    <div className="menu-page">
      <h2 className="menu-page__title">
        🌐 ウェブデザイン技能検定
      </h2>

      <p className="menu-page__description">
        3級
      </p>

      <MenuSection
        title="📘 学科"
        description="学習したいモードを選択してください"
      >
        <MenuButton
          onClick={onStartTheoryPractice}
          wide
        >
          学科 練習モード
          <br />
          現在 {theoryQuestionCount}問
        </MenuButton>

        <MenuButton
          onClick={onStartTheoryMock}
          disabled={!canStartTheoryMock}
          variant="primary"
          wide
        >
          学科 模試モード
          <br />
          25問・45分
          {!canStartTheoryMock && (
            <>
              <br />
              現在 {theoryQuestionCount}/25問
            </>
          )}
        </MenuButton>
      </MenuSection>

      <MenuSection
        title="💻 実技"
        description="実技課題のモードを選択してください"
      >
        <MenuButton
          onClick={onStartPracticalPractice}
          wide
        >
          実技 練習モード
          <br />
          1課題・12分
        </MenuButton>

        <MenuButton
          onClick={onStartPracticalMock}
          disabled={!canStartPracticalMock}
          variant="primary"
          wide
        >
          実技 模試モード
          <br />
          5課題・60分
          {!canStartPracticalMock && (
            <>
              <br />
              現在 {practicalTaskCount}/5課題
            </>
          )}
        </MenuButton>
      </MenuSection>
    </div>
  );
}

export default WebDesignMenu;
