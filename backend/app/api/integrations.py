from fastapi import APIRouter

router = APIRouter()


@router.post("/jira/sync")
def sync_jira():

    return []