from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.project_schema import (
    ProjectCreate
)

from app.services.project_service import (
    ProjectService
)

router = APIRouter()


@router.get("/")
def get_projects(
    db: Session = Depends(get_db)
):

    return ProjectService.get_all(db)


@router.post("/")
def create_project(
    payload: ProjectCreate,
    db: Session = Depends(get_db)
):

    return ProjectService.create(
        db,
        payload
    )