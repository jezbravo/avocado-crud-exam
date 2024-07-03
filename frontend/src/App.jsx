import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import TaskForm from "./pages/TaskForm";
import NavBar from "./components/NavBar";

function App() {
  return (
    <BrowserRouter>
      <main className="container mx-auto px-10">
        <NavBar />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/tasks" element={<HomePage />} />
          <Route path="/tasks/new" element={<TaskForm />} />
          <Route path="/tasks/:id" element={<TaskForm />} />
        </Routes>
      </main>
    </BrowserRouter>
  );
}

export default App;
