from fastapi import APIRouter

router = APIRouter(prefix="/evaluation", tags=["Evaluation"])

@router.post("/evaluate")
def evaluate(data: dict):
    answer = data.get("answer", "").lower()

    if answer.strip() == "":
        result = "skipped"
    elif "correct" in answer:
        result = "correct"
    else:
        result = "wrong"

    return {
        "question_id": data.get("question_id"),
        "result": result
    }
