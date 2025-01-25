from sqlalchemy.orm import Session
from app.models.seo import SEO
from app.schemas.seo import SEOCreate

def create_seo_entry(db: Session, seo: SEOCreate):
    db_seo = SEO(**seo.dict())
    db.add(db_seo)
    db.commit()
    db.refresh(db_seo)
    return db_seo

def get_seo_entry(db: Session, seo_id: int):
    return db.query(SEO).filter(SEO.id == seo_id).first()
