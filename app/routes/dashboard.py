from fastapi import APIRouter
from app.services.dashboard_service import get_dashboard_data

router = APIRouter()

@router.get("/dashboard/")
async def fetch_dashboard_data():
    return get_dashboard_data()

