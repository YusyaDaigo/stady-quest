import {
  webDesignPracticalTasks
} from "./practical/tasks";

function WebDesignMenu({
  onStartPracticalPractice,
  onStartPracticalMock
}) {
  const practicalTaskCount =
    webDesignPracticalTasks.length;

  const canStartMock =
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
          disabled
          style={{
            padding: "18px"
          }}
        >
          📘 学科試験
          <br />
          準備中
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
          disabled={!canStartMock}
          style={{
            padding: "18px"
          }}
        >
          🧪 実技 模試モード
          <br />
          5課題・60分
          {!canStartMock && (
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
