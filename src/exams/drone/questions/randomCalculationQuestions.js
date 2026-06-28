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

  // 旋回半径とバンク角から飛行速度
  {
    const patterns = [
      { radius: 180, bank: 12, tan: 0.21 },
      { radius: 200, bank: 10, tan: 0.18 },
      { radius: 240, bank: 10, tan: 0.18 },
      { radius: 300, bank: 17, tan: 0.32 }
    ];

    const pattern =
      patterns[Math.floor(Math.random() * patterns.length)];

    const speed =
      round1(
        Math.sqrt(
          pattern.radius * 9.8 * pattern.tan
        )
      );

    const wrong1 = round1(speed * 0.9);
    const wrong2 = round1(speed * 1.1);

    const result = choiceShuffle(
      [
        `${wrong1}m/s`,
        `${speed}m/s`,
        `${wrong2}m/s`
      ],
      `${speed}m/s`
    );

    questions.push({
      subject: "drone",
      category: CATEGORIES.CALC,

      question:
        `旋回半径が${pattern.radius}m、バンク角が${pattern.bank}°のときの飛行速度として最も適切なものはどれか。` +
        `なお、重力加速度は9.8m/s²、tan${pattern.bank}°は${pattern.tan}とする。`,
      choices: result.choices,
      answer: result.answer,
      explanation:
        `旋回半径 R = V² / (g × tanθ) より、` +
        `V² = ${pattern.radius} × 9.8 × ${pattern.tan}。` +
        `V は約${speed}m/sです。`
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

  // 旋回半径と速度からバンク角
  {
    const patterns = [
      {
        radius: 300,
        speed: 30,
        choices: [
          { angle: "10°", tan: 0.18 },
          { angle: "17°", tan: 0.32 },
          { angle: "20°", tan: 0.36 }
        ],
        answer: "17°"
      },
      {
        radius: 250,
        speed: 28,
        choices: [
          { angle: "10°", tan: 0.18 },
          { angle: "15°", tan: 0.27 },
          { angle: "20°", tan: 0.36 }
        ],
        answer: "20°"
      }
    ];

    const pattern =
      patterns[Math.floor(Math.random() * patterns.length)];

    const result = choiceShuffle(
      pattern.choices.map((c) => c.angle),
      pattern.answer
    );

    questions.push({
      subject: "drone",
      category: CATEGORIES.CALC,

      question:
        `旋回半径が${pattern.radius}m、速度が${pattern.speed}m/sのときのバンク角として最も適切なものはどれか。` +
        `なお、重力加速度は9.8m/s²、` +
        pattern.choices
          .map((c) => `tan${c.angle}=${c.tan}`)
          .join("、") +
        "とする。",

      choices: result.choices,
      answer: result.answer,

      explanation:
        `R = V² / (g × tanθ) より、` +
        `tanθ = ${pattern.speed}² / (${pattern.radius} × 9.8) で求めます。` +
        `最も近い値の角度を選びます。`
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

  // 推力から回転角速度
  {
    const patterns = [
      { density: 1.0, omega: 10 },
      { density: 1.2, omega: 10 },
      { density: 0.9, omega: 12 },
      { density: 0.8, omega: 15 }
    ];

    const pattern =
      patterns[Math.floor(Math.random() * patterns.length)];

    const thrust =
      round1(
        pattern.density *
        pattern.omega *
        pattern.omega
      );

    const correct =
      `${pattern.omega}rad/s`;

    const result = choiceShuffle(
      [
        `${round1(pattern.omega * 0.8)}rad/s`,
        correct,
        `${round1(pattern.omega * 1.2)}rad/s`
      ],
      correct
    );

    questions.push({
      subject: "drone",
      category: CATEGORIES.CALC,

      question:
        `推力Tが${thrust}、空気密度ρが${pattern.density}のとき、` +
        `回転角速度ωとして最も適切なものはどれか。`,

      choices: result.choices,
      answer: result.answer,

      explanation:
        `ω = √(T / ρ) = √(${thrust} / ${pattern.density}) = ${pattern.omega}rad/s`
    });
  }

  // 消費パワーから回転角速度
  {
    const omegaOptions =
      [10, 12, 15, 20];

    const omega =
      omegaOptions[
        Math.floor(
          Math.random() *
          omegaOptions.length
        )
      ];

    const power =
      omega * omega * omega;

    const correct =
      `${omega}rad/s`;

    const result = choiceShuffle(
      [
        `${round1(omega * 0.8)}rad/s`,
        correct,
        `${round1(omega * 1.2)}rad/s`
      ],
      correct
    );

    questions.push({
      subject: "drone",
      category: CATEGORIES.CALC,

      question:
        `消費パワーPが${power}のとき、` +
        `回転角速度ωとして最も適切なものはどれか。`,

      choices: result.choices,
      answer: result.answer,

      explanation:
        `ω = ∛P = ∛${power} = ${omega}rad/s`
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

  // 揚抗比から滑空角
  {
    const patterns = [
      {
        liftDragRatio: 10,
        correctAngle: "6°",
        tanChoices: [
          { angle: "5°", tan: 0.087 },
          { angle: "6°", tan: 0.105 },
          { angle: "10°", tan: 0.176 }
        ]
      },
      {
        liftDragRatio: 12,
        correctAngle: "5°",
        tanChoices: [
          { angle: "4°", tan: 0.070 },
          { angle: "5°", tan: 0.087 },
          { angle: "6°", tan: 0.105 }
        ]
      }
    ];

    const pattern =
      patterns[Math.floor(Math.random() * patterns.length)];

    const result = choiceShuffle(
      pattern.tanChoices.map((item) => item.angle),
      pattern.correctAngle
    );

    questions.push({
      subject: "drone",
      category: CATEGORIES.CALC,

      question:
        `揚抗比が${pattern.liftDragRatio}の飛行機が定常滑空飛行を行うとき、` +
        `滑空角として最も適切なものはどれか。` +
        pattern.tanChoices
          .map((item) => `tan${item.angle}=${item.tan}`)
          .join("、") +
        "とする。",
      choices: result.choices,
      answer: result.answer,
      explanation:
        `滑空角は tanθ = 1 / 揚抗比 で求めます。` +
        `1/${pattern.liftDragRatio} = ${round1(1 / pattern.liftDragRatio)} となるため、` +
        `最も近いtan値の角度を選びます。`
    });
  }

  // 揚力・速度・空気密度を求める問題
  {
    const patterns = [
      {
        density: 1.0,
        speed: 10
      },
      {
        density: 1.2,
        speed: 8
      },
      {
        density: 0.9,
        speed: 12
      },
      {
        density: 0.8,
        speed: 15
      }
    ];

    const pattern =
      patterns[Math.floor(Math.random() * patterns.length)];

    const lift =
      round1(pattern.density * pattern.speed * pattern.speed);

    const questionType =
      ["lift", "speed", "density"][
        Math.floor(Math.random() * 3)
      ];

    if (questionType === "lift") {
      const correct = `${lift}`;

      const result = choiceShuffle(
        [
          `${round1(lift * 0.8)}`,
          correct,
          `${round1(lift * 1.25)}`
        ],
        correct
      );

      questions.push({
        subject: "drone",
        category: CATEGORIES.CALC,

      question:
        `空気密度が${pattern.density}、速度が${pattern.speed}m/sのとき、` +
        `揚力として最も適切なものはどれか。`,
        choices: result.choices,
        answer: result.answer,
        explanation:
          `揚力 = 空気密度 × 速度² より、` +
          `${pattern.density} × ${pattern.speed}² = ${lift} です。`
      });
    }

    if (questionType === "speed") {
      const correct = `${pattern.speed}m/s`;

      const result = choiceShuffle(
        [
          `${round1(pattern.speed * 0.8)}m/s`,
          correct,
          `${round1(pattern.speed * 1.2)}m/s`
        ],
        correct
      );

      questions.push({
        subject: "drone",
        category: CATEGORIES.CALC,

      question:
        `空気密度が${pattern.density}、速度が${pattern.speed}m/sのとき、` +
        `揚力として最も適切なものはどれか。`,
        choices: result.choices,
        answer: result.answer,
        explanation:
          `揚力 = 空気密度 × 速度² より、` +
          `速度 = √(揚力 / 空気密度) = √(${lift} / ${pattern.density}) = ${pattern.speed}m/s です。`
      });
    }

    if (questionType === "density") {
      const correct = `${pattern.density}`;

      const result = choiceShuffle(
        [
          `${round1(pattern.density * 0.8)}`,
          correct,
          `${round1(pattern.density * 1.25)}`
        ],
        correct
      );

      questions.push({
        subject: "drone",
        category: CATEGORIES.CALC,

        question:
        `揚力が${lift}、速度が${pattern.speed}m/sのとき、` +
        `空気密度として最も適切なものはどれか。`,
        choices: result.choices,
        answer: result.answer,
        explanation:
          `揚力 = 空気密度 × 速度² より、` +
          `空気密度 = 揚力 / 速度² = ${lift} / ${pattern.speed}² = ${pattern.density} です。`
      });
    }
  }

  // フレネルゾーン半径
  {
    const patterns = [
      { distance: 50, frequencyGhz: 2.4 },
      { distance: 80, frequencyGhz: 2.4 },
      { distance: 100, frequencyGhz: 5.7 },
      { distance: 120, frequencyGhz: 5.7 }
    ];

    const pattern =
      patterns[Math.floor(Math.random() * patterns.length)];

    const useSixtyPercent =
      Math.random() < 0.5;

    const frequencyHz =
      pattern.frequencyGhz * 1000000000;

    const wavelength =
      300000000 / frequencyHz;

    const d1 =
      pattern.distance / 2;

    const d2 =
      pattern.distance / 2;

    const radius100 =
      Math.sqrt(
        wavelength * d1 * d2 /
        (d1 + d2)
      );

    const radius =
      round1(
        useSixtyPercent
          ? radius100 * 0.6
          : radius100
      );

    const correct =
      `${radius}m`;

    const result = choiceShuffle(
      [
        `${round1(radius * 0.7)}m`,
        correct,
        `${round1(radius * 1.3)}m`
      ],
      correct
    );

    questions.push({
      subject: "drone",
      category: CATEGORIES.CALC,

      question:
        `送受信アンテナ間の距離が${pattern.distance}mで、` +
        `中心地点におけるフレネルゾーン` +
        `${useSixtyPercent ? "60%半径" : "半径"}として最も適切なものはどれか。` +
        `使用周波数は${pattern.frequencyGhz}GHz、光速度は3×10⁸m/sとする。`,

      choices: result.choices,
      answer: result.answer,

      explanation:
        `波長 λ = c / f = 3×10⁸ / (${pattern.frequencyGhz}×10⁹) = 約${round1(wavelength)}m。` +
        `中心地点なので d1 = d2 = ${d1}m。` +
        `フレネルゾーン半径は √(λ×d1×d2/(d1+d2)) = 約${round1(radius100)}m。` +
        `${useSixtyPercent ? `60%半径なので ${round1(radius100)} × 0.6 = 約${radius}mです。` : `したがって約${radius}mです。`}`
    });
  }

  console.log(questions);

  return questions;
};