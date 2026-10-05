import {
  useCallback,
  useEffect,
  useMemo,
  useState
} from "react";

import PracticalWorkspace from "../../components/practical/PracticalWorkspace";
import {
  evaluateTask
} from "../../components/practical/validators";
import { webDesignPracticalTasks } from "./practical/tasks";

const PRACTICAL_MODES = {
  practice: {
    label: "練習モード",
    taskCount: 1,
    timeLimit: 12 * 60
  },

  mock: {
    label: "模試モード",
    taskCount: 5,
    timeLimit: 60 * 60
  }
};

const createInitialFiles = (task) => {
  return Object.fromEntries(
    task.workspace.starterFiles.map(
      (file) => [
        file.path,
        file.content
      ]
    )
  );
};

const createInitialTaskFiles = (
  tasks
) => {
  return Object.fromEntries(
    tasks.map(
      (task) => [
        task.id,
        createInitialFiles(task)
      ]
    )
  );
};

function WebDesignPractical({
  mode,
  onExit
}) {
  const modeConfig =
    PRACTICAL_MODES[mode];

  const sessionTasks =
    useMemo(() => {
      if (!modeConfig) {
        return [];
      }

      return webDesignPracticalTasks.slice(
        0,
        modeConfig.taskCount
      );
    }, [modeConfig]);

  const [
    currentTaskIndex,
    setCurrentTaskIndex
  ] = useState(0);

  const [
    taskFiles,
    setTaskFiles
  ] = useState(() =>
    createInitialTaskFiles(
      sessionTasks
    )
  );

  const [
    remainingSeconds,
    setRemainingSeconds
  ] = useState(
    modeConfig?.timeLimit ?? 0
  );

  const [
    examResult,
    setExamResult
  ] = useState(null);

  const submitExam =
    useCallback(
      (reason = "manual") => {
        const taskResults =
          sessionTasks.map(
            (task) => {
              const files =
                taskFiles[
                  task.id
                ] ||
                createInitialFiles(
                  task
                );

              const checks =
                evaluateTask(
                  task,
                  files
                );

              const passed =
                checks.filter(
                  (check) =>
                    check.passed
                ).length;

              return {
                taskId:
                  task.id,
                title:
                  task.title,
                passed,
                total:
                  checks.length,
                checks
              };
            }
          );

        const passed =
          taskResults.reduce(
            (sum, result) =>
              sum +
              result.passed,
            0
          );

        const total =
          taskResults.reduce(
            (sum, result) =>
              sum +
              result.total,
            0
          );

        setExamResult({
          reason,
          passed,
          total,
          taskResults
        });
      },
      [
        sessionTasks,
        taskFiles
      ]
    );

  useEffect(() => {
    if (
      remainingSeconds <= 0 ||
      examResult
    ) {
      return undefined;
    }

    const timer =
      window.setTimeout(
        () => {
          if (
            remainingSeconds <= 1
          ) {
            setRemainingSeconds(
              0
            );

            if (
              mode === "mock"
            ) {
              submitExam(
                "time_limit"
              );
            }

            return;
          }

          setRemainingSeconds(
            remainingSeconds - 1
          );
        },
        1000
      );

    return () =>
      window.clearTimeout(
        timer
      );
  }, [
    mode,
    remainingSeconds,
    examResult,
    submitExam
  ]);

  if (!modeConfig) {
    return (
      <div>
        <h2>実技試験</h2>

        <p>
          不明な実技モードです。
        </p>

        <button onClick={onExit}>
          戻る
        </button>
      </div>
    );
  }

  if (
    mode === "mock" &&
    webDesignPracticalTasks.length <
      modeConfig.taskCount
  ) {
    return (
      <div>
        <h2>
          ウェブデザイン技能検定
          3級 実技
        </h2>

        <h3>
          模試モード
        </h3>

        <p>
          模試には5課題が必要です。
        </p>

        <p>
          現在：
          {
            webDesignPracticalTasks.length
          }
          /5課題
        </p>

        <button onClick={onExit}>
          実技メニューへ戻る
        </button>
      </div>
    );
  }

  if (
    mode === "mock" &&
    examResult
  ) {
    const percentage =
      examResult.total > 0
        ? Math.round(
            (
              examResult.passed /
              examResult.total
            ) * 100
          )
        : 0;

    return (
      <div
        style={{
          width: "92%",
          maxWidth: "1000px",
          margin: "0 auto 60px"
        }}
      >
        <h2>
          ウェブデザイン技能検定
          3級 実技 模試
        </h2>

        <h2>結果発表</h2>

        {examResult.reason ===
          "time_limit" && (
          <p>
            ⏰ 時間切れのため
            自動提出されました。
          </p>
        )}

        <h3>
          総合採点：
          {" "}
          {examResult.passed}
          /
          {examResult.total}
        </h3>

        <p>
          達成率：
          {" "}
          {percentage}
          %
        </p>

        <div
          style={{
            display: "grid",
            gap: "16px",
            marginTop: "30px"
          }}
        >
          {examResult.taskResults.map(
            (
              taskResult,
              index
            ) => (
              <section
                key={
                  taskResult.taskId
                }
                style={{
                  textAlign: "left",
                  border:
                    "1px solid #555",
                  borderRadius:
                    "10px",
                  padding: "20px"
                }}
              >
                <h3>
                  課題
                  {" "}
                  {index + 1}
                  ：
                  {" "}
                  {
                    taskResult.passed
                  }
                  /
                  {
                    taskResult.total
                  }
                </h3>

                <p>
                  {
                    taskResult.title
                  }
                </p>

                {taskResult.checks.map(
                  (check) => (
                    <p
                      key={
                        check.id
                      }
                    >
                      {check.passed
                        ? "✅"
                        : "❌"}{" "}
                      {check.label}
                    </p>
                  )
                )}
              </section>
            )
          )}
        </div>

        <div
          style={{
            marginTop: "30px"
          }}
        >
          <button
            onClick={onExit}
          >
            実技メニューへ戻る
          </button>
        </div>
      </div>
    );
  }

  const task =
    sessionTasks[
      currentTaskIndex
    ];

  if (!task) {
    return (
      <div>
        <h2>実技試験</h2>

        <p>
          実技課題がありません。
        </p>

        <button onClick={onExit}>
          戻る
        </button>
      </div>
    );
  }

  const currentFiles =
    taskFiles[task.id] ||
    createInitialFiles(task);

  const updateCurrentFiles =
    (nextFiles) => {
      setTaskFiles(
        (current) => ({
          ...current,
          [task.id]:
            nextFiles
        })
      );
    };

  return (
    <div>
      <div
        style={{
          width: "94%",
          maxWidth: "1500px",
          margin: "0 auto 24px"
        }}
      >
        <h2>
          ウェブデザイン技能検定
          3級 実技
        </h2>

        <h3>
          {modeConfig.label}
        </h3>

        <p>
          残り時間：
          {" "}
          {remainingSeconds}
          秒
        </p>

        <p>
          課題
          {" "}
          {currentTaskIndex + 1}
          /
          {sessionTasks.length}
        </p>

        {sessionTasks.length >
          1 && (
          <div
            style={{
              display: "flex",
              justifyContent:
                "center",
              gap: "10px",
              flexWrap: "wrap",
              marginBottom: "18px"
            }}
          >
            {sessionTasks.map(
              (item, index) => (
                <button
                  key={item.id}
                  onClick={() =>
                    setCurrentTaskIndex(
                      index
                    )
                  }
                  style={{
                    padding:
                      "10px 18px",
                    border:
                      index ===
                      currentTaskIndex
                        ? "2px solid white"
                        : "1px solid #666"
                  }}
                >
                  課題
                  {" "}
                  {index + 1}
                </button>
              )
            )}
          </div>
        )}

        {mode === "mock" && (
          <button
            onClick={() =>
              submitExam(
                "manual"
              )
            }
            style={{
              padding:
                "12px 24px",
              marginBottom: "20px"
            }}
          >
            📤 試験全体を提出
          </button>
        )}
      </div>

      <PracticalWorkspace
        key={task.id}
        task={task}
        files={currentFiles}
        onFilesChange={
          updateCurrentFiles
        }
        onExit={onExit}
        showTaskScoring={
          mode === "practice"
        }
      />
    </div>
  );
}

export default WebDesignPractical;
