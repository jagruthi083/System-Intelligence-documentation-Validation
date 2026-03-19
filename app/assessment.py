from fastapi import APIRouter
from app.database import db

router = APIRouter(prefix="/assessment", tags=["Assessment"])

@router.post("/start")
def start_assessment(data: dict):
    candidate_id = data.get("candidate_id")
    db["assessments"][candidate_id] = {"answers": []}
    return {"message": "Assessment started"}

@router.post("/submit")
def submit_answer(data: dict):
    candidate_id = data.get("candidate_id")
    db["assessments"][candidate_id]["answers"].append(data)
    return {"message": "Answer submitted"}
