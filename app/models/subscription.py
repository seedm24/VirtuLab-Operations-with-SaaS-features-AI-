from sqlalchemy import Column, Integer, String, Boolean
from app.database.db import Base

class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    price = Column(Integer)
    features = Column(String)  # JSON string listing available features
    is_active = Column(Boolean, default=True)

