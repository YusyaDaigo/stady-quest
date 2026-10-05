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
    <div>
      <h2>
        🌐 ウェブデザイン技能検定
      </h2>

      <h3>3級</h3>

      <div
        style={{
          display: "grid",
          gap: "16px",
          maxWidth: "560px",
          margin: "30px auto"
        }}
      >
        <button
          onClick={
            onStartTheoryPractice
          }
          style={{
            padding: "18px"
          }}
        >
          📘 学科 練習モード
          <br />
          現在
          {" "}
          {theoryQuestionCount}
          問
        </button>

        <button
          onClick={
            onStartTheoryMock
          }
          disabled={
            !canStartTheoryMock
          }
          style={{
            padding: "18px"
          }}
        >
          📝 学科 模試モード
          <br />
          25問・45分
          {!canStartTheoryMock && (
            <>
              <br />
              現在
              {" "}
              {theoryQuestionCount}
              /25問
            </>
          )}
        </button>

        <button
          onClick={
            onStartPracticalPractice
          }
          style={{
            padding: "18px"
          }}
        >
          💻 実技 練習モード
          <br />
          1課題・12分
        </button>

        <button
          onClick={
            onStartPracticalMock
          }
          disabled={
            !canStartPracticalMock
          }
          style={{
            padding: "18px"
          }}
        >
          🧪 実技 模試モード
          <br />
          5課題・60分
          {!canStartPracticalMock && (
            <>
              <br />
              現在
              {" "}
              {practicalTaskCount}
              /5課題
            </>
          )}
        </button>
      </div>
    </div>
  );
}

export default WebDesignMenu;
