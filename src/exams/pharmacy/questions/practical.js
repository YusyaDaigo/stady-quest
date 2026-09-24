import { practical103Questions } from "./practical_103";
import { practical104Questions } from "./practical_104";
import { practical105Questions } from "./practical_105";
import { practical106Questions } from "./practical_106";
import { practical107Questions } from "./practical_107";
import { practical108Questions } from "./practical_108";
import { practical109Questions } from "./practical_109";
import { practical110Questions } from "./practical_110";
import { practical111Questions } from "./practical_111";

const allPracticalQuestions = [
  ...practical103Questions,
  ...practical104Questions,
  ...practical105Questions,
  ...practical106Questions,
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
