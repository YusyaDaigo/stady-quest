import { theory109Questions } from "./theory_109";
import { theory110Questions } from "./theory_110";
import { theory111Questions } from "./theory_111";

const allTheoryQuestions = [
  ...theory109Questions,
  ...theory110Questions,
  ...theory111Questions,
];

export const theoryQuestions =
  allTheoryQuestions.filter(
    (question) =>
      question.scoringStatus !== "no_answer"
  );
