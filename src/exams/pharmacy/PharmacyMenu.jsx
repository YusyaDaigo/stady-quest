function PharmacyMenu({
  onStartRequiredPractice,
  onStartRequiredMock,
  onStartReview,
  onClearReview,
  mistakeCount,
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

  const sectionStyle = {
    maxWidth: "760px",
    margin: "34px auto",
    padding: "24px 18px",
    borderTop: "1px solid #555",
  };

  const gridStyle = {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(140px, 1fr))",
    gap: "12px",
    maxWidth: "620px",
    margin: "0 auto",
  };

  const buttonStyle = {
    minHeight: "52px",
    padding: "14px 18px",
    fontSize: "1.05rem",
    borderRadius: "14px",
    fontWeight: "bold",
  };

  const wideButtonStyle = {
    ...buttonStyle,
    width: "90%",
    maxWidth: "420px",
    marginTop: "12px",
  };

  return (
    <div>
      <h2>💊 薬剤師国家試験</h2>

      <p>必須問題に対応中</p>

      <section style={sectionStyle}>
        <h3>📖 必須問題 練習</h3>

        <div style={gridStyle}>
          {fields.map((field) => (
            <button
              key={field.value}
              onClick={() =>
                onStartRequiredPractice(field.value)
              }
              style={buttonStyle}
            >
              {field.label}
            </button>
          ))}
        </div>
      </section>

      <section style={sectionStyle}>
        <h3>📝 必須問題 模試</h3>

        <button
          onClick={onStartRequiredMock}
          style={wideButtonStyle}
        >
          本番形式 90問
        </button>
      </section>

      <section style={sectionStyle}>
        <h3>🔁 復習モード</h3>

        <button
          onClick={onStartReview}
          disabled={mistakeCount === 0}
        >
          間違えた問題を復習
          （{mistakeCount}問）
        </button>

        <br /><br />

        <button
          onClick={onClearReview}
          disabled={mistakeCount === 0}
        >
          🗑 復習リスト削除
        </button>
      </section>
    </div>
  );
}

export default PharmacyMenu;
