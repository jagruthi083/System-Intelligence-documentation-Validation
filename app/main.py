from fastapi import FastAPI
from app import auth, assessment, evaluation, scoring, monitoring, report

app = FastAPI(title="System Intelligence & Validation Platform")

app.include_router(auth.router)
app.include_router(assessment.router)
app.include_router(evaluation.router)
app.include_router(scoring.router)
app.include_router(monitoring.router)
app.include_router(report.router)

@app.get("/")
def home():
    return {"message": "System Running Successfully"}
