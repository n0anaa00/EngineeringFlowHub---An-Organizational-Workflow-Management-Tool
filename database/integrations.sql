CREATE TABLE integrations (
    id SERIAL PRIMARY KEY,
    source_system VARCHAR(255),
    external_id VARCHAR(255),
    sync_status VARCHAR(50)
);