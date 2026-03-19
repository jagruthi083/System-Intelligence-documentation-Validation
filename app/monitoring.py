from fastapi import APIRouter
from app.database import db

router = APIRouter(prefix="/monitor", tags=["Monitoring"])

@router.post("/log")
def log_activity(data: dict):
    db["logs"].append(data)
    return {"message": "Activity logged"}
