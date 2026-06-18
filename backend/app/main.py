
from fastapi import FastAPI
from app.api import projects, tasks, reports, integrations

app = FastAPI(title="Engineering Flow Hub")

app.include_router(projects.router, prefix="/api/projects", tags=["projects"])
app.include_router(tasks.router, prefix="/api/tasks", tags=["tasks"])
app.include_router(reports.router, prefix="/api/reports", tags=["reports"])
app.include_router(integrations.router, prefix="/api/integrations", tags=["integrations"])

@app.get("/")
def root():
    return {"status":"ok"}
