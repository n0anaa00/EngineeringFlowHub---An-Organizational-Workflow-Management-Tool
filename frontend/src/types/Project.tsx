export interface Project {
    id: number;

    name: string;

    description: string;

    status: "ACTIVE" | "ARCHIVED";

    created_at?: string;
}