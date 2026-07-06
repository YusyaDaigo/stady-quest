function PharmacyMenu({
  onStartRequiredPractice,
  onStartRequiredMock,
}) {
  const fields = [
    { label: "全範囲", value: "ALL" },
    { label: "物理", value: "物理" },
    { label: "化学", value: "化学" },
    { label: "生物", value: "生物" },
    { label: "衛生", value: "衛生" },
    { label: "薬理", value: "薬理" },
    { label: "薬剤", value: "薬剤" },
    { label: "病態", value: "病態" },
    { label: "法規", value: "法規" },
    { label: "実務", value: "実務" },
  ];

  return (
    <div>
      <h2>💊 薬剤師国家試験</h2>

      <p>必須問題に対応中</p>

      <h3>📖 必須問題 練習</h3>

      {fields.map((field) => (
        <button
          key={field.value}
          onClick={() =>
            onStartRequiredPractice(field.value)
          }
        >
          {field.label}
        </button>
      ))}

      <hr />

      <h3>📝 必須問題 模試</h3>

      <button onClick={onStartRequiredMock}>
        本番形式 90問
      </button>
    </div>
  );
}

export default PharmacyMenu;
