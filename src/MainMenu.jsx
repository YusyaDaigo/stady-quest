function MainMenu({ selectExam }) {
  return (
    <div>
      <h1>Study QUEST</h1>

      <h2>学習する試験を選択</h2>

      <button
        onClick={() => selectExam("drone")}
      >
        🚁 ドローン国家資格
      </button>

      <button
        onClick={() => selectExam("pharmacy")}
      >
        💊 薬剤師国家試験
      </button>

      
    </div>
  );
}

export default MainMenu;