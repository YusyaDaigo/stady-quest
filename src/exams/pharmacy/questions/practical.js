import { practical109Questions } from "./practical_109";
import { practical110Questions } from "./practical_110";
import { practical111Questions } from "./practical_111";

const allPracticalQuestions = [
  ...practical109Questions,
  ...practical110Questions,
  ...practical111Questions,
];

export const practicalQuestions =
  allPracticalQuestions.filter(
    (question) =>
      question.scoringStatus !== "no_answer"
  );
