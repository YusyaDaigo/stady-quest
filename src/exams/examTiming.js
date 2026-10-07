import {
  CATEGORIES as DRONE_CATEGORIES
} from "./drone/questions/categories";

const DEFAULT_QUESTION_TIME = 30;
const DEFAULT_SESSION_TIME = 30;

const EXAM_TIMING = {
  drone: {
    questionDefault: 30,

    questionByCategory: {
      [DRONE_CATEGORIES.CALC]: 150
    },

    mockByExamType: {
      second: 1800,
      first: 4500
    }
  },

  pharmacy: {
    questionDefault: 60,

    questionByExamType: {
      theory: 150,
      theory_part1: 150,
      theory_part2: 150,
      practical: 150,
      practical_part1: 150,
      practical_part2: 150,
      practical_part3_case: 150,
      practical_part3_single: 150
    },

    mockByExamType: {
      required: 5400,
      theory_part1: 9000,
      theory_part2: 6900,
      practical_part1: 7500,
      practical_part2: 6000,
      practical_part3_case: 6000,
      practical_part3_single: 3000
    }
  },

  webdesign: {
    questionDefault: 108,

    mockByExamType: {
      webdesign_theory: 2700
    }
  }
};

export const getQuestionTimeLimit = (
  question,
  exam,
  examType
) => {
  const config = EXAM_TIMING[exam];

  if (!config) {
    return DEFAULT_QUESTION_TIME;
  }

  const examTypeTime =
    config.questionByExamType?.[examType];

  if (Number.isFinite(examTypeTime)) {
    return examTypeTime;
  }

  const categoryTime =
    config.questionByCategory?.[
      question?.category
    ];

  if (Number.isFinite(categoryTime)) {
    return categoryTime;
  }

  return (
    config.questionDefault ??
    DEFAULT_QUESTION_TIME
  );
};

export const getInitialTime = (
  exam,
  mode,
  examType
) => {
  if (mode !== "mock") {
    return DEFAULT_SESSION_TIME;
  }

  const config = EXAM_TIMING[exam];

  if (!config) {
    return DEFAULT_SESSION_TIME;
  }

  return (
    config.mockByExamType?.[examType] ??
    DEFAULT_SESSION_TIME
  );
};
