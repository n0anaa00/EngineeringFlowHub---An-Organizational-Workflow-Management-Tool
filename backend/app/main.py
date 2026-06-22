
from app.database.connection import engine
from app.database.base import Base

from app.models.project import Project
from app.models.task import Task
from app.models.integration import Integration

Base.metadata.create_all(bind=engine)