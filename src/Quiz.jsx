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
            top: "140px",
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
                onClick={() =>
                  jumpQuestion(index)
                }
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
            : "10px",
          top: "50%",
          transform: "translateY(-50%)",
          width: "40px",
          height: "40px",
          borderRadius: "50%",
          fontSize: "18px",
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

          {mode === "mock" && (
            <button
              onClick={prevQuestion}
              disabled={currentIndex === 0}
            >
              前の問題へ
            </button>
          )}

          {mode === "mock" && (
            <button
              onClick={nextQuestion}
              disabled={
                currentIndex + 1 >= totalQuestions
              }
            >
              次の問題へ
            </button>
          )}

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

          {!showExplanation &&
            currentQuestion.choices.map(
              (choice, index) => (

                <div key={index}>

                  <button
                    disabled={showExplanation}
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

              <p>
                解説：
                {
                  currentQuestion.explanation
                }
              </p>

              <button
                onClick={nextQuestion}
              >
                次へ
              </button>

            </div>
          )}

        </>
      )}

    </div>
  );
}

export default Quiz;