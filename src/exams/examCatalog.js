export const EXAM_CATALOG = [
  {
    id: "drone",
    icon: "🚁",
    label: "ドローン国家資格"
  },
  {
    id: "pharmacy",
    icon: "💊",
    label: "薬剤師国家試験"
  },
  {
    id: "webdesign",
    icon: "🌐",
    label: "ウェブデザイン技能検定"
  }
];

export const getExamConfig = (examId) => {
  return (
    EXAM_CATALOG.find(
      (exam) => exam.id === examId
    ) ?? null
  );
};
