from sqlalchemy.orm import Session

from app.models.project import Project


class ProjectService:

    @staticmethod
    def get_all(db: Session):

        return db.query(Project).all()

    @staticmethod
    def create(
        db: Session,
        data
    ):

        project = Project(
            name=data.name,
            description=data.description,
            status="ACTIVE"
        )

        db.add(project)

        db.commit()

        db.refresh(project)

        return project