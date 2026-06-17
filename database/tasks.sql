CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    project_id INTEGER,
    title VARCHAR(255),
    status VARCHAR(50),
    assignee VARCHAR(255),
    created_at TIMESTAMP
);