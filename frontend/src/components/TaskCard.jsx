import { useNavigate } from "react-router-dom";

function TaskCard({ task }) {
  const navigate = useNavigate();
  return (
    <div
      className="overflow-auto bg-gray-300 p-4 hover:cursor-pointer hover:bg-blue-300"
      onClick={() => {
        navigate(`/tasks/${task._id}`);
      }}
    >
      <div className="flex justify-between">
        <h2 className="text-2xl font-bold text-slate-900">{task.title}</h2>
        <button>{task.completed == true ? "✔" : "❌"}</button>
      </div>
      <p className="font-bold text-slate-900">{task.description}</p>
      <p className="text-slate-900">Completed: {String(task.completed)}</p>
      <p className="text-slate-900">Task ID: {task._id}</p>
    </div>
  );
}

export default TaskCard;
