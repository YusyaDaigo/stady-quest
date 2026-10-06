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
  },

  {
    id: "webdesign-3-theory-original-006",
    subject: "webdesign",
    category: CATEGORIES.INTERNET,
    sourceType: "original",
    questionType: "true_false",
    sourceNumber: 6,

    question:
      "DNSは、ドメイン名に対応するIPアドレスを調べるために利用される仕組みである。正しいか、誤りか。",

    choices: [
      "正しい",
      "誤り"
    ],

    answer: 0,

    explanation:
      "DNSはドメイン名とIPアドレスなどの情報を対応付ける仕組みです。Webブラウザでドメイン名を指定した際の名前解決などに利用されます。"
  },

  {
    id: "webdesign-3-theory-original-007",
    subject: "webdesign",
    category: CATEGORIES.INTERNET,
    sourceType: "original",
    questionType: "true_false",
    sourceNumber: 7,

    question:
      "クライアントサーバ方式では、Webブラウザがサーバーへ要求を送り、サーバーがその要求に応じて応答を返すことがある。正しいか、誤りか。",

    choices: [
      "正しい",
      "誤り"
    ],

    answer: 0,

    explanation:
      "WebではブラウザなどのクライアントがHTTPリクエストを送り、Webサーバーがレスポンスを返すクライアントサーバ方式が広く利用されています。"
  },

  {
    id: "webdesign-3-theory-original-008",
    subject: "webdesign",
    category: CATEGORIES.INTERNET,
    sourceType: "original",
    questionType: "true_false",
    sourceNumber: 8,

    question:
      "公開鍵暗号方式では、暗号化と復号に必ず同一の1本の鍵を使用する。正しいか、誤りか。",

    choices: [
      "正しい",
      "誤り"
    ],

    answer: 1,

    explanation:
      "公開鍵暗号方式では、互いに対応する公開鍵と秘密鍵という異なる鍵を利用します。同一の鍵を共有する方式とは異なります。"
  },

  {
    id: "webdesign-3-theory-original-009",
    subject: "webdesign",
    category: CATEGORIES.OPERATION,
    sourceType: "original",
    questionType: "true_false",
    sourceNumber: 9,

    question:
      "他者が制作した画像は、インターネット上で閲覧できるものであれば、著作権を確認せず自由に自分のWebサイトへ転載できる。正しいか、誤りか。",

    choices: [
      "正しい",
      "誤り"
    ],

    answer: 1,

    explanation:
      "インターネット上で閲覧できることと、自由に転載できることは別です。利用条件や権利関係を確認し、必要に応じて許諾を得る必要があります。"
  },

  {
    id: "webdesign-3-theory-original-010",
    subject: "webdesign",
    category: CATEGORIES.HTML_CSS,
    sourceType: "original",
    questionType: "true_false",
    sourceNumber: 10,

    question:
      "一般にHTMLは文書の構造や意味を表し、CSSは主に表示上の見た目やレイアウトを指定するために利用される。正しいか、誤りか。",

    choices: [
      "正しい",
      "誤り"
    ],

    answer: 0,

    explanation:
      "HTMLは見出し、段落、リンクなど文書の構造や意味を表し、CSSは色、余白、配置などの表示方法を指定する役割を担います。"
  },

  {
    id: "webdesign-3-theory-original-011",
    subject: "webdesign",
    category: CATEGORIES.HTML_CSS,
    sourceType: "original",
    questionType: "true_false",
    sourceNumber: 11,

    question:
      "1つの外部CSSファイルを複数のHTML文書から読み込んで共通利用することができる。正しいか、誤りか。",

    choices: [
      "正しい",
      "誤り"
    ],

    answer: 0,

    explanation:
      "外部スタイルシートは複数ページから共通して読み込めます。サイト全体のデザインを統一し、保守しやすくする方法の1つです。"
  },

  {
    id: "webdesign-3-theory-original-012",
    subject: "webdesign",
    category: CATEGORIES.DESIGN,
    sourceType: "original",
    questionType: "true_false",
    sourceNumber: 12,

    question:
      "レスポンシブWebデザインでは、画面サイズが変化しても常に同じ固定幅のレイアウトだけを表示することが目的である。正しいか、誤りか。",

    choices: [
      "正しい",
      "誤り"
    ],

    answer: 1,

    explanation:
      "レスポンシブWebデザインは、画面幅や端末などに応じてレイアウトや表示を調整し、さまざまな環境で利用しやすくする考え方です。"
  },

  {
    id: "webdesign-3-theory-original-013",
    subject: "webdesign",
    category: CATEGORIES.OPERATION,
    sourceType: "original",
    questionType: "true_false",
    sourceNumber: 13,

    question:
      "Webサイトのデータを定期的にバックアップすることは、サイト運用・管理における対策の1つである。正しいか、誤りか。",

    choices: [
      "正しい",
      "誤り"
    ],

    answer: 0,

    explanation:
      "障害や操作ミスなどでデータが失われた場合に備え、必要なデータを定期的にバックアップすることは運用上重要です。"
  },

  {
    id: "webdesign-3-theory-original-014",
    subject: "webdesign",
    category: CATEGORIES.INTERNET,
    sourceType: "original",
    questionType: "multiple_choice",
    sourceNumber: 14,

    question:
      "HTTPのステータスコード404が示す内容として、最も適切なのはどれか。1つ選べ。",

    choices: [
      "要求されたリソースが見つからない",
      "通信が必ず暗号化されている",
      "サーバーが正常終了した",
      "ドメイン名の登録が完了した"
    ],

    answer: 0,

    explanation:
      "404 Not Foundは、要求されたリソースをサーバーが見つけられない場合に用いられるHTTPステータスコードです。"
  },

  {
    id: "webdesign-3-theory-original-015",
    subject: "webdesign",
    category: CATEGORIES.INTERNET,
    sourceType: "original",
    questionType: "multiple_choice",
    sourceNumber: 15,

    question:
      "Web技術の標準化に関わる団体として、最も適切なのはどれか。1つ選べ。",

    choices: [
      "W3C",
      "WHO",
      "IMF",
      "IOC"
    ],

    answer: 0,

    explanation:
      "W3CはWorld Wide Web Consortiumの略で、Webに関する標準化活動を行う団体の1つです。"
  },

  {
    id: "webdesign-3-theory-original-016",
    subject: "webdesign",
    category: CATEGORIES.HTML_CSS,
    sourceType: "original",
    questionType: "multiple_choice",
    sourceNumber: 16,

    question:
      "HTMLで第2レベルの見出しを表す要素として、適切なのはどれか。1つ選べ。",

    choices: [
      "<p>",
      "<h2>",
      "<title>",
      "<strong>"
    ],

    answer: 1,

    explanation:
      "h1からh6は見出しを表す要素です。第2レベルの見出しにはh2要素を使用します。"
  },

  {
    id: "webdesign-3-theory-original-017",
    subject: "webdesign",
    category: CATEGORIES.HTML_CSS,
    sourceType: "original",
    questionType: "multiple_choice",
    sourceNumber: 17,

    question:
      "class=\"notice\" が指定された要素をCSSで選択するセレクターとして、適切なのはどれか。1つ選べ。",

    choices: [
      "#notice",
      ".notice",
      "*notice",
      "@notice"
    ],

    answer: 1,

    explanation:
      "classセレクターにはピリオドを使用します。したがって class=\"notice\" の要素には .notice を使用します。"
  },

  {
    id: "webdesign-3-theory-original-018",
    subject: "webdesign",
    category: CATEGORIES.HTML_CSS,
    sourceType: "original",
    questionType: "multiple_choice",
    sourceNumber: 18,

    question:
      "ECMAScriptと最も関係が深いものはどれか。1つ選べ。",

    choices: [
      "JavaScriptの言語仕様",
      "JPEG画像の圧縮方式",
      "DNSの名前解決方式",
      "CSSの画像形式"
    ],

    answer: 0,

    explanation:
      "ECMAScriptはJavaScriptなどの基礎となる標準化された言語仕様です。"
  },

  {
    id: "webdesign-3-theory-original-019",
    subject: "webdesign",
    category: CATEGORIES.DESIGN,
    sourceType: "original",
    questionType: "multiple_choice",
    sourceNumber: 19,

    question:
      "写真のように多数の色や連続した階調を含む画像をWebで扱う場合に、一般的によく利用される画像形式はどれか。1つ選べ。",

    choices: [
      "JPEG",
      "TXT",
      "CSV",
      "HTML"
    ],

    answer: 0,

    explanation:
      "JPEGは写真などの多数の色や連続階調を含む画像で広く利用される画像形式です。"
  },

  {
    id: "webdesign-3-theory-original-020",
    subject: "webdesign",
    category: CATEGORIES.DESIGN,
    sourceType: "original",
    questionType: "multiple_choice",
    sourceNumber: 20,

    question:
      "複数ページで構成されたWebサイトのナビゲーションとして、利用者が目的のページを探しやすくするために適切なものはどれか。1つ選べ。",

    choices: [
      "ページごとに主要メニューの位置を大きく変える",
      "主要なナビゲーションの配置や表現に一貫性を持たせる",
      "リンクであることが分からない表現に統一する",
      "現在位置を示す情報をすべて削除する"
    ],

    answer: 1,

    explanation:
      "主要なナビゲーションに一貫性を持たせることで、利用者が操作方法を予測しやすくなり、サイト内を移動しやすくなります。"
  },

  {
    id: "webdesign-3-theory-original-021",
    subject: "webdesign",
    category: CATEGORIES.DESIGN,
    sourceType: "original",
    questionType: "multiple_choice",
    sourceNumber: 21,

    question:
      "サイトマップを作成する主な目的として、最も適切なのはどれか。1つ選べ。",

    choices: [
      "Webサイトの情報構造やページ同士の関係を整理する",
      "画像を自動的に圧縮する",
      "すべての文字色を同じ色にする",
      "ブラウザの履歴を削除する"
    ],

    answer: 0,

    explanation:
      "サイトマップはサイト内の情報構造やページ階層、ページ同士の関係を整理・把握するために利用されます。"
  },

  {
    id: "webdesign-3-theory-original-022",
    subject: "webdesign",
    category: CATEGORIES.ACCESSIBILITY,
    sourceType: "original",
    questionType: "multiple_choice",
    sourceNumber: 22,

    question:
      "文字情報を読みやすくするためのアクセシビリティ上の配慮として、最も適切なのはどれか。1つ選べ。",

    choices: [
      "文字色と背景色のコントラストを十分に確保する",
      "すべての文字を極端に小さくする",
      "重要な情報を色の違いだけで伝える",
      "本文をすべて画像として配置する"
    ],

    answer: 0,

    explanation:
      "文字と背景の十分なコントラストは、さまざまな利用者が内容を読み取りやすくするための基本的な配慮です。"
  },

  {
    id: "webdesign-3-theory-original-023",
    subject: "webdesign",
    category: CATEGORIES.ACCESSIBILITY,
    sourceType: "original",
    questionType: "multiple_choice",
    sourceNumber: 23,

    question:
      "Webページをキーボードだけで利用するユーザーへの配慮として、最も適切なのはどれか。1つ選べ。",

    choices: [
      "操作可能な要素へキーボードで移動・操作できるようにする",
      "すべてのリンクをマウス専用にする",
      "フォーカスの移動を完全に禁止する",
      "入力フォームをすべて画像に置き換える"
    ],

    answer: 0,

    explanation:
      "マウスを利用できない場合でも操作できるよう、リンクやフォームなどをキーボードから利用可能にすることが重要です。"
  },

  {
    id: "webdesign-3-theory-original-024",
    subject: "webdesign",
    category: CATEGORIES.OPERATION,
    sourceType: "original",
    questionType: "multiple_choice",
    sourceNumber: 24,

    question:
      "公開中のWebサイトを運用する際の対応として、最も適切なのはどれか。1つ選べ。",

    choices: [
      "更新前の確認やバックアップを必要に応じて行う",
      "公開後は内容を一切確認しない",
      "障害が起きても記録を残さない",
      "管理用パスワードを誰でも見られる場所へ掲載する"
    ],

    answer: 0,

    explanation:
      "Webサイトの運用では、更新内容の確認、バックアップ、障害対応など、継続的な管理が重要です。"
  },

  {
    id: "webdesign-3-theory-original-025",
    subject: "webdesign",
    category: CATEGORIES.OPERATION,
    sourceType: "original",
    questionType: "multiple_choice",
    sourceNumber: 25,

    question:
      "長時間のVDT作業を行う際の作業環境として、最も適切なのはどれか。1つ選べ。",

    choices: [
      "姿勢や画面位置などを調整し、適切に休止を取りながら作業する",
      "休止せず同じ姿勢で作業し続ける",
      "画面を必ず極端に暗くする",
      "作業場所を整理せず機器の周囲へ物を積み上げる"
    ],

    answer: 0,

    explanation:
      "VDT作業では、姿勢や機器の配置、作業環境に配慮し、身体への負担を減らしながら作業することが重要です。"
  }
];
