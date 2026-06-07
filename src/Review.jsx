function Review({
  questions,
  userAnswers,
  bookmarkedIndexes,
  goResult
}) {
  return (
    <div>

      <h2>答案レビュー</h2>

      {questions.map((question, index) => {

        const userAnswer =
          userAnswers[index];

        const isCorrect =
          userAnswer === question.answer;

        return (
          <div
            key={index}
            style={{
              border: "1px solid #555",
              borderRadius: "10px",
              padding: "15px",
              marginBottom: "20px"
            }}
          >
            <h3>
              問題 {index + 1}
              {bookmarkedIndexes.includes(index)
                ? " 🔖"
                : ""}
            </h3>

            <p>
              {question.question}
            </p>

            <p>
              あなたの回答：
              {userAnswer === undefined
                ? "未回答"
                : question.choices[userAnswer]}
            </p>

            <p>
              正解：
              {question.choices[question.answer]}
            </p>

            <h3>
              {isCorrect
                ? "⭕ 正解"
                : "❌ 不正解"}
            </h3>

            <p>
              解説：
              {question.explanation}
            </p>
          </div>
        );
      })}

      <button onClick={goResult}>
        結果画面へ戻る
      </button>

    </div>
  );
}

export default Review;