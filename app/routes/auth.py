from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from app.services.auth_service import authenticate_user, create_access_token
from app.schemas.user import UserCreate, UserResponse
from app.database.db import get_db
from sqlalchemy.orm import Session

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login", response_model=UserResponse, tags=["Auth"])
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    """
    Authenticate user and return access token.
    """
    user = authenticate_user(db, request.username, request.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
