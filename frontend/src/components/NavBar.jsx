import { Link } from "react-router-dom";

function NavBar() {
  return (
    <header className="my-7 flex items-center justify-between">
      <Link to={"/"}>
        <h1 className="text-3xl font-bold hover:text-red-500">
          Python + React JS CRUD
        </h1>
      </Link>
      <Link
        to={"/tasks/new"}
        className="rounded bg-green-700 p-2 hover:bg-green-500"
      >
        Create Task
      </Link>
    </header>
  );
}

export default NavBar;
