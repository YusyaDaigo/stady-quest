
  function Result({
    correctCount,
    totalQuestions,
    score,
    remainingTimes,
    mode,
    examType,
    bookmarkedCount,
    goMenu,
    goReview
})
 {
    const averageTime =
  remainingTimes.length > 0
    ? (
        remainingTimes.reduce(
          (a, b) => a + b,
          0
        ) / remainingTimes.length
      ).toFixed(1)
    : 0;

  // ランク計算
  const accuracy =
    Math.round(
      (correctCount / totalQuestions) * 100
    );

let rank = "";

  if (mode === "practice") {

    if (
      accuracy >= 95 &&
      averageTime >= 20
    ) {

      rank = "💎 THE PARAGON";

    } else if (
      accuracy >= 90 &&
      averageTime >= 15
    ) {

      rank = "🥇 プロフェッショナル";

    } else if (
      accuracy >= 80 &&
      averageTime >= 10
    ) {

      rank = "🥈 ベテラン";

    } else if (
      accuracy >= 70 &&
      averageTime >= 3
    ) {

      rank = "🥉 ルーキー";

    } else {

      rank = "🪵 練習生";
    }

  } else if (mode === "mock") {

  // 二等

    if (examType === "second") {

      if (
        accuracy >= 95 &&
        averageTime >= 1200
      ) {

        rank = "💎 EXPERT";

      } else if (
        accuracy >= 90 &&
        averageTime >= 1080
      ) {

        rank = "🥇 MASTER";

      } else if (
        accuracy >= 80 &&
        averageTime >= 840
      ) {

        rank = "🥈 熟練者";

      } else if (
        accuracy >= 70 &&
        averageTime >= 120
      ) {

        rank = "🥉 経験者";

      } else {

        rank = "🪵 初心者";
      }

    }

    // 一等

    else if (examType === "first") {

      if (
        accuracy >= 95 &&
        averageTime >= 2400
      ) {

        rank = "💎 EXPERT";

      } else if (
        accuracy >= 90 &&
        averageTime >= 1800
      ) {

        rank = "🥇 MASTER";

      } else if (
        accuracy >= 80 &&
        averageTime >= 1020
      ) {

        rank = "🥈 熟練者";

      } else if (
        accuracy >= 70 &&
        averageTime >= 300
      ) {

        rank = "🥉 経験者";

      } else {

        rank = "🪵 初心者";
      }

  }

} else {

    rank = "📚 復習完了";
}

return (
    <div>

      <h2>結果発表</h2>

      <h3>ランク : {rank}</h3>

      <p>
        正解数 :
        {correctCount} /
        {totalQuestions}
      </p>

      <p>
        正答率 :
        {accuracy}%
      </p>

      <p>
        栞数 :
        {bookmarkedCount}
      </p>

      <p>
        Score :
        {score} pt
      </p>

      <p>
  平均残り時間 :
  {averageTime} sec
</p>

      <button onClick={goReview}>
        📋 答案を見る
      </button>

      <button onClick={goMenu}>
        メインメニューへ戻る
      </button>

    </div>
  );
}

export default Result;