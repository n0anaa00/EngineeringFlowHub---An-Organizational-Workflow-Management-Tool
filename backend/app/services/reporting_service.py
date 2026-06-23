from sqlalchemy import func

from app.models.project import Project
from app.models.task import Task


class ReportingService:

    @staticmethod
    def dashboard(db):

        projects = db.query(Project).count()

        open_tasks = (
            db.query(Task)
            .filter(Task.status == "OPEN")
            .count()
        )

        completed_tasks = (
            db.query(Task)
            .filter(Task.status == "DONE")
            .count()
        )

        return {

            "projects": projects,

            "open_tasks": open_tasks,

            "completed_tasks": completed_tasks
        }