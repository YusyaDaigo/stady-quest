export { CATEGORIES } from "./categories";

export { commonQuestions }
from "./droneCommon";

export { commonExtraQuestions }
from "./droneCommonExtra";

import { commonQuestions }
from "./droneCommon";

import { commonExtraQuestions }
from "./droneCommonExtra";

import { generateRandomCalculationQuestions } from "./randomCalculationQuestions";

import {
  firstNormalQuestions,
  firstCalculationQuestions,
  firstRiskQuestions
} from "./droneFirst";

export const secondExamQuestions = [
  ...commonQuestions,
  ...commonExtraQuestions
];

export const firstExamQuestions = [
  ...commonQuestions,
  ...commonExtraQuestions,
  ...firstNormalQuestions,
  ...firstCalculationQuestions,
  ...generateRandomCalculationQuestions(),
  ...firstRiskQuestions
];