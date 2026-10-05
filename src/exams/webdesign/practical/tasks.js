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
,

  {
    id: "webdesign-3-practical-sample-003",
    exam: "webdesign",
    level: 3,
    itemType: "task",
    taskType: "web_editing",

    title: "実技サンプル課題 3",

    instructions: [
      "id が company-link の a 要素のリンク先を company.html に変更する。",
      "id が contact-link の a 要素のリンク先を contact.html に変更する。",
      "nav 要素内の h2 の文字を「サイトメニュー」に変更する。",
      "style.css の .nav-link に text-decoration: none; を設定する。"
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
  <title>Navigation Practice</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <main class="page">
    <h1>Study QUEST Cafe</h1>

    <nav>
      <h2>Menu</h2>

      <a
        id="company-link"
        class="nav-link"
        href="#"
      >
        会社案内
      </a>

      <a
        id="contact-link"
        class="nav-link"
        href="#"
      >
        お問い合わせ
      </a>
    </nav>
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
}

.page {
  max-width: 720px;
  margin: 40px auto;
}

.nav-link {
  display: block;
  margin: 12px 0;
}`
        }
      ]
    },

    evaluation: {
      checks: [
        {
          id: "company-href",
          label: "会社案内のリンク先が company.html",
          type: "html_attribute",
          file: "index.html",
          selector: "#company-link",
          attribute: "href",
          expected: "company.html"
        },
        {
          id: "contact-href",
          label: "お問い合わせのリンク先が contact.html",
          type: "html_attribute",
          file: "index.html",
          selector: "#contact-link",
          attribute: "href",
          expected: "contact.html"
        },
        {
          id: "nav-heading",
          label: "nav 内 h2 の文字が指定どおり",
          type: "html_text",
          file: "index.html",
          selector: "nav h2",
          expected: "サイトメニュー"
        },
        {
          id: "nav-decoration",
          label: ".nav-link の text-decoration が none",
          type: "css_property",
          file: "style.css",
          selector: ".nav-link",
          property: "text-decoration",
          expected: "none"
        }
      ]
    }
  },

  {
    id: "webdesign-3-practical-sample-004",
    exam: "webdesign",
    level: 3,
    itemType: "task",
    taskType: "web_editing",

    title: "実技サンプル課題 4",

    instructions: [
      "style.css の .hero に background-color: #e8f4ff; を設定する。",
      "style.css の .hero に color: #123456; を設定する。",
      "style.css の .content に max-width: 680px; を設定する。",
      "style.css の .content に margin: 0 auto; を設定する。"
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
  <title>Layout Practice</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header class="hero">
    <h1>沖縄ウェブ制作室</h1>
    <p>見やすいページを作る練習です。</p>
  </header>

  <main class="content">
    <h2>お知らせ</h2>
    <p>
      CSSを編集して指定されたレイアウトにしてください。
    </p>
  </main>
</body>
</html>`
        },

        {
          path: "style.css",
          language: "css",
          editable: true,
          content: `body {
  margin: 0;
  font-family: sans-serif;
}

.hero {
  padding: 32px;
}

.content {
  padding: 24px;
}`
        }
      ]
    },

    evaluation: {
      checks: [
        {
          id: "hero-bg",
          label: ".hero の背景色が #e8f4ff",
          type: "css_property",
          file: "style.css",
          selector: ".hero",
          property: "background-color",
          expected: "#e8f4ff"
        },
        {
          id: "hero-color",
          label: ".hero の文字色が #123456",
          type: "css_property",
          file: "style.css",
          selector: ".hero",
          property: "color",
          expected: "#123456"
        },
        {
          id: "content-width",
          label: ".content の max-width が 680px",
          type: "css_property",
          file: "style.css",
          selector: ".content",
          property: "max-width",
          expected: "680px"
        },
        {
          id: "content-margin",
          label: ".content の margin が 0 auto",
          type: "css_property",
          file: "style.css",
          selector: ".content",
          property: "margin",
          expected: "0 auto"
        }
      ]
    }
  },

  {
    id: "webdesign-3-practical-sample-005",
    exam: "webdesign",
    level: 3,
    itemType: "task",
    taskType: "web_editing",

    title: "実技サンプル課題 5",

    instructions: [
      "index.html の id が about-link のリンク先を about.html に変更する。",
      "about.html の id が home-link のリンク先を index.html に変更する。",
      "about.html の h2 の文字を「私たちについて」に変更する。",
      "style.css の .nav に display: flex; を設定する。"
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
  <title>Home</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <h1>Island Studio</h1>

    <nav class="nav">
      <a href="index.html">
        ホーム
      </a>

      <a
        id="about-link"
        href="#"
      >
        私たちについて
      </a>
    </nav>
  </header>

  <main>
    <p>トップページです。</p>
  </main>
</body>
</html>`
        },

        {
          path: "about.html",
          language: "html",
          editable: true,
          content: `<!doctype html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>About</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <h1>Island Studio</h1>

    <nav class="nav">
      <a
        id="home-link"
        href="#"
      >
        ホーム
      </a>

      <a href="about.html">
        私たちについて
      </a>
    </nav>
  </header>

  <main>
    <h2>About Us</h2>
    <p>
      ウェブ制作について学ぶサンプルページです。
    </p>
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
  max-width: 760px;
  margin: 40px auto;
}

.nav {
  gap: 20px;
}`
        }
      ]
    },

    evaluation: {
      checks: [
        {
          id: "about-link",
          label: "index.html から about.html へリンク",
          type: "html_attribute",
          file: "index.html",
          selector: "#about-link",
          attribute: "href",
          expected: "about.html"
        },
        {
          id: "home-link",
          label: "about.html から index.html へリンク",
          type: "html_attribute",
          file: "about.html",
          selector: "#home-link",
          attribute: "href",
          expected: "index.html"
        },
        {
          id: "about-heading",
          label: "about.html の h2 が指定どおり",
          type: "html_text",
          file: "about.html",
          selector: "h2",
          expected: "私たちについて"
        },
        {
          id: "nav-flex",
          label: ".nav の display が flex",
          type: "css_property",
          file: "style.css",
          selector: ".nav",
          property: "display",
          expected: "flex"
        }
      ]
    }
  }

];
