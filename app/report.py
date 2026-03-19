from fastapi import APIRouter
from app.database import db

router = APIRouter(prefix="/report", tags=["Report"])

@router.get("/{candidate_id}")
def generate_report(candidate_id: str):
    assessment = db["assessments"].get(candidate_id, {})

    answers = assessment.get("answers", [])

    correct = sum(1 for a in answers if a.get("result") == "correct")
    wrong = sum(1 for a in answers if a.get("result") == "wrong")
    skipped = sum(1 for a in answers if a.get("result") == "skipped")

    score = (correct * 1) - (wrong * 0.25)

    return {
        "candidate_id": candidate_id,
        "correct": correct,
        "wrong": wrong,
        "skipped": skipped,
        "final_score": round(score, 2)
    }
