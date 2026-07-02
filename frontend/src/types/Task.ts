export interface Task {
    id: number;

    project_id: number;

    title: string;

    description: string;

    status: "OPEN" | "IN_PROGRESS" | "DONE";

    assignee: string;

    created_at?: string;
}