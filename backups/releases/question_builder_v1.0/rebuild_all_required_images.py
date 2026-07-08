import subprocess
import sys


EXAMS = list(range(97, 112))


def run_command(command):
    print("================================")
    print("🚀", " ".join(command))
    print("================================")

    result = subprocess.run(command)

    if result.returncode != 0:
        print("⚠️ 失敗しましたが、次へ進みます:")
        print(" ".join(command))
        return False

    return True


def main():
    failed_exams = []

    for exam in EXAMS:
        ok = run_command([
            sys.executable,
            "tools/question_builder/import_exam.py",
            "--exam",
            str(exam),
            "--skip-build",
        ])

        if not ok:
            failed_exams.append(exam)

    print("================================")
    print("🏗️ npm run build")
    print("================================")

    build_ok = run_command(["npm", "run", "build"])

    print("================================")

    if failed_exams:
        print("⚠️ 画像再生成に失敗した年度:")
        print(failed_exams)
        print("APIクォータ回復後に以下を再実行してください:")
        for exam in failed_exams:
            print(
                f"python tools/question_builder/import_exam.py --exam {exam} --skip-build"
            )
    else:
        print("✅ 全年度の画像再生成完了")

    if build_ok:
        print("✅ build成功")

    print("================================")


if __name__ == "__main__":
    main()