import {
  useEffect,
  useMemo,
  useState
} from "react";

import PracticalWorkspace from "../../components/practical/PracticalWorkspace";
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

const formatTime = (
  totalSeconds
) => {
  const minutes =
    Math.floor(
      totalSeconds / 60
    );

  const seconds =
    totalSeconds % 60;

  return (
    `${minutes}:` +
    `${seconds}`.padStart(
      2,
      "0"
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

  useEffect(() => {
    if (
      remainingSeconds <= 0
    ) {
      return undefined;
    }

    const timer =
      window.setInterval(
        () => {
          setRemainingSeconds(
            (current) =>
              Math.max(
                0,
                current - 1
              )
          );
        },
        1000
      );

    return () =>
      window.clearInterval(
        timer
      );
  }, [remainingSeconds]);

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
          {formatTime(
            remainingSeconds
          )}
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
              marginBottom: "24px"
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
      </div>

      <PracticalWorkspace
        key={task.id}
        task={task}
        files={currentFiles}
        onFilesChange={
          updateCurrentFiles
        }
        onExit={onExit}
      />
    </div>
  );
}

export default WebDesignPractical;
