from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.database.base import Base


class Task(Base):

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)

    project_id = Column(
        Integer,
        ForeignKey("projects.id")
    )

    title = Column(String(255))

    description = Column(String(1000))

    status = Column(String(50))

    assignee = Column(String(255))