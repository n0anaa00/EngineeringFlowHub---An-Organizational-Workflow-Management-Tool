from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.services.task_service import (
    TaskService
)

from app.schemas.task_schema import (
    TaskCreate
)

router = APIRouter()


@router.get("/")
def get_tasks(
    db: Session = Depends(get_db)
):

    return TaskService.get_all(db)


@router.post("/")
def create_task(
    payload: TaskCreate,
    db: Session = Depends(get_db)
):

    return TaskService.create(
        db,
        payload
    )