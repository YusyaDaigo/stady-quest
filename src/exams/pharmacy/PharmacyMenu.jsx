function PharmacyMenu({ onStartRequiredPractice, onStartRequiredMock }) {
  return (
    <div>
      <h2>💊 薬剤師国家試験</h2>

      <p>第111回 必須問題に対応しました。</p>

      <button onClick={onStartRequiredPractice}>
        必須問題 練習
      </button>

      <button onClick={onStartRequiredMock}>
        薬剤師国家試験 模試
      </button>
    </div>
  );
}

export default PharmacyMenu;