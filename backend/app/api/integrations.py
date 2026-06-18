from fastapi import APIRouter
router = APIRouter()

@router.post("/jira/sync")
def sync():
    return [{"external_id":"JIRA-1001","title":"Review CAD drawings"}]