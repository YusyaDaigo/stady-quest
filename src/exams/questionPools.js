import {
  secondExamQuestions,
  firstExamQuestions
} from "./drone/questions";

import {
  requiredQuestions,
  theoryQuestions,
  practicalQuestions
} from "./pharmacy/questions";

import {
  theoryQuestions as webDesignTheoryQuestions
} from "./webdesign/questions";

const PHARMACY_THEORY_TYPES = new Set([
  "theory",
  "theory_part1",
  "theory_part2"
]);

const PHARMACY_PRACTICAL_TYPES = new Set([
  "practical",
  "practical_part1",
  "practical_part2",
  "practical_part3_case",
  "practical_part3_single"
]);

export const getPharmacyQuestionPool = (
  examType
) => {
  if (PHARMACY_THEORY_TYPES.has(examType)) {
    return theoryQuestions;
  }

  if (PHARMACY_PRACTICAL_TYPES.has(examType)) {
    return practicalQuestions;
  }

  return requiredQuestions;
};

export const getWebDesignQuestionPool = () => {
  return webDesignTheoryQuestions;
};

export const getDroneQuestionPool = (
  examType
) => {
  if (examType === "first") {
    return firstExamQuestions;
  }

  return secondExamQuestions;
};
