import {
  CATEGORIES
} from "./categories";

export const theoryQuestions = [
  {
    id: "webdesign-3-theory-original-001",
    subject: "webdesign",
    category: CATEGORIES.INTERNET,
    sourceType: "original",
    questionType: "true_false",
    sourceNumber: 1,

    question:
      "HTTPSを利用したWeb通信では、TLSによってブラウザとWebサーバー間の通信内容を暗号化できる。正しいか、誤りか。",

    choices: [
      "正しい",
      "誤り"
    ],

    answer: 0,

    explanation:
      "HTTPSはHTTPをTLSで保護する仕組みです。通信内容の暗号化に加えて、通信相手の認証や通信内容の改ざん検知にも利用されます。"
  },

  {
    id: "webdesign-3-theory-original-002",
    subject: "webdesign",
    category: CATEGORIES.HTML_CSS,
    sourceType: "original",
    questionType: "true_false",
    sourceNumber: 2,

    question:
      "CSSでは、idセレクターを「.」、classセレクターを「#」で指定する。正しいか、誤りか。",

    choices: [
      "正しい",
      "誤り"
    ],

    answer: 1,

    explanation:
      "逆です。idセレクターは「#」、classセレクターは「.」を使います。例えば id=\"main\" は #main、class=\"card\" は .card と指定します。"
  },

  {
    id: "webdesign-3-theory-original-003",
    subject: "webdesign",
    category: CATEGORIES.HTML_CSS,
    sourceType: "original",
    questionType: "multiple_choice",
    sourceNumber: 3,

    question:
      "現在のHTML文書から同じフォルダにある profile.html へ移動するリンクとして、適切なのはどれか。1つ選べ。",

    choices: [
      "<link href=\"profile.html\">プロフィール</link>",
      "<a href=\"profile.html\">プロフィール</a>",
      "<a src=\"profile.html\">プロフィール</a>",
      "<href=\"profile.html\">プロフィール</href>"
    ],

    answer: 1,

    explanation:
      "HTMLでハイパーリンクを作る場合はa要素を使用し、リンク先をhref属性に指定します。したがって <a href=\"profile.html\">プロフィール</a> が適切です。"
  },

  {
    id: "webdesign-3-theory-original-004",
    subject: "webdesign",
    category: CATEGORIES.DESIGN,
    sourceType: "original",
    questionType: "multiple_choice",
    sourceNumber: 4,

    question:
      "CSSで要素に「padding: 20px;」を設定した場合、20pxの余白が設けられる位置として最も適切なのはどれか。1つ選べ。",

    choices: [
      "内容領域と境界線の間",
      "境界線の外側",
      "隣接する要素同士の間だけ",
      "ブラウザ画面の外側"
    ],

    answer: 0,

    explanation:
      "paddingは要素の内容領域とborderの間に設ける内側の余白です。borderの外側の余白にはmarginを使用します。"
  },

  {
    id: "webdesign-3-theory-original-005",
    subject: "webdesign",
    category: CATEGORIES.ACCESSIBILITY,
    sourceType: "original",
    questionType: "multiple_choice",
    sourceNumber: 5,

    question:
      "HTMLのimg要素に指定するalt属性の主な目的として、最も適切なのはどれか。1つ選べ。",

    choices: [
      "画像ファイルの容量を小さくする",
      "画像の表示速度を必ず高速化する",
      "画像を利用できない場合に代替となるテキストを提供する",
      "画像を自動的に別形式へ変換する"
    ],

    answer: 2,

    explanation:
      "alt属性は画像の代替テキストを指定するために使用します。画像を表示できない場合や、スクリーンリーダーを利用する場合などに重要です。"
  }
];
