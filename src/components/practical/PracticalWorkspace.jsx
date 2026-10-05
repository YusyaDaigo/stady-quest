import {
  useMemo,
  useState
} from "react";

const escapeRegExp = (value) => {
  return value.replace(
    /[.*+?^${}()|[\]\\]/g,
    "\\$&"
  );
};

const getCssProperty = (
  cssText,
  selector,
  property
) => {
  const selectorPattern =
    new RegExp(
      `${escapeRegExp(selector)}\\s*\\{([^}]*)\\}`,
      "i"
    );

  const ruleMatch =
    cssText.match(selectorPattern);

  if (!ruleMatch) {
    return null;
  }

  const declarations =
    ruleMatch[1]
      .split(";")
      .map((item) => item.trim())
      .filter(Boolean);

  for (const declaration of declarations) {
    const separatorIndex =
      declaration.indexOf(":");

    if (separatorIndex === -1) {
      continue;
    }

    const key =
      declaration
        .slice(0, separatorIndex)
        .trim()
        .toLowerCase();

    const value =
      declaration
        .slice(separatorIndex + 1)
        .trim();

    if (
      key === property.toLowerCase()
    ) {
      return value;
    }
  }

  return null;
};

const evaluateTask = (
  task,
  files
) => {
  return task.evaluation.checks.map(
    (check) => {
      let passed = false;

      if (
        check.type === "html_text"
      ) {
        const parser =
          new DOMParser();

        const document =
          parser.parseFromString(
            files[check.file] || "",
            "text/html"
          );

        const element =
          document.querySelector(
            check.selector
          );

        passed =
          element?.textContent?.trim() ===
          check.expected;
      }

      if (
        check.type === "html_class"
      ) {
        const parser =
          new DOMParser();

        const document =
          parser.parseFromString(
            files[check.file] || "",
            "text/html"
          );

        const element =
          document.querySelector(
            check.selector
          );

        passed =
          Boolean(
            element?.classList.contains(
              check.className
            )
          );
      }

      if (
        check.type === "css_property"
      ) {
        const actual =
          getCssProperty(
            files[check.file] || "",
            check.selector,
            check.property
          );

        passed =
          actual?.toLowerCase() ===
          check.expected.toLowerCase();
      }

      return {
        ...check,
        passed
      };
    }
  );
};

