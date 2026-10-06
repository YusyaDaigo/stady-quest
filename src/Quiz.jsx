import { useState } from "react";


const renderExamText = (text) => {
  if (typeof text !== "string") {
    return text;
  }

  const pattern = /\[\[([^|\]]+)\|([^\]]*)\]\]/g;

  const parts = [];
  let lastIndex = 0;
  let match;
  let key = 0;

  while ((match = pattern.exec(text)) !== null) {
    if (match.index > lastIndex) {
      parts.push(
        text.slice(lastIndex, match.index)
      );
    }

    const label = match[1];
    const content = match[2];

    parts.push(
      <span
        key={`exam-mark-${key}`}
        style={{
          display: "inline-block",
          borderBottom: "2px solid currentColor",
          padding: "0 0.18em 0.05em",
          margin: "0 0.12em",
          whiteSpace: "nowrap",
        }}
      >
        <span
          style={{
            fontSize: "0.72em",
            fontWeight: 700,
            marginRight: content ? "0.35em" : 0,
          }}
        >
          {label}
        </span>

        {content || "\u3000\u3000\u3000"}
      </span>
    );

    key += 1;
    lastIndex = pattern.lastIndex;
  }

  if (lastIndex < text.length) {
    parts.push(text.slice(lastIndex));
  }

  return parts.length > 0
    ? parts
    : text;
};

