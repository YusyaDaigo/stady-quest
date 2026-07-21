export { CATEGORIES } from "./categories";

export { commonQuestions } from "./droneCommon";
export { commonExtraQuestions } from "./droneCommonExtra";

export { requiredQuestions } from "./required";
export { theoryQuestions } from "./theory";
export { practicalQuestions } from "./practical";

import { commonQuestions } from "./droneCommon";
import { commonExtraQuestions } from "./droneCommonExtra";

import { requiredQuestions } from "./required";
import { theoryQuestions } from "./theory";
import { practicalQuestions } from "./practical";

import { generateRandomCalculationQuestions } from "./randomCalculationQuestions";

import {
  firstNormalQuestions,
  firstCalculationQuestions,
  firstRiskQuestions
} from "./droneFirst";

export const secondExamQuestions = [
  ...commonQuestions,
  ...commonExtraQuestions,
  ...requiredQuestions,
  ...theoryQuestions,
  ...practicalQuestions
];

export const firstExamQuestions = [
  ...commonQuestions,
  ...commonExtraQuestions,
  ...requiredQuestions,
  ...theoryQuestions,
  ...practicalQuestions,
  ...firstNormalQuestions,
  ...firstCalculationQuestions,
  ...generateRandomCalculationQuestions(),
  ...firstRiskQuestions
];