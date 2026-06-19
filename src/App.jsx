import { useState, useEffect } from "react";
import {
  CATEGORIES,
  commonQuestions,
  secondExamQuestions,
  firstExamQuestions
} from "./questions/index";

import Menu from "./Menu";
import Quiz from "./Quiz";
import Result from "./Result";
import Review from "./Review";

const shuffleArray = (array) => {
  return [...array].sort(
    () => Math.random() - 0.5
  );
};

const getQuestionTimeLimit = (question) => {
  if (question?.category === CATEGORIES.CALC) {
    return 150;
  }

  return 30;
};

function App() {

  const [screen, setScreen] = useState("menu");
  const [currentIndex, setCurrentIndex] = useState(0);

  const [mode, setMode] = useState("practice");
  const [examType, setExamType] = useState(null);

  const [selectedCategory, setSelectedCategory]
    = useState(CATEGORIES.ALL);

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

  useEffect(() => {

    const savedMistakes =
      localStorage.getItem("mistakeQuestions");

    if (savedMistakes) {
      setMistakeQuestions(
        JSON.parse(savedMistakes)
      );
    }

  }, []);

  useEffect(() => {
    localStorage.setItem(
      "mistakeQuestions",
      JSON.stringify(mistakeQuestions)
    );

  }, [mistakeQuestions]);

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

  const startQuiz = (
    selectedMode,
    selectedExamType = null,
    category = CATEGORIES.ALL
  ) => {

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

        if (category === CATEGORIES.ALL) {

          selectedQuestions =
            secondExamQuestions;

        } else if (
          category === CATEGORIES.CALC ||
          category === CATEGORIES.FIRST
        ) {

          selectedQuestions =
            firstExamQuestions.filter(
              (question) =>
                question.category === category
            );

        } else {

          selectedQuestions =
            secondExamQuestions.filter(
              (question) =>
                question.category === category
            );
      console.log("MODE:", selectedMode);
      console.log("CATEGORY:", category);
      console.log("SELECTED QUESTIONS:", selectedQuestions.length);
      console.log(
        "CATEGORY LIST:",
        secondExamQuestions.map((q) => q.category).slice(0, 10)
);

console.log(
  "CATEGORY",
  category,
  "COUNT",
  selectedQuestions.length
);
        }
      }

    let shuffledQuestions =
      shuffleArray(selectedQuestions);

    if (selectedMode === "practice") {
      if (category === CATEGORIES.ALL) {
        shuffledQuestions =
          shuffledQuestions.slice(0, 30);
      } else {
        shuffledQuestions =
          shuffledQuestions.slice(0, 10);
      }
    }

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
    setSelectedCategory(category);

    setCurrentIndex(0);
    setScore(0);
    setCorrectCount(0);
    setShowExplanation(false);

  if (selectedMode === "practice") {

    setTime(
      getQuestionTimeLimit(
        shuffledQuestions[0]
      )
    );

  } else {

    setTime(
      getInitialTime(
        selectedMode,
        selectedExamType
    )
  );
}

    setIsCorrect(null);
    setUserAnswers([]);
    setRemainingTimes([]);
    setBookmarkedIndexes([]);

    setScreen("quiz");
  };

  const handleAnswer = (index) => {

    const correct =
      index === currentQuestion.answer;

    const newAnswers = [...userAnswers];

    newAnswers[currentIndex] = index;

    setUserAnswers(newAnswers);

    setIsCorrect(correct);

    setRemainingTimes((prev) => [
      ...prev,
      time
    ]);

    if (correct) {

      setScore((prev) => prev + time);

      setCorrectCount((prev) => prev + 1);
    }

    if (!correct) {

      setMistakeQuestions((prev) => {

        if (prev.includes(currentQuestion)) {
          return prev;
        }

        return [...prev, currentQuestion];
      });
    }

    if (mode === "practice") {

      setShowExplanation(true);

      return;
    }

    if (mode === "mock") {

      if (
        currentIndex + 1 >=
        currentQuestions.length
      ) {
        return;
      }

      setCurrentIndex((prev) => prev + 1);

      return;
    }

    if (
      currentIndex + 1 >=
      currentQuestions.length
    ) {

      setScreen("result");

      return;
    }

  const next =
    currentQuestions[currentIndex + 1];

  setCurrentIndex((prev) => prev + 1);

  if (mode !== "mock") {
    setTime(getQuestionTimeLimit(next));
}
  };

  const nextQuestion = () => {

    setShowExplanation(false);

    const next =
      currentQuestions[currentIndex + 1];

    if (mode !== "mock") {
      setTime(getQuestionTimeLimit(next));
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

  const prevQuestion = () => {

    if (currentIndex > 0) {

      setCurrentIndex((prev) => prev - 1);

      setShowExplanation(false);

      setIsCorrect(null);
    }
  };

  const jumpQuestion = (index) => {

    setCurrentIndex(index);

    setShowExplanation(false);

    setIsCorrect(null);
  };

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

  const goMenu = () => {

    if (screen === "quiz") {

      const message =
        mode === "mock"
          ? "模試を終了してメニューに戻りますか？"
          : "学習を終了してメニューに戻りますか？";

      const confirmExit =
        window.confirm(message);

      if (!confirmExit) {
        return;
      }
    }

    setScreen("menu");
  };

  const goReview = () => {

    setScreen("review");
  };

  const goResult = () => {

    setScreen("result");
  };

  const finishExam = () => {

    setScreen("result");
  };

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

      if (mode === "practice") {

        setShowExplanation(true);

      } else {

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