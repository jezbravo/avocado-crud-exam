import { useEffect, useState } from "react";
import TaskList from "../components/TaskList";
import { getAllTasks } from "../api/helper";

function HomePage() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    getAllTasks()
      .then((res) => {
        setTasks(res.data);
      })
      .catch((err) => console.error(err));
  }, []);
  return <TaskList tasks={tasks} />;
}

export default HomePage;
