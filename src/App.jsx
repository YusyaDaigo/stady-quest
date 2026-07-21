import { useState, useEffect } from "react";
import "./App.css";
import {
  CATEGORIES,
  commonQuestions,
  secondExamQuestions,
  firstExamQuestions
} from "./exams/drone/questions";

import DroneMenu from "./exams/drone/DroneMenu";
import Quiz from "./Quiz";
import Result from "./Result";
import Review from "./Review";
import MainMenu from "./MainMenu";
import PharmacyMenu from "./exams/pharmacy/PharmacyMenu";
import { requiredQuestions } from "./exams/pharmacy/questions/required";

const shuffleArray = (array) => {
  return [...array].sort(
    () => Math.random() - 0.5
  );
};

const REQUIRED_MOCK_STRUCTURE = [
  { field: "物理", count: 5 },
  { field: "化学", count: 5 },
  { field: "生物", count: 5 },
  { field: "衛生", count: 10 },
  { field: "薬理", count: 15 },
  { field: "薬剤", count: 15 },
  { field: "病態", count: 15 },
  { field: "法規", count: 10 },
  { field: "実務", count: 10 },
];

const FIELD_ALIAS = {
  "物理": "物理",
  "化学": "化学",
  "生物": "生物",
  "衛生": "衛生",
  "薬理": "薬理",
  "薬剤": "薬剤",
  "実務": "実務",

  "病態": "病態",
  "病態・薬物治療": "病態",

  "法規": "法規",
  "法規・制度・倫理": "法規",
};

const normalizeField = (field) => {
  if (!field) return "";

  const normalized = field.trim();

  if (FIELD_ALIAS[normalized]) {
    return FIELD_ALIAS[normalized];
  }

  // 念のため部分一致も許可
  if (normalized.includes("病態")) return "病態";
  if (normalized.includes("法規")) return "法規";

  return normalized;
};

const getRequiredFieldFromSourceNumber = (sourceNumber) => {
  if (sourceNumber >= 1 && sourceNumber <= 5) return "物理";
  if (sourceNumber >= 6 && sourceNumber <= 10) return "化学";
  if (sourceNumber >= 11 && sourceNumber <= 15) return "生物";
  if (sourceNumber >= 16 && sourceNumber <= 25) return "衛生";
  if (sourceNumber >= 26 && sourceNumber <= 40) return "薬理";
  if (sourceNumber >= 41 && sourceNumber <= 55) return "薬剤";
  if (sourceNumber >= 56 && sourceNumber <= 70) return "病態";
  if (sourceNumber >= 71 && sourceNumber <= 80) return "法規";
  if (sourceNumber >= 81 && sourceNumber <= 90) return "実務";

  return "";
};

const getQuestionField = (question) => {
  if (!question) return "";

  return normalizeField(
    question.field ||
    getRequiredFieldFromSourceNumber(question.sourceNumber)
  );
};

const buildRequiredMockQuestions = (questions) => {
  return REQUIRED_MOCK_STRUCTURE.flatMap((section) => {
    const pool = questions.filter(
      (question) =>
        getQuestionField(question) === section.field
    );

    return shuffleArray(pool).slice(0, section.count);
  });
};

const getQuestionTimeLimit = (
  question,
  selectedExam
) => {
  // 薬剤師国家試験の必須問題・練習系
  if (selectedExam === "pharmacy") {
    return 60;
  }

  // ドローン計算問題
  if (question?.category === CATEGORIES.CALC) {
    return 150;
  }

  // ドローン通常問題
  return 30;
};

function App() {

  const [selectedExam, setSelectedExam] = useState(null);
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
      selectedExam === "pharmacy" &&
      selectedMode === "mock" &&
      selectedExamType === "required"
    ) {
      return 5400;
    }

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

    const TEST_GENERATED_PHARMACY_QUESTION = false;

    // 薬剤師 必須問題
    if (selectedExam === "pharmacy") {
        const selectedField =
          category === "ALL" ? "ALL" : normalizeField(category);

          if (TEST_GENERATED_PHARMACY_QUESTION) {
          selectedQuestions = requiredQuestions.filter((question) => {
            return question?.sourceType === "generated";
          });
        } else if (selectedMode === "review") {
          selectedQuestions = mistakeQuestions;
        } else if (
          selectedMode === "practice" &&
          selectedField !== "ALL"
        ) {
          selectedQuestions = requiredQuestions.filter((question) => {
            if (!question) return false;

            return (
              getQuestionField(question) === selectedField
            );
          });
        } else {
          selectedQuestions = requiredQuestions;
        }

        console.log("PHARMACY MODE:", selectedMode);
        console.log("PHARMACY FIELD:", selectedField);
        console.log("PHARMACY QUESTIONS:", selectedQuestions.length);

        if (selectedQuestions.length === 0) {
          alert(
            `${selectedField} の問題が見つかりません。field名を確認してください。`
          );
          return;
        }

      } else


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

    let shuffledQuestions;

    if (
      selectedExam === "pharmacy" &&
      selectedMode === "mock" &&
      selectedExamType === "required"
    ) {
      shuffledQuestions =
        buildRequiredMockQuestions(selectedQuestions);
    } else {
      shuffledQuestions =
        shuffleArray(selectedQuestions);
    }

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
        shuffledQuestions[0],
        selectedExam
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
    if (userAnswers[currentIndex] !== undefined) {
      return;
    }

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
    setTime(
      getQuestionTimeLimit(
        next,
        selectedExam
      )
    );
  }
};

  const nextQuestion = () => {

    setShowExplanation(false);

    const next =
      currentQuestions[currentIndex + 1];

    if (mode !== "mock") {
      setTime(
        getQuestionTimeLimit(
          next,
          selectedExam
        )
      );
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
          ? "模試を終了してジャンルメニューへ戻りますか？"
          : "学習を終了してジャンルメニューへ戻りますか？";

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

  const clearMistakeQuestions = () => {

    const confirmDelete = window.confirm(
      "復習リストをすべて削除しますか？"
    );

    if (!confirmDelete) {
      return;
    }

    setMistakeQuestions([]);

    localStorage.removeItem("mistakeQuestions");

    alert("復習リストを削除しました。");
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

      setUserAnswers((prev) => {
        const newAnswers = [...prev];
        newAnswers[currentIndex] = null;
        return newAnswers;
});

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
            const next =
              currentQuestions[currentIndex + 1];

            setTime(
              getQuestionTimeLimit(
                next,
                selectedExam
              )
            );
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

  if (selectedExam === null) {
    return (
      <MainMenu
        selectExam={setSelectedExam}
      />
    );
}

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
        ジャンルメニュー
      </button>

        <h1
          onClick={() => {
            setSelectedExam(null);
            setScreen("menu");
          }}
          style={{
            cursor: "pointer"
          }}
        >
          Study QUEST
        </h1>

      {selectedExam === "drone" &&
        screen === "menu" && (
          <DroneMenu
            startQuiz={startQuiz}
            mistakeQuestions={mistakeQuestions}
            setMistakeQuestions={setMistakeQuestions}
          />
)}

      {selectedExam === "pharmacy" &&
        screen === "menu" && (
          <PharmacyMenu
            onStartRequiredPractice={(field) =>
              startQuiz(
                "practice",
                "required",
                field
              )
            }
            onStartRequiredMock={() =>
              startQuiz("mock", "required")
            }
            onStartReview={() =>
              startQuiz("review", "required")
            }
            onClearReview={() =>
              clearMistakeQuestions()
            }
            mistakeCount={mistakeQuestions.length}
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