export { CATEGORIES } from "./categories";

export { requiredQuestions } from "./required";
export { theoryQuestions } from "./theory";
export { practicalQuestions } from "./practical";

import { requiredQuestions } from "./required";
import { theoryQuestions } from "./theory";
import { practicalQuestions } from "./practical";

export const pharmacyPracticeQuestions = [
  ...requiredQuestions,
  ...theoryQuestions,
  ...practicalQuestions
];

export const pharmacyMockQuestions = [
  ...requiredQuestions,
  ...theoryQuestions,
  ...practicalQuestions
];