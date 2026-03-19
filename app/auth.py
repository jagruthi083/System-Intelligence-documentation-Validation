from fastapi import APIRouter, HTTPException
from app.models import LoginModel

router = APIRouter(prefix="/auth", tags=["Auth"])

fake_user = {
    "email": "test@example.com",
    "password": "password123"
}

@router.post("/login")
def login(data: LoginModel):
    if data.email == fake_user["email"] and data.password == fake_user["password"]:
        return {"access_token": "jwt_token", "role": "user"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
