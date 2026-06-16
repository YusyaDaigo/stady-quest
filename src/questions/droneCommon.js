import { CATEGORIES } from "./categories";

export const commonQuestions = [

    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "無人航空機を飛行させる際の体調管理として、最も適切なものはどれか？",
        choices: [
          "体調が悪くても短時間であれば飛行してよい",
          "睡眠不足や疲労がある場合は飛行を避ける",
          "補助者がいれば操縦者の体調は問題にならない"
        ],
        answer: 1,
        explanation:
          "体調不良、睡眠不足、疲労は判断力や注意力の低下につながるため、飛行を避ける必要があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
        
        question:
          "飛行前に行う現地調査として、適切なものはどれか？",
        choices: [
          "障害物や歩行者、自動車の通行状況を確認する",
          "飛行経験のある場所なら現地確認は不要である",
          "離陸後に機体カメラで周囲を確認すればよい"
        ],
        answer: 0,
        explanation:
          "飛行前には、障害物、離着陸場所、歩行者や車両、有人航空機の状況などを確認する必要があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "飛行計画の作成について、最も適切なものはどれか？",
        choices: [
          "過去に飛行した場所では同じ計画をそのまま使えばよい",
          "緊急着陸地点や安全に旋回できる場所も考慮する",
          "飛行計画の通報は原則として飛行後に行う"
        ],
        answer: 1,
        explanation:
          "飛行計画では、通常の経路だけでなく、緊急着陸地点や安全にホバリング・旋回できる場所も考慮します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "無人航空機と有人航空機の飛行経路が接近する場合、適切な対応はどれか？",
        choices: [
          "無人航空機側が回避行動を取る",
          "有人航空機側が必ず回避する",
          "高度が低ければそのまま飛行を続けてよい"
        ],
        answer: 0,
        explanation:
          "航空機の航行の安全を確保するため、無人航空機側が回避行動を取る必要があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "飛行後の機体やバッテリーの保管として、適切なものはどれか？",
        choices: [
          "バッテリーを接続したまま保管する",
          "次回すぐ使えるよう満充電のまま長期間保管する",
          "機体やバッテリーを安全な状態で適切な場所に保管する"
        ],
        answer: 2,
        explanation:
          "飛行後は機体やバッテリーを安全な状態にし、適切な場所で保管します。バッテリー接続状態での保管は避けるべきです。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "リモートID機能により発信される情報として、正しいものはどれか？",
        choices: [
          "所有者や使用者の氏名が発信される",
          "製造番号、登録記号、位置、速度、高度、時刻などが含まれる",
          "登録記号のみが1分に1回発信される"
        ],
        answer: 1,
        explanation:
          "リモートIDでは、静的情報と動的情報が発信されますが、所有者や使用者の情報は含まれません。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "高度150m以上の飛行禁止空域について、正しいものはどれか？",
        choices: [
          "海抜高度が150m以上の空域を指す",
          "無人航空機の直下の地表または水面から150m以上の空域を指す",
          "山岳地では高度制限を考慮しなくてよい"
        ],
        answer: 1,
        explanation:
          "高度150m以上とは、海抜ではなく、無人航空機の直下の地表または水面からの高さで判断します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "リチウムポリマーバッテリーの長期保管として、適切なものはどれか？",
        choices: [
          "満充電の状態で保管する",
          "完全に放電した状態で保管する",
          "おおむね60%程度の充電状態で保管する"
        ],
        answer: 2,
        explanation:
          "リチウムポリマーバッテリーは、長期間使用しない場合、おおむね60%程度の充電状態で保管することが望ましいです。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "マルチローターの基本操作の説明として、正しいものはどれか？",
        choices: [
          "上下操作をスロットル、前後移動をエレベーターという",
          "上下操作をエレベーター、前後移動をスロットルという",
          "左右旋回操作をエルロンという"
        ],
        answer: 0,
        explanation:
          "マルチローターでは、上下操作をスロットル、前後移動をエレベーター、左右移動をエルロン、左右旋回をラダーといいます。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "リスク管理の考え方として、最も適切なものはどれか？",
        choices: [
          "リスクは必ずゼロにしなければならない",
          "ハザードを特定し、リスクを許容可能な程度まで低減する",
          "法令を守っていればリスク評価は不要である"
        ],
        answer: 1,
        explanation:
          "リスク管理では、ハザードを特定し、発生確率や被害を低減して、リスクを許容可能な程度に抑えることが重要です。"
      }
    ];
    