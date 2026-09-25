import { theory98Questions } from "./theory_98";
import { theory99Questions } from "./theory_99";
import { theory100Questions } from "./theory_100";
import { theory101Questions } from "./theory_101";
import { theory102Questions } from "./theory_102";
import { theory103Questions } from "./theory_103";
import { theory104Questions } from "./theory_104";
import { theory105Questions } from "./theory_105";
import { theory106Questions } from "./theory_106";
import { theory107Questions } from "./theory_107";
import { theory108Questions } from "./theory_108";
import { theory109Questions } from "./theory_109";
import { theory110Questions } from "./theory_110";
import { theory111Questions } from "./theory_111";

const allTheoryQuestions = [
  ...theory98Questions,
  ...theory99Questions,
  ...theory100Questions,
  ...theory101Questions,
  ...theory102Questions,
  ...theory103Questions,
  ...theory104Questions,
  ...theory105Questions,
  ...theory106Questions,
  ...theory107Questions,
  ...theory108Questions,
  ...theory109Questions,
  ...theory110Questions,
  ...theory111Questions,
];

export const theoryQuestions =
  allTheoryQuestions.filter(
    (question) =>
      question.scoringStatus !== "no_answer"
  );
