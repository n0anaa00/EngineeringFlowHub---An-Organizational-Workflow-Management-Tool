from sqlalchemy.orm import Session

from app.models.task import Task


class TaskService:

    @staticmethod
    def get_all(db):

        return db.query(Task).all()

    @staticmethod
    def create(db, data):

        task = Task(
            project_id=data.project_id,
            title=data.title,
            description=data.description,
            assignee=data.assignee,
            status="OPEN"
        )

        db.add(task)

        db.commit()

        db.refresh(task)

        return task