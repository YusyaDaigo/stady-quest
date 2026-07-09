import { useState } from "react";

function Quiz({
  mode,
  examType,
  time,
  currentQuestion,
  showExplanation,
  handleAnswer,
  isCorrect,
  nextQuestion,
  prevQuestion,
  currentIndex,
  toggleBookmark,
  isBookmarked,
  jumpQuestion,
  totalQuestions,
  bookmarkedIndexes,
  userAnswers,
  finishExam
}) {
  const [showQuestionList, setShowQuestionList]
    = useState(false);

  return (
    <div>

      {/* 問題一覧サイドバー */}
      {showQuestionList && (
        <div
          style={{
            position: "fixed",
            right: "10px",
            top: "150px",
            width: "200px",
            height: "70vh",
            overflowY: "scroll",
            padding: "15px",
            backgroundColor: "#222",
            border: "1px solid #555",
            borderRadius: "10px",
            zIndex: 999
}}
        >
          <h3>問題一覧</h3>

          {Array.from(
            { length: totalQuestions },
            (_, index) => (
              <button
                key={index}
                onClick={() => {
                  jumpQuestion(index);
                }}
                style={{
                  display: "block",
                  width: "100%",
                  marginBottom: "8px",
                  textAlign: "left",

                  backgroundColor:
                    index === currentIndex
                      ? "#4a6fa5"
                      : "#2b2f3a",

                  color: "#ffffff",

                  border: "1px solid #444",

                  borderRadius: "8px",

                  padding: "8px 10px",

                  cursor: "pointer"
                }}
              >
                {index === currentIndex
                  ? "▶ "
                  : ""}
                {bookmarkedIndexes.includes(index)
                  ? "🔖 "
                  : ""}
                {userAnswers[index] === undefined
                  ? "⬜ "
                  : "✅ "}
                問題 {index + 1}
              </button>
            )
          )}
        </div>
      )}

      {/* サイドバー開閉ボタン */}
      <button
        onClick={() =>
          setShowQuestionList(
            (prev) => !prev
          )
        }
        style={{
          position: "fixed",
          right: showQuestionList
            ? "230px"
            : "20px",

          top: "85px",

          width: "48px",
          height: "48px",

          borderRadius: "50%",
          fontSize: "22px",

          zIndex: 1001
}}
      >
        {showQuestionList ? "▶" : "◀"}
      </button>

      {!currentQuestion ? (

        <div>
          <h2>
            問題がありません
          </h2>
        </div>

      ) : (

        <>

          <h2>
            {mode === "practice"
              ? "練習モード"
              : mode === "mock" && examType === "second"
              ? "二等操縦士 模試"
              : mode === "mock" && examType === "first"
              ? "一等操縦士 模試"
              : "復習モード"}
          </h2>

          <p>
            残り時間：
            {time}秒
          </p>

          <button onClick={toggleBookmark}>
            {isBookmarked
              ? "📌 栞済み"
              : "🔖 栞を付ける"}
          </button>

       {mode === "mock" && (
          <button
            onClick={() => {

              const unansweredCount =
                Array.from(
                  { length: totalQuestions },
                  (_, index) => userAnswers[index]
                ).filter(
                  (answer) => answer === undefined
                ).length;

              const message =
                unansweredCount > 0
                  ? `未回答問題が${unansweredCount}問あります。\nそれでも模試を終了しますか？`
                  : "模試を終了しますか？";

              const confirmFinish =
                window.confirm(message);

              if (confirmFinish) {
                finishExam();
              }
            }}
          >
            模試を終了する
          </button>
)}

          <h2
        
            style={{
              maxWidth: "820px",
              width: "82%",
              margin: "40px auto 32px",
              lineHeight: "1.7",
              textAlign: "left"
            }}
          >
            {currentQuestion.question}
          </h2>

          {currentQuestion.image && (
            <div
              style={{
                width: "92%",
                maxWidth: "920px",
                maxHeight: "58vh",
                overflow: "auto",
                margin: "20px auto",
                backgroundColor: "#ffffff",
                borderRadius: "10px",
                border: "1px solid #ddd"
              }}
            >
              <img
                src={currentQuestion.image}
                alt="問題図"
                style={{
                  display: "block",
                  width: "100%",
                  height: "auto",
                  objectFit: "contain"
                }}
              />
            </div>
          )}

          {currentQuestion.choices.map(
              (choice, index) => (

                <div key={index}>

                  <button
                    disabled={
                      showExplanation ||
                      userAnswers[currentIndex] !== undefined
                    }
                    onClick={() =>
                      handleAnswer(index)
                    }
                    style={{
                      backgroundColor:
                        userAnswers[currentIndex] === index
                          ? "#4a6fa5"
                          : "#2b2f3a",

                      color: "#ffffff",

                      border:
                        userAnswers[currentIndex] === index
                          ? "2px solid #ffffff"
                          : "1px solid #444",

                      borderRadius: "10px",

                      fontSize: "1.15rem",

                      padding: "16px 20px",

                      marginBottom: "14px",

                      maxWidth: "820px",

                      width: "90%",

                      lineHeight: "1.6",

                      textAlign: "left"
                    }}
                  >
                    {userAnswers[currentIndex] === index
                      ? "▶ "
                      : ""}
                    {choice}
                  </button>

                </div>
              )
            )}

            {showExplanation && (

              <div>

                <h1>
                  {isCorrect
                    ? "⭕ 正解！"
                    : "❌ 不正解"}
                </h1>

                <p>
                  正解：
                  {
                    currentQuestion.choices[
                      currentQuestion.answer
                    ]
                  }
                </p>

                <details
                  style={{
                    margin: "18px auto",
                    maxWidth: "820px",
                    width: "90%",
                    textAlign: "left",
                    backgroundColor: "#20242f",
                    border: "1px solid #444",
                    borderRadius: "12px",
                    padding: "14px 18px"
                  }}
                >
                  <summary
                    style={{
                      cursor: "pointer",
                      fontSize: "1.05rem",
                      fontWeight: "bold"
                    }}
                  >
                    解説を見る
                  </summary>

                  <p
                    style={{
                      marginTop: "14px",
                      lineHeight: "1.8",
                      color: "#d8dce6"
                    }}
                  >
                    {currentQuestion.explanation}
                  </p>
                </details>

                <button
                  onClick={() => {
                    nextQuestion();
                  }}
                  style={{
                    marginTop: "20px",
                    width: "180px",
                    minHeight: "48px",
                    fontSize: "1rem",
                    borderRadius: "12px",
                    padding: "10px 16px"
                  }}
                >
                  次へ →
                </button>

              </div>

            )}
        </>
      )}

    </div>
  );
}

export default Quiz;