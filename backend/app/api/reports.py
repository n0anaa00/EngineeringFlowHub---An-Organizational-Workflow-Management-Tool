from fastapi import APIRouter
router = APIRouter()

@router.get("/dashboard")
def dashboard():
    return {"projects":0,"open_tasks":0,"completed_tasks":0}
