import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav>

      <Link to="/">
        Dashboard
      </Link>

      <Link to="/projects">
        Projects
      </Link>

      <Link to="/tasks">
        Tasks
      </Link>

      <Link to="/integrations">
        Integrations
      </Link>

    </nav>
  );
}