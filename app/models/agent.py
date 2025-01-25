from sqlalchemy import Column, Integer, String
from app.database.db import Base

class Agent(Base):
    __tablename__ = 'agents'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

