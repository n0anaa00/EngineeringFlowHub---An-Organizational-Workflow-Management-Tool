import { Project } from "../types/Project";

interface Props {
  projects: Project[];
}

export default function ProjectTable(
  { projects }: Props
) {
  return (
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Status</th>
        </tr>
      </thead>

      <tbody>
        {projects.map(project => (
          <tr key={project.id}>
            <td>{project.name}</td>
            <td>{project.status}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}