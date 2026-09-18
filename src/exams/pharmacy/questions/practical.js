import { practical107Questions } from "./practical_107";
import { practical108Questions } from "./practical_108";
import { practical109Questions } from "./practical_109";
import { practical110Questions } from "./practical_110";
import { practical111Questions } from "./practical_111";

const allPracticalQuestions = [
  ...practical107Questions,
  ...practical108Questions,
  ...practical109Questions,
  ...practical110Questions,
  ...practical111Questions,
];

export const practicalQuestions =
  allPracticalQuestions.filter(
    (question) =>
      question.scoringStatus !== "no_answer"
  );
