import { useState, useEffect } from "react";
import {
  commonQuestions,
  secondExamQuestions,
  firstExamQuestions
} from "./questions";
const shuffleArray = (array) => {

  return [...array].sort(
    () => Math.random() - 0.5
  );

};
import Menu from "./Menu";
import Quiz from "./Quiz";
import Result from "./Result";
import Review from "./Review";

function App() {

  const [screen, setScreen] = useState("menu");
  const [currentIndex, setCurrentIndex] = useState(0);

  const [mode, setMode] = useState("practice");
  const [examType, setExamType] = useState(null);

  const [score, setScore] = useState(0);
  const [correctCount, setCorrectCount] = useState(0);

  const [showExplanation, setShowExplanation] = useState(false);

  const [time, setTime] = useState(30);

  const [isCorrect, setIsCorrect] = useState(null);

  const [userAnswers, setUserAnswers] = useState([]);

  const [mistakeQuestions, setMistakeQuestions] = useState([]);

  const [remainingTimes, setRemainingTimes]
  = useState([]);

  const [bookmarkedIndexes, setBookmarkedIndexes]
  = useState([]);

  const [quizQuestions, setQuizQuestions]
  = useState([]);

// localStorage 読み込み
useEffect(() => {

  const savedMistakes =
    localStorage.getItem("mistakeQuestions");

  if (savedMistakes) {

    setMistakeQuestions(
      JSON.parse(savedMistakes)
    );
  }

}, []);

// localStorage 保存

useEffect(() => {
  localStorage.setItem(
    "mistakeQuestions",
    JSON.stringify(mistakeQuestions)
  );

}, [mistakeQuestions]);

  // 出題問題切り替え
  const currentQuestions =
    quizQuestions;

  const currentQuestion =
    currentQuestions[currentIndex] || null;

  const getInitialTime = (
    selectedMode,
    selectedExamType
  ) => {

    if (
      selectedMode === "mock" &&
      selectedExamType === "second"
    ) {
      return 1800;
    }

    if (
      selectedMode === "mock" &&
      selectedExamType === "first"
    ) {
      return 4500;
    }

    return 30;
};  

  // クイズ開始
  const startQuiz = (selectedMode, selectedExamType = null) => {

    let selectedQuestions;

    if (selectedMode === "review") {

      selectedQuestions =
        mistakeQuestions;

    } else if (
      selectedMode === "mock" &&
      selectedExamType === "second"
      ) {

      selectedQuestions =
        secondExamQuestions;

    } else if (
      selectedMode === "mock" &&
      selectedExamType === "first"
      ) {

      selectedQuestions =
        firstExamQuestions;

    } else {

      selectedQuestions =
        commonQuestions;
      }

    let shuffledQuestions =
      shuffleArray(selectedQuestions);

    if (
      selectedMode === "mock" &&
      selectedExamType === "second"
    ) {

      shuffledQuestions =
        shuffledQuestions.slice(0, 50);
    }

    if (
      selectedMode === "mock" &&
      selectedExamType === "first"
    ) {

      shuffledQuestions =
        shuffledQuestions.slice(0, 70);
    }

    setQuizQuestions(shuffledQuestions);

    setMode(selectedMode);
    setExamType(selectedExamType);

    setCurrentIndex(0);

    setScore(0);

    setCorrectCount(0);

    setShowExplanation(false);

    setTime(
      getInitialTime(
        selectedMode,
        selectedExamType
  )
);

    setIsCorrect(null);

    setUserAnswers([]);

    setRemainingTimes([]);

    setBookmarkedIndexes([]);

    setScreen("quiz");
  };

  // 回答処理
  const handleAnswer = (index) => {

    const correct =
      index === currentQuestion.answer;

    // 回答保存
    const newAnswers = [...userAnswers];

    newAnswers[currentIndex] = index;

    setUserAnswers(newAnswers);

    setIsCorrect(correct);
    setRemainingTimes((prev) => [
  ...prev,
  time
]);

    // 正解
    if (correct) {

      setScore((prev) => prev + time);

      setCorrectCount((prev) => prev + 1);
    }

    // 不正解
    if (!correct) {

      setMistakeQuestions((prev) => {

        // 重複防止
        if (prev.includes(currentQuestion)) {
          return prev;
        }

        return [...prev, currentQuestion];
      });
    }

    // 練習モード
    if (mode === "practice") {

      setShowExplanation(true);

      return;
    }

    // 模試モード
    if (mode === "mock") {

      // 最後の問題なら自動終了しない
      if (
        currentIndex + 1 >=
        currentQuestions.length
      ) {
        return;
      }

      setCurrentIndex((prev) => prev + 1);

      return;
    }

    // 復習モード
    if (
      currentIndex + 1 >=
      currentQuestions.length
    ) {

      setScreen("result");

      return;
    }

    setCurrentIndex((prev) => prev + 1);

    if (mode !== "mock") {
  setTime(30);
}

};

  // 次の問題
  const nextQuestion = () => {

    setShowExplanation(false);

    if (mode !== "mock") {
      setTime(30);
}

    setIsCorrect(null);

    if (
      currentIndex + 1 <
      currentQuestions.length
    ) {

      setCurrentIndex((prev) => prev + 1);

    } else {

      setScreen("result");
    }
  };

  // 前の問題
  const prevQuestion = () => {

    if (currentIndex > 0) {

      setCurrentIndex((prev) => prev - 1);

      setShowExplanation(false);

      setIsCorrect(null);
  }
};

  // 指定した問題へ移動
  const jumpQuestion = (index) => {

    setCurrentIndex(index);

    setShowExplanation(false);

    setIsCorrect(null);
};

  // 栞切り替え
  const toggleBookmark = () => {

    setBookmarkedIndexes((prev) => {

      if (prev.includes(currentIndex)) {

        return prev.filter(
          (index) => index !== currentIndex
      );
    }

      return [
        ...prev,
        currentIndex
      ];
  });
};

  // メニューへ戻る
  const goMenu = () => {

    if (screen === "quiz") {

      const confirmExit =
        window.confirm(
          "模試を終了してメニューに戻りますか？"
        );

      if (!confirmExit) {
        return;
      }
    }

    setScreen("menu");
  };

  // 答案レビューへ
  const goReview = () => {

    setScreen("review");
  };

  // 結果画面へ戻る
  const goResult = () => {

    setScreen("result");
  };

  // 模試終了
  const finishExam = () => {

    setScreen("result");
  };
  
   // タイマー
useEffect(() => {

  if (screen !== "quiz") return;

  if (showExplanation) return;

  if (!currentQuestion) return;

  if (time <= 0) {

    setMistakeQuestions((prev) => {

      if (prev.includes(currentQuestion)) {
        return prev;
      }

      return [...prev, currentQuestion];
    });

    setIsCorrect(false);

    setRemainingTimes((prev) => [
      ...prev,
      0
    ]);

    // 練習モード
    if (mode === "practice") {

      setShowExplanation(true);

    } else {

      // 最後の問題
      if (
        currentIndex + 1 >=
        currentQuestions.length
      ) {

        setScreen("result");

      } else {

        setCurrentIndex((prev) => prev + 1);

        if (mode !== "mock") {
          setTime(30);
        }
      }
    }

    return;
  }

  const timer = setTimeout(() => {

    setTime((prev) => prev - 1);

  }, 1000);

  return () => clearTimeout(timer);

}, [
  time,
  screen,
  showExplanation,
  mode,
  currentIndex,
  currentQuestion,
  currentQuestions.length
]);

  return (
    <div>

      {/* 固定メニューボタン */}
      <button
        onClick={goMenu}
        style={{
          position: "fixed",
          top: "20px",
          right: "20px",
          zIndex: 1000,
          padding: "10px",
          borderRadius: "10px"
        }}
      >
        メニュー
      </button>

      <h1>Study QUEST</h1>

      {/* メニュー画面 */}
      {screen === "menu" && (

  <Menu
    startQuiz={startQuiz}
    mistakeQuestions={mistakeQuestions}
    setMistakeQuestions={
      setMistakeQuestions
    }
  />

)}

  {screen === "quiz" && (

  <Quiz
    mode={mode}
    examType={examType}
    time={time}
    currentQuestion={currentQuestion}
    showExplanation={showExplanation}
    handleAnswer={handleAnswer}
    isCorrect={isCorrect}
    nextQuestion={nextQuestion}
    jumpQuestion={jumpQuestion}
    totalQuestions={currentQuestions.length}
    bookmarkedIndexes={bookmarkedIndexes}
    prevQuestion={prevQuestion}
    currentIndex={currentIndex}
    toggleBookmark={toggleBookmark}
    isBookmarked={
      bookmarkedIndexes.includes(currentIndex)
  }
    userAnswers={userAnswers}
    finishExam={finishExam}
/>

)}

{/* 結果画面 */}
{screen === "result" && (

  <Result
    correctCount={correctCount}
    totalQuestions={
      currentQuestions.length
    }
    score={score}
    remainingTimes={remainingTimes}
    mode={mode}
    examType={examType}
    goMenu={goMenu}
    bookmarkedCount={bookmarkedIndexes.length}
    goReview={goReview}
  />

)}

{screen === "review" && (

  <Review
    questions={currentQuestions}
    userAnswers={userAnswers}
    bookmarkedIndexes={bookmarkedIndexes}
    goResult={goResult}
  />

)}

    </div>
  );
}

export default App;