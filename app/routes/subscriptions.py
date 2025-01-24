from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.subscription import SubscriptionCreate, SubscriptionResponse
from app.models.subscription import Subscription
from app.database.db import get_db

router = APIRouter()

@router.post("/subscriptions", response_model=SubscriptionResponse, tags=["Subscriptions"])
async def create_subscription(subscription: SubscriptionCreate, db: Session = Depends(get_db)):
    """
    Create a new subscription.
    """
    db_subscription = Subscription(**subscription.dict())
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription

@router.get("/subscriptions/{subscription_id}", response_model=SubscriptionResponse, tags=["Subscriptions"])
async def read_subscription(subscription_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a subscription by ID.
    """
    db_subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
    if db_subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return db_subscription
