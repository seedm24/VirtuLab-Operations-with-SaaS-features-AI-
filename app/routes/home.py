from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["Home"])
async def read_root():
    """
    Root endpoint returning a welcome message.
    """
    return {"message": "Welcome to the SaaS and AI Platform API"}

