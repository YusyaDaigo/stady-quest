import {
  EXAM_CATALOG
} from "./exams/examCatalog";

function MainMenu({ selectExam }) {
  return (
    <div>
      <h1>Study QUEST</h1>

      <h2>学習する試験を選択</h2>

      {EXAM_CATALOG.map((exam) => (
        <button
          key={exam.id}
          onClick={() =>
            selectExam(exam.id)
          }
        >
          {exam.icon} {exam.label}
        </button>
      ))}
    </div>
  );
}

export default MainMenu;