function Quiz({
  mode,
  examType,
  selectedCategory,
  time,
  currentQuestion,
  questions,
  showExplanation,
  handleAnswer,
  isCorrect,
  nextQuestion,
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

  const [pendingAnswers, setPendingAnswers]
    = useState([]);

  const isPracticalMock =
    mode === "mock" &&
    (
      examType === "practical_part1" ||
      examType === "practical_part2" ||
      examType === "practical_part3_case" ||
      examType === "practical_part3_single"
    );

  const isPracticalPractice =
    mode === "practice" &&
    examType === "practical";

  const isPracticalCaseReview =
    mode === "review" &&
    Boolean(currentQuestion?.caseId);

  const usesPracticalCaseDisplay =
    isPracticalMock ||
    isPracticalPractice ||
    isPracticalCaseReview;

  const currentCaseId =
    usesPracticalCaseDisplay
      ? currentQuestion?.caseId || null
      : null;

  const isPracticalCaseQuestion =
    Boolean(currentCaseId);

  const caseGroups = [];

  if (
    usesPracticalCaseDisplay &&
    Array.isArray(questions)
  ) {
    const groupMap = new Map();

    questions.forEach((question, index) => {
      if (!question) return;

      const sourceNumber =
        question.sourceNumber;

      /*
       * caseId を持つ問題だけをケース問題として扱う。
       * 年度や問題番号には依存しない。
       */
      const caseKey =
        question.caseId || null;

      if (caseKey) {
        if (!groupMap.has(caseKey)) {
          groupMap.set(caseKey, {
            key: caseKey,
            indexes: [],
            isCase: true,
          });
        }

        groupMap
          .get(caseKey)
          .indexes
          .push(index);

        return;
      }

      /*
       * caseId を持たない問題は通常の単問。
       */
      const singleKey =
        `single-${question.examNumber ?? "unknown"}-${sourceNumber ?? index}`;

      groupMap.set(singleKey, {
        key: singleKey,
        indexes: [index],
        isCase: false,
      });
    });

    caseGroups.push(
      ...groupMap.values()
    );
  }

  const currentGroupIndex =
    usesPracticalCaseDisplay
      ? caseGroups.findIndex(
          (group) =>
            group.indexes.includes(currentIndex)
        )
      : -1;

  const currentGroup =
    currentGroupIndex >= 0
      ? caseGroups[currentGroupIndex]
      : null;

  const caseNumber =
    currentGroupIndex >= 0
      ? currentGroupIndex + 1
      : null;

  const totalCases =
    caseGroups.length;

  const casePosition =
    currentCaseId && currentGroup
      ? currentGroup.indexes.indexOf(
          currentIndex
        ) + 1
      : null;

  const caseQuestionCount =
    currentCaseId && currentGroup
      ? currentGroup.indexes.length
      : null;

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
            {mode === "practice" && examType === "required"
              ? `必須問題 練習｜${
                  selectedCategory === "ALL"
                    ? "全範囲"
                    : selectedCategory
                }`
              : mode === "practice" && examType === "theory"
              ? `理論問題 練習｜${
                  selectedCategory === "ALL"
                    ? "全範囲"
                    : selectedCategory
                }`
              : mode === "practice" && examType === "practical"
              ? `実践問題 練習｜${
                  selectedCategory === "ALL"
                    ? "全範囲"
                    : selectedCategory
                }`
              : mode === "mock" && examType === "required"
              ? "必須問題 模試"
              : mode === "mock" && examType === "theory_part1"
              ? "理論問題 Part1 模試"
              : mode === "mock" && examType === "theory_part2"
              ? "理論問題 Part2 模試"
              : mode === "mock" && examType === "practical_part1"
              ? "実践問題 Part1 模試"
              : mode === "mock" && examType === "practical_part2"
              ? "実践問題 Part2 模試"
              : mode === "mock" &&
                examType === "practical_part3_case"
              ? "実践問題 Part3① 症例問題 模試"
              : mode === "mock" &&
                examType === "practical_part3_single"
              ? "実践問題 Part3② 単問 模試"
              : mode === "mock" && examType === "second"
              ? "二等操縦士 模試"
              : mode === "mock" && examType === "first"
              ? "一等操縦士 模試"
              : mode === "mock" &&
                examType === "webdesign_theory"
              ? "ウェブデザイン技能検定3級 学科 模試"
              : mode === "review"
              ? "復習モード"
              : "練習モード"}
          </h2>

          {isPracticalCaseQuestion && currentCaseId && (
            <p>
              ケース {caseNumber} / {totalCases}
              {"　"}
              ケース内 問 {casePosition} / {caseQuestionCount}
            </p>
          )}

          {isPracticalCaseQuestion && !currentCaseId && (
            <p>
              ケース問題
              {"　"}
              問題 {currentIndex + 1} / {totalQuestions}
            </p>
          )}

          {isPracticalMock && !isPracticalCaseQuestion && (
            <p>
              問題 {currentIndex + 1} / {totalQuestions}
            </p>
          )}

          {mode !== "review" && (
            <p>
              残り時間：
              {time}秒
            </p>
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

          {isPracticalCaseQuestion &&
            currentQuestion.caseContext && (
              <div
                style={{
                  maxWidth: "820px",
                  width: "82%",
                  margin: "30px auto",
                  padding: "20px",
                  textAlign: "left",
                  lineHeight: "1.7",
                  backgroundColor: "#222631",
                  border: "1px solid #555",
                  borderRadius: "10px",
                }}
              >
                <h3>
                  📋 症例
                </h3>

                <p
                  style={{
                    whiteSpace: "pre-wrap",
                    marginBottom: 0,
                  }}
                >
                  {currentQuestion.caseContext}
                </p>
              </div>
            )}

          <h2
        
            style={{
              maxWidth: "820px",
              width: "82%",
              margin: "40px auto 32px",
              lineHeight: "1.7",
              textAlign: "left",
              whiteSpace: "pre-wrap"
            }}
          >
            {renderExamText(currentQuestion.question)}
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
            (choice, index) => {
              const isMultipleAnswer =
                Array.isArray(
                  currentQuestion.answer
                );

              const storedAnswer =
                userAnswers[currentIndex];

              const isSelected =
                isMultipleAnswer
                  ? pendingAnswers.includes(index)
                  : storedAnswer === index;

              return (
                <div key={index}>
                  <button
                    disabled={
                      showExplanation ||
                      storedAnswer !== undefined
                    }
                    onClick={() => {
                      if (!isMultipleAnswer) {
                        handleAnswer(index);
                        return;
                      }

                      setPendingAnswers((prev) => {
                        if (prev.includes(index)) {
                          return prev.filter(
                            (value) =>
                              value !== index
                          );
                        }

                        return [
                          ...prev,
                          index,
                        ];
                      });
                    }}
                    style={{
                      backgroundColor:
                        isSelected
                          ? "#4a6fa5"
                          : "#2b2f3a",

                      color: "#ffffff",

                      border:
                        isSelected
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
                    {isSelected
                      ? "▶ "
                      : ""}
                    {choice}
                  </button>
                </div>
              );
            }
          )}

          {Array.isArray(
            currentQuestion.answer
          ) &&
            userAnswers[currentIndex] === undefined && (() => {
              const requiredSelections =
                currentQuestion.requiredSelections ??
                currentQuestion.answer.length;

              return (
                <button
                  disabled={
                    pendingAnswers.length !==
                    requiredSelections
                  }
                  onClick={() => {
                    handleAnswer(
                      pendingAnswers
                    );

                    setPendingAnswers([]);
                  }}
                  style={{
                    marginTop: "10px",
                    marginBottom: "24px",
                    padding: "14px 24px",
                    fontSize: "1.1rem",
                    borderRadius: "10px",
                    cursor:
                      pendingAnswers.length ===
                      requiredSelections
                        ? "pointer"
                        : "not-allowed",
                  }}
                >
                  回答する
                  （
                  {pendingAnswers.length}
                  /
                  {requiredSelections}
                  ）
                </button>
              );
            })()}

            {showExplanation && (

              <div>

                <h1>
                  {isCorrect
                    ? "⭕ 正解！"
                    : "❌ 不正解"}
                </h1>

                <p>
                  {currentQuestion.requiredSelections != null
                    ? `正答候補（このうち${currentQuestion.requiredSelections}つ選択）：`
                    : "正解："}
                  {Array.isArray(currentQuestion.answer)
                    ? currentQuestion.answer
                        .map(
                          (index) =>
                            currentQuestion.choices[index]
                        )
                        .join(" / ")
                    : currentQuestion.choices[
                        currentQuestion.answer
                      ]}
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