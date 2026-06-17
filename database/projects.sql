CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    status VARCHAR(50),
    created_at TIMESTAMP
);