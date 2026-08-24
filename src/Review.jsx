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

        const normalizeAnswer = (value) => {
          if (Array.isArray(value)) {
            return [...value].sort(
              (a, b) => a - b
            );
          }

          return value;
        };

        const normalizedUserAnswer =
          normalizeAnswer(userAnswer);

        const normalizedCorrectAnswer =
          normalizeAnswer(question.answer);

        const isCorrect =
          Array.isArray(normalizedUserAnswer) &&
          Array.isArray(normalizedCorrectAnswer)
            ? (
                normalizedUserAnswer.length ===
                  normalizedCorrectAnswer.length &&
                normalizedUserAnswer.every(
                  (value, answerIndex) =>
                    value ===
                    normalizedCorrectAnswer[answerIndex]
                )
              )
            : normalizedUserAnswer ===
              normalizedCorrectAnswer;

        const formatAnswer = (answer) => {
          if (answer === undefined) {
            return "未回答";
          }

          if (Array.isArray(answer)) {
            return answer
              .map(
                (choiceIndex) =>
                  question.choices[choiceIndex]
              )
              .join(" / ");
          }

          return question.choices[answer];
        };

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
              {formatAnswer(userAnswer)}
            </p>

            <p>
              正解：
              {formatAnswer(question.answer)}
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