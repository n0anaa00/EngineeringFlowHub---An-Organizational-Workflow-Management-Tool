from fastapi import APIRouter

from app.services.integration_service import (
    IntegrationService
)

router = APIRouter()


@router.post("/jira/sync")
def sync_jira():

     return IntegrationService.sync_jira()

