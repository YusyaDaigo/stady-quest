function Menu({
  startQuiz,
  mistakeQuestions,
  setMistakeQuestions
}) {

  return (
    <div>

      <h2>メインメニュー</h2>

      <p>
        復習問題数：
        {mistakeQuestions.length}
      </p>

      <button
        onClick={() =>
          startQuiz("practice")
        }
      >
        練習モード
      </button>

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