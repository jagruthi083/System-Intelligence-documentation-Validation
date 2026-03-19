from fastapi import APIRouter

router = APIRouter(prefix="/scoring", tags=["Scoring"])

@router.post("/calculate")
def calculate_score(data: dict):
    correct = data.get("correct", 0)
    wrong = data.get("wrong", 0)
    skipped = data.get("skipped", 0)

    score = (correct * 1) - (wrong * 0.25)

    return {
        "correct": correct,
        "wrong": wrong,
        "skipped": skipped,
        "final_score": round(score, 2)
    }
