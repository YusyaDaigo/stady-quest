function WebDesignMenu({
  onStartPractical
}) {
  return (
    <div>
      <h2>
        🌐 ウェブデザイン技能検定
      </h2>

      <h3>3級</h3>

      <div
        style={{
          display: "grid",
          gap: "16px",
          maxWidth: "520px",
          margin: "30px auto"
        }}
      >
        <button
          disabled
          style={{
            padding: "18px"
          }}
        >
          📘 学科試験
          <br />
          準備中
        </button>

        <button
          onClick={onStartPractical}
          style={{
            padding: "18px"
          }}
        >
          💻 実技試験
          <br />
          Practical Engine v1
        </button>
      </div>
    </div>
  );
}

export default WebDesignMenu;
