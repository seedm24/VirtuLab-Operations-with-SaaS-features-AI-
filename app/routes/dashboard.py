from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.dashboard_service import get_dashboard_data
from app.schemas.dashboard import DashboardResponse
from app.database.db import get_db

router = APIRouter()

@router.get("/dashboard", response_model=DashboardResponse, tags=["Dashboard"])
async def read_dashboard_data(db: Session = Depends(get_db)):
    """
    Retrieve dashboard analytics data.
    """
    data = get_dashboard_data(db)
    return data
