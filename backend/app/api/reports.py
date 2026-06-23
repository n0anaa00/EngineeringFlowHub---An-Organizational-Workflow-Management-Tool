from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.services.reporting_service import (
    ReportingService
)

router = APIRouter()


@router.get("/dashboard")
def dashboard(
    db: Session = Depends(get_db)
):

    return ReportingService.dashboard(db)