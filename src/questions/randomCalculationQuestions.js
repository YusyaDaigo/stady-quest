import { CATEGORIES } from "./categories";

const choiceShuffle = (choices, correctValue) => {
  const shuffled = [...choices].sort(() => Math.random() - 0.5);
  return {
    choices: shuffled.map(String),
    answer: shuffled.findIndex((v) => v === correctValue)
  };
};

const round1 = (num) => Math.round(num * 10) / 10;

export const generateRandomCalculationQuestions = () => {
  const questions = [];

  // 落下距離問題
  {
    const speedKmhOptions = [36, 54, 72, 90];
    const heightOptions = [20, 45, 80, 125];

    const speedKmh =
      speedKmhOptions[Math.floor(Math.random() * speedKmhOptions.length)];
    const height =
      heightOptions[Math.floor(Math.random() * heightOptions.length)];

    const speedMs = speedKmh / 3.6;
    const time = Math.sqrt((2 * height) / 10);
    const distance = Math.round(speedMs * time);

    const wrong1 = Math.round(distance * 0.7);
    const wrong2 = Math.round(distance * 1.4);

    const result = choiceShuffle(
      [`${wrong1}m`, `${distance}m`, `${wrong2}m`],
      `${distance}m`
    );

    questions.push({
      subject: "drone",
      category: CATEGORIES.CALC,

      question:
        `対地速度${speedKmh}km/hで飛行している無人航空機が、高度${height}mで揚力を失った。` +
        `地上に到達するまでの水平距離として最も適切なものはどれか。` +
        `重力加速度は10m/s²、空気抵抗は無視する。`,
      choices: result.choices,
      answer: result.answer,
      explanation:
        `${speedKmh}km/hは${round1(speedMs)}m/sです。` +
        `落下時間は√(2H/g)=√(${2 * height}/10)=約${round1(time)}秒。` +
        `水平距離は${round1(speedMs)} × ${round1(time)} = 約${distance}mです。`
    });
  }

  // 揚力倍率問題
  {
    const densityOptions = [0.8, 0.9, 1.1, 1.2];
    const speedOptions = [0.8, 0.9, 1.1, 1.2];

    const density =
      densityOptions[Math.floor(Math.random() * densityOptions.length)];
    const speed =
      speedOptions[Math.floor(Math.random() * speedOptions.length)];

    const lift = round1(density * speed * speed);

    const wrong1 = round1(lift * 0.8);
    const wrong2 = round1(lift * 1.25);

    const result = choiceShuffle(
      [`${wrong1}倍`, `${lift}倍`, `${wrong2}倍`],
      `${lift}倍`
    );

    questions.push({
      subject: "drone",
      category: CATEGORIES.CALC,

      question:
        `空気密度が${density}倍、速度が${speed}倍になったとき、` +
        `揚力は何倍になるか。`,
      choices: result.choices,
      answer: result.answer,
      explanation:
        `揚力は空気密度に比例し、速度の2乗に比例します。` +
        `${density} × ${speed}² = ${lift} なので、約${lift}倍です。`
    });
  }

  // 回転角速度と推力
  {
    const omegaOptions = [1.1, 1.2, 1.3, 1.4];

    const omega =
      omegaOptions[Math.floor(Math.random() * omegaOptions.length)];

    const thrust = round1(omega * omega);

    const wrong1 = round1(omega);
    const wrong2 = round1(omega * omega * omega);

    const result = choiceShuffle(
      [`${wrong1}倍`, `${thrust}倍`, `${wrong2}倍`],
      `${thrust}倍`
    );

    questions.push({
      subject: "drone",
      category: CATEGORIES.CALC,

      question:
        `回転角速度を${omega}倍にしたとき、推力として最も適切なものはどれか。`,
      choices: result.choices,
      answer: result.answer,
      explanation:
        `推力は回転角速度の2乗に比例します。` +
        `${omega}² = ${thrust} なので、約${thrust}倍です。`
    });
  }

  // 回転角速度と消費パワー
  {
    const omegaOptions = [1.1, 1.2, 1.3, 1.4];

    const omega =
      omegaOptions[Math.floor(Math.random() * omegaOptions.length)];

    const power = round1(omega * omega * omega);

    const wrong1 = round1(omega * omega);
    const wrong2 = round1(omega);

    const result = choiceShuffle(
      [`${wrong1}倍`, `${power}倍`, `${wrong2}倍`],
      `${power}倍`
    );

    questions.push({
      subject: "drone",
      category: CATEGORIES.CALC,

      question:
        `回転角速度を${omega}倍にしたとき、消費パワーとして最も適切なものはどれか。`,
      choices: result.choices,
      answer: result.answer,
      explanation:
        `消費パワーは回転角速度の3乗に比例します。` +
        `${omega}³ = ${power} なので、約${power}倍です。`
    });
  }

  return questions;
};