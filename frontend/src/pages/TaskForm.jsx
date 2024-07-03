import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { getTask, createTask, updateTask, deleteTask } from "../api/helper";

function TaskForm() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [completed, setCompleted] = useState(false);
  const params = useParams();
  const navigate = useNavigate();

  const handleClick = async () => {
    try {
      setCompleted(!completed);
    } catch (error) {
      console.error(error);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (!params.id) {
        const response = await createTask({ title, description });
        console.log(response);
      } else {
        const response = await updateTask(params.id, {
          title,
          description,
          completed,
        });
        console.log(response);
      }
      navigate("/tasks");
    } catch (error) {
      console.error(error);
    }

    e.target.reset();
  };

  useEffect(() => {
    if (params.id) {
      getTask(params.id)
        .then((res) => {
          setTitle(res.data.title);
          setDescription(res.data.description);
        })
        .catch((err) => console.error(err));
    }
  }, []);

  return (
    <div className="flex h-[calc(100vh-10rem)] items-center justify-center">
      <div>
        <form onSubmit={handleSubmit} className="bg-green-700 p-10">
          <h1 className="my-4 text-3xl font-bold">
            {params.id ? "Update Task" : "Create Task"}
          </h1>
          <input
            type="text"
            placeholder="title"
            className="mb-4 block w-full px-3 py-2 text-black"
            onChange={(e) => setTitle(e.target.value)}
            autoFocus
            value={title}
          />
          <textarea
            placeholder="description"
            rows={3}
            className="mb-4 block w-full px-3 py-2 text-black"
            onChange={(e) => setDescription(e.target.value)}
            value={description}
          ></textarea>
          {params.id && (
            <div className="p-2">
              <label htmlFor="completed" className="mr-2">
                Completed
              </label>
              <input
                type="checkbox"
                id="completed"
                checked={completed}
                onChange={handleClick}
              />
            </div>
          )}
          <button className="rounded bg-zinc-950 p-2 hover:bg-zinc-800">
            {params.id ? "Update Task" : "Create Task"}
          </button>
        </form>

        {params.id && (
          <button
            className="mt-5 rounded bg-red-500 px-4 py-2 font-bold text-white hover:bg-red-400"
            onClick={async () => {
              try {
                const response = await deleteTask(params.id);
                console.log(response);
                navigate("/tasks");
              } catch (error) {
                console.error(error);
              }
            }}
          >
            Delete
          </button>
        )}
      </div>
    </div>
  );
}

export default TaskForm;
