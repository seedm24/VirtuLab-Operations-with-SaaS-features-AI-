from sqlalchemy import Column, Integer, String
from app.database.db import Base

class SEO(Base):
    __tablename__ = 'seo_entries'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    keywords = Column(String)

