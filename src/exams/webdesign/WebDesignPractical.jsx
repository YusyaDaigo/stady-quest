import {
  useState
} from "react";

import PracticalWorkspace from "../../components/practical/PracticalWorkspace";
import { webDesignPracticalTasks } from "./practical/tasks";

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

const createInitialTaskFiles = () => {
  return Object.fromEntries(
    webDesignPracticalTasks.map(
      (task) => [
        task.id,
        createInitialFiles(task)
      ]
    )
  );
};

function WebDesignPractical({
  onExit
}) {
  const [
    currentTaskIndex,
    setCurrentTaskIndex
  ] = useState(0);

  const [
    taskFiles,
    setTaskFiles
  ] = useState(
    createInitialTaskFiles
  );

  const task =
    webDesignPracticalTasks[
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

        <p>
          課題{" "}
          {currentTaskIndex + 1}
          /
          {
            webDesignPracticalTasks.length
          }
        </p>

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
          {webDesignPracticalTasks.map(
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
                課題 {index + 1}
              </button>
            )
          )}
        </div>
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
