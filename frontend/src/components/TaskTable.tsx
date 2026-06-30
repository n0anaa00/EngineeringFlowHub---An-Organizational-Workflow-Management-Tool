import { Task } from "../types/Task";

interface Props {
  tasks: Task[];
}

export default function TaskTable(
  { tasks }: Props
) {
  return (
    <table>
      <thead>
        <tr>
          <th>Title</th>
          <th>Status</th>
          <th>Assignee</th>
        </tr>
      </thead>

      <tbody>
        {tasks.map(task => (
          <tr key={task.id}>
            <td>{task.title}</td>
            <td>{task.status}</td>
            <td>{task.assignee}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}