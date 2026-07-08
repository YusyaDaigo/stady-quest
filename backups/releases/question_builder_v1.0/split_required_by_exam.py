from pathlib import Path
import re

BASE = Path("src/exams/pharmacy/questions")
SOURCE = BASE / "required.js"
MARKER = "  // AI_QUESTION_INSERT_HERE"

text = SOURCE.read_text(encoding="utf-8")
lines = text.splitlines()

blocks = []
current = []
inside = False
depth = 0

for line in lines:
    if line.strip() == "{":
        inside = True
        current = [line]
        depth = 1
        continue

    if inside:
        current.append(line)
        depth += line.count("{")
        depth -= line.count("}")

        if depth == 0:
            block = "\n".join(current)
            blocks.append(block)
            inside = False

by_exam = {}

for block in blocks:
    m = re.search(r"examNumber:\s*(\d+)", block)
    if not m:
        continue

    exam_number = int(m.group(1))
    by_exam.setdefault(exam_number, []).append(block)

for exam_number, exam_blocks in sorted(by_exam.items(), reverse=True):
    export_name = f"required{exam_number}Questions"
    out = BASE / f"required_{exam_number}.js"

    body = ",\n\n".join(exam_blocks)

    out.write_text(
        f'''import {{ CATEGORIES }} from "./categories";

export const {export_name} = [

{body},

{MARKER}
];
''',
        encoding="utf-8",
    )

imports = []
spreads = []

for exam_number in sorted(by_exam.keys(), reverse=True):
    export_name = f"required{exam_number}Questions"
    imports.append(
        f'import {{ {export_name} }} from "./required_{exam_number}";'
    )
    spreads.append(f"  ...{export_name},")

SOURCE.write_text(
    "\n".join(imports)
    + "\n\nexport const requiredQuestions = [\n"
    + "\n".join(spreads)
    + "\n];\n",
    encoding="utf-8",
)

print("✅ required.js を年度別に分割しました")
for exam_number in sorted(by_exam.keys(), reverse=True):
    print(f"第{exam_number}回: {len(by_exam[exam_number])}問")
