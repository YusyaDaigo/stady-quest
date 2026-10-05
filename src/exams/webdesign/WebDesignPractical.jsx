import PracticalWorkspace from "../../components/practical/PracticalWorkspace";
import { webDesignPracticalTasks } from "./practical/tasks";

function WebDesignPractical({
  onExit
}) {
  const task =
    webDesignPracticalTasks[0];

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

  return (
    <PracticalWorkspace
      task={task}
      onExit={onExit}
    />
  );
}

export default WebDesignPractical;
