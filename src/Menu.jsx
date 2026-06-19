import { CATEGORIES } from "./questions/index";

function Menu({
  startQuiz,
  mistakeQuestions,
  setMistakeQuestions
}) {

  return (
    <div>

      <h2>メインメニュー</h2>

      <div
        style={{
          margin: "20px auto",
          padding: "14px 18px",
          maxWidth: "360px",
          borderRadius: "12px",
          backgroundColor:
            mistakeQuestions.length > 0
              ? "#3a2f1f"
              : "#222",
          border:
            mistakeQuestions.length > 0
              ? "2px solid #d6a84f"
              : "1px solid #444"
        }}
      >
        <strong>
          復習問題数：
          {mistakeQuestions.length} 問
        </strong>

        <p
          style={{
            marginBottom: 0,
            color:
              mistakeQuestions.length > 0
                ? "#ffd98a"
                : "#aaa"
          }}
        >
          {mistakeQuestions.length > 0
            ? "復習できる問題があります"
            : "現在、復習問題はありません"}
        </p>
      </div>

      <h3>練習モード</h3>

      <button
        onClick={() =>
          startQuiz(
            "practice",
            null,
            CATEGORIES.ALL
          )
        }
      >
        全範囲
      </button>

      <button
        onClick={() =>
          startQuiz(
            "practice",
            null,
            CATEGORIES.RULE
          )
        }
      >
        規則
      </button>

      <button
        onClick={() =>
          startQuiz(
            "practice",
            null,
            CATEGORIES.SYSTEM
          )
        }
      >
        システム
      </button>

      <button
        onClick={() =>
          startQuiz(
            "practice",
            null,
            CATEGORIES.RISK
          )
        }
      >
        リスク管理
      </button>

      <button
        onClick={() =>
          startQuiz(
            "practice",
            null,
            CATEGORIES.CALC
          )
        }
      >
        計算
      </button>

      <h3>模試モード</h3>

      <button
        onClick={() =>
          startQuiz("mock", "second")
        }
      >
        二等操縦士 模試
      </button>

      <button
        onClick={() =>
          startQuiz("mock", "first")
        }
      >
        一等操縦士 模試
      </button>

      <h3>復習モード</h3>

      <button
        onClick={() =>
          startQuiz("review")
        }
      >
        復習モード
      </button>

      <button
        onClick={() => {
          setMistakeQuestions([]);
        }}
      >
        復習リスト削除
      </button>

    </div>
  );
}

export default Menu;