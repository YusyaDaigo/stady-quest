export { CATEGORIES } from "./categories";

export { commonQuestions } from "./droneCommon";
export { commonExtraQuestions } from "./droneCommonExtra";
export { generatedDroneQuestions } from "./droneGeneratedQuestions";

export { requiredQuestions } from "./required";
export { theoryQuestions } from "./theory";
export { practicalQuestions } from "./practical";

import { commonQuestions } from "./droneCommon";
import { commonExtraQuestions } from "./droneCommonExtra";
import { generatedDroneQuestions } from "./droneGeneratedQuestions";

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
  ...generatedDroneQuestions,
  ...requiredQuestions,
  ...theoryQuestions,
  ...practicalQuestions
];

export const firstExamQuestions = [
  ...commonQuestions,
  ...commonExtraQuestions,
  ...generatedDroneQuestions,
  ...requiredQuestions,
  ...theoryQuestions,
  ...practicalQuestions,
  ...firstNormalQuestions,
  ...firstCalculationQuestions,
  ...generateRandomCalculationQuestions(),
  ...firstRiskQuestions
];