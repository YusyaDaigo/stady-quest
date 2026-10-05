export const webDesignPracticalTasks = [
  {
    id: "webdesign-3-practical-sample-001",
    exam: "webdesign",
    level: 3,
    itemType: "task",
    taskType: "web_editing",

    title: "実技サンプル課題 1",

    instructions: [
      "index.html の h1 の文字を「Study QUEST Web Lab」に変更する。",
      "id が message の p 要素に highlight クラスを追加する。",
      "style.css に .highlight の font-weight: 700; を設定する。",
      "style.css の .card に border-radius: 12px; を設定する。"
    ],

    workspace: {
      entryFile: "index.html",

      starterFiles: [
        {
          path: "index.html",
          language: "html",
          editable: true,
          content: `<!doctype html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>Web Practice</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <main class="page">
    <h1>Web Practice</h1>

    <p id="message">
      指定された条件に合わせてこのページを編集してください。
    </p>

    <section class="card">
      <h2>課題</h2>
      <p>HTMLとCSSの基本編集を確認します。</p>
    </section>
  </main>
</body>
</html>`
        },

        {
          path: "style.css",
          language: "css",
          editable: true,
          content: `body {
  font-family: sans-serif;
  margin: 0;
  background: #f2f2f2;
}

.page {
  max-width: 760px;
  margin: 40px auto;
  padding: 24px;
  background: white;
}

.card {
  border: 1px solid #777;
  padding: 20px;
}`
        }
      ]
    },

    evaluation: {
      checks: [
        {
          id: "heading",
          label: "h1 の文字が指定どおり",
          type: "html_text",
          file: "index.html",
          selector: "h1",
          expected: "Study QUEST Web Lab"
        },
        {
          id: "highlight-class",
          label: "#message に highlight クラスがある",
          type: "html_class",
          file: "index.html",
          selector: "#message",
          className: "highlight"
        },
        {
          id: "highlight-weight",
          label: ".highlight の font-weight が 700",
          type: "css_property",
          file: "style.css",
          selector: ".highlight",
          property: "font-weight",
          expected: "700"
        },
        {
          id: "card-radius",
          label: ".card の border-radius が 12px",
          type: "css_property",
          file: "style.css",
          selector: ".card",
          property: "border-radius",
          expected: "12px"
        }
      ]
    }
  },

  {
    id: "webdesign-3-practical-sample-002",
    exam: "webdesign",
    level: 3,
    itemType: "task",
    taskType: "web_editing",

    title: "実技サンプル課題 2",

    instructions: [
      "index.html の h2 の文字を「プロフィール」に変更する。",
      "id が intro の p 要素に lead クラスを追加する。",
      "style.css に .lead の text-align: center; を設定する。",
      "style.css の .panel に padding: 24px; を設定する。"
    ],

    workspace: {
      entryFile: "index.html",

      starterFiles: [
        {
          path: "index.html",
          language: "html",
          editable: true,
          content: `<!doctype html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>Profile Practice</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <main class="wrapper">
    <h1>Sample Site</h1>

    <section class="panel">
      <h2>About</h2>

      <p id="intro">
        このページはプロフィール紹介の練習用ページです。
      </p>
    </section>
  </main>
</body>
</html>`
        },

        {
          path: "style.css",
          language: "css",
          editable: true,
          content: `body {
  font-family: sans-serif;
  background: #eeeeee;
}

.wrapper {
  max-width: 720px;
  margin: 40px auto;
}

.panel {
  background: white;
  border: 1px solid #888;
}`
        }
      ]
    },

    evaluation: {
      checks: [
        {
          id: "profile-heading",
          label: "h2 の文字が指定どおり",
          type: "html_text",
          file: "index.html",
          selector: "h2",
          expected: "プロフィール"
        },
        {
          id: "lead-class",
          label: "#intro に lead クラスがある",
          type: "html_class",
          file: "index.html",
          selector: "#intro",
          className: "lead"
        },
        {
          id: "lead-align",
          label: ".lead の text-align が center",
          type: "css_property",
          file: "style.css",
          selector: ".lead",
          property: "text-align",
          expected: "center"
        },
        {
          id: "panel-padding",
          label: ".panel の padding が 24px",
          type: "css_property",
          file: "style.css",
          selector: ".panel",
          property: "padding",
          expected: "24px"
        }
      ]
    }
  }
];