function PracticalWorkspace({
  task,
  onExit
}) {
  const initialFiles =
    useMemo(() => {
      return Object.fromEntries(
        task.workspace.starterFiles.map(
          (file) => [
            file.path,
            file.content
          ]
        )
      );
    }, [task]);

  const editableFiles =
    task.workspace.starterFiles.filter(
      (file) => file.editable
    );

  const [files, setFiles] =
    useState(initialFiles);

  const [
    selectedPath,
    setSelectedPath
  ] = useState(
    editableFiles[0]?.path || ""
  );

  const [
    results,
    setResults
  ] = useState(null);

  const selectedFile =
    task.workspace.starterFiles.find(
      (file) =>
        file.path === selectedPath
    );

  const previewHtml =
    useMemo(() => {
      const html =
        files[
          task.workspace.entryFile
        ] || "";

      const css =
        files["style.css"] || "";

      const htmlWithoutLocalCss =
        html.replace(
          /<link[^>]*href=["']style\.css["'][^>]*>/i,
          ""
        );

      const styleTag =
        `<style>${css}</style>`;

      if (
        /<\/head>/i.test(
          htmlWithoutLocalCss
        )
      ) {
        return htmlWithoutLocalCss.replace(
          /<\/head>/i,
          `${styleTag}</head>`
        );
      }

      return (
        styleTag +
        htmlWithoutLocalCss
      );
    }, [
      files,
      task.workspace.entryFile
    ]);

  const updateCurrentFile =
    (value) => {
      setFiles((current) => ({
        ...current,
        [selectedPath]: value
      }));

      setResults(null);
    };

  const submitTask = () => {
    setResults(
      evaluateTask(
        task,
        files
      )
    );
  };

  const resetTask = () => {
    setFiles(initialFiles);
    setResults(null);
    setSelectedPath(
      editableFiles[0]?.path || ""
    );
  };

  const passedCount =
    results
      ? results.filter(
          (item) => item.passed
        ).length
      : 0;

  return (
    <div
      style={{
        width: "94%",
        maxWidth: "1500px",
        margin: "0 auto 60px"
      }}
    >
      <h2>{task.title}</h2>

      <div
        style={{
          textAlign: "left",
          maxWidth: "1000px",
          margin: "0 auto 24px"
        }}
      >
        <h3>課題条件</h3>

        <ol>
          {task.instructions.map(
            (instruction) => (
              <li key={instruction}>
                {instruction}
              </li>
            )
          )}
        </ol>
      </div>

      <div
        style={{
          display: "grid",
          gridTemplateColumns:
            "220px minmax(0, 1fr) minmax(360px, 1fr)",
          gap: "14px",
          alignItems: "stretch"
        }}
      >
        <section
          style={{
            border:
              "1px solid #555",
            borderRadius: "10px",
            padding: "14px",
            textAlign: "left"
          }}
        >
          <h3>📁 ファイル</h3>

          {editableFiles.map(
            (file) => (
              <button
                key={file.path}
                onClick={() =>
                  setSelectedPath(
                    file.path
                  )
                }
                style={{
                  display: "block",
                  width: "100%",
                  marginBottom: "8px",
                  padding: "10px",
                  textAlign: "left",
                  border:
                    selectedPath ===
                    file.path
                      ? "2px solid white"
                      : "1px solid #666"
                }}
              >
                {file.path}
              </button>
            )
          )}
        </section>

        <section
          style={{
            minWidth: 0
          }}
        >
          <h3>
            ✏️ {selectedPath}
          </h3>

          <textarea
            value={
              files[selectedPath] || ""
            }
            onChange={(event) =>
              updateCurrentFile(
                event.target.value
              )
            }
            spellCheck="false"
            style={{
              width: "100%",
              minHeight: "560px",
              resize: "vertical",
              boxSizing:
                "border-box",
              padding: "16px",
              fontFamily:
                "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace",
              fontSize: "14px",
              lineHeight: 1.5,
              background: "#111318",
              color: "#f5f5f5",
              border:
                "1px solid #555",
              borderRadius: "10px"
            }}
            aria-label={
              selectedFile
                ? `${selectedFile.path} editor`
                : "editor"
            }
          />
        </section>

        <section>
          <h3>
            🌐 プレビュー
          </h3>

          <iframe
            title="実技プレビュー"
            srcDoc={previewHtml}
            sandbox="allow-scripts"
            style={{
              width: "100%",
              minHeight: "560px",
              background: "white",
              border:
                "1px solid #555",
              borderRadius: "10px"
            }}
          />
        </section>
      </div>

      <div
        style={{
          marginTop: "24px",
          display: "flex",
          gap: "12px",
          justifyContent:
            "center",
          flexWrap: "wrap"
        }}
      >
        <button
          onClick={submitTask}
        >
          ✅ 提出して採点
        </button>

        <button
          onClick={resetTask}
        >
          ↩️ 初期状態に戻す
        </button>

        <button
          onClick={onExit}
        >
          実技メニューへ戻る
        </button>
      </div>

      {results && (
        <section
          style={{
            maxWidth: "800px",
            margin: "30px auto 0",
            textAlign: "left",
            border:
              "1px solid #555",
            borderRadius: "10px",
            padding: "20px"
          }}
        >
          <h3>
            採点結果：
            {passedCount}
            /
            {results.length}
          </h3>

          {results.map(
            (result) => (
              <p key={result.id}>
                {result.passed
                  ? "✅"
                  : "❌"}{" "}
                {result.label}
              </p>
            )
          )}
        </section>
      )}
    </div>
  );
}

export default PracticalWorkspace;
