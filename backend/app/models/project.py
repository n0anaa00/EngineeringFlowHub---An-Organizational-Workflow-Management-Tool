from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from app.database.base import Base


class Project(Base):

    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)

    name = Column(String(255))

    description = Column(String(1000))

    status = Column(String(50))

    created_at = Column(
        DateTime,
        default=datetime.now(datetime.timezone.utc)
    )