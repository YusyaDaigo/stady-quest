export { CATEGORIES } from "./categories";

export { commonQuestions }
from "./droneCommon";

export { commonExtraQuestions }
from "./droneCommonExtra";

import { commonQuestions }
from "./droneCommon";

import { commonExtraQuestions }
from "./droneCommonExtra";

export const secondExamQuestions = [
  ...commonQuestions,
  ...commonExtraQuestions
];

// 一旦空配列
export const firstNormalQuestions = [];
export const firstCalculationQuestions = [];
export const firstRiskQuestions = [];

export const firstExamQuestions = [
  ...commonQuestions,
  ...commonExtraQuestions,
  ...firstNormalQuestions,
  ...firstCalculationQuestions,
  ...firstRiskQuestions
];