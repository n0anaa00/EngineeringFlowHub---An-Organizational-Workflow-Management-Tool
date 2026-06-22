from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database.base import Base


class Integration(Base):

    __tablename__ = "integrations"

    id = Column(Integer, primary_key=True)

    source_system = Column(String(255))

    external_id = Column(String(255))

    sync_status = Column(String(50))