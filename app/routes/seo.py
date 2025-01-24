from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.seo import SEOCreate, SEOResponse
from app.models.seo import SEO
from app.database.db import get_db

router = APIRouter()

@router.post("/seo", response_model=SEOResponse, tags=["SEO"])
async def create_seo_entry(seo: SEOCreate, db: Session = Depends(get_db)):
    """
    Create a new SEO entry.
    """
    db_seo = SEO(**seo.dict())
    db.add(db_seo)
    db.commit()
    db.refresh(db_seo)
    return db_seo

@router.get("/seo/{seo_id}", response_model=SEOResponse, tags=["SEO"])
async def read_seo_entry(seo_id: int, db: Session = Depends(get_db)):
    """
    Retrieve an SEO entry by ID.
    """
    db_seo = db.query(SEO).filter(SEO.id == seo_id).first()
    if db_seo is None:
        raise HTTPException(status_code=404, detail="SEO entry not found")
    return db_seo
