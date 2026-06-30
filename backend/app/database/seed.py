from sqlalchemy.orm import Session

from app.models.project import Project

def seed(db: Session):

    project = Project(
        name="Engineering Upgrade",
        description="Demo Project",
        status="ACTIVE"
    )

    db.add(project)

    db.commit()