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

const evaluateHtmlText = (
  check,
  files
) => {
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

  return (
    element?.textContent?.trim() ===
    check.expected
  );
};

const evaluateHtmlAttribute = (
  check,
  files
) => {
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

  return (
    element?.getAttribute(
      check.attribute
    ) === check.expected
  );
};

const evaluateHtmlClass = (
  check,
  files
) => {
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

  return Boolean(
    element?.classList.contains(
      check.className
    )
  );
};

const evaluateCssProperty = (
  check,
  files
) => {
  const actual =
    getCssProperty(
      files[check.file] || "",
      check.selector,
      check.property
    );

  return (
    actual?.toLowerCase() ===
    check.expected.toLowerCase()
  );
};

const CHECK_EVALUATORS = {
  html_text: evaluateHtmlText,
  html_attribute:
    evaluateHtmlAttribute,
  html_class: evaluateHtmlClass,
  css_property: evaluateCssProperty
};

export const evaluateCheck = (
  check,
  files
) => {
  const evaluator =
    CHECK_EVALUATORS[check.type];

  if (!evaluator) {
    return {
      ...check,
      passed: false,
      error:
        `Unsupported check type: ${check.type}`
    };
  }

  return {
    ...check,
    passed: evaluator(
      check,
      files
    )
  };
};

export const evaluateTask = (
  task,
  files
) => {
  return task.evaluation.checks.map(
    (check) =>
      evaluateCheck(
        check,
        files
      )
  );
};
