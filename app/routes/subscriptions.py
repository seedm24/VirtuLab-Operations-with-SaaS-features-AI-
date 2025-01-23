
from fastapi import APIRouter, HTTPException
from app.schemas.subscription import SubscriptionRequest, SubscriptionResponse
from app.services.subscription_service import create_subscription, list_subscriptions

router = APIRouter()

@router.post("/subscriptions/", response_model=SubscriptionResponse)
async def create_new_subscription(subscription: SubscriptionRequest):
    return create_subscription(subscription)

@router.get("/subscriptions/", response_model=list[SubscriptionResponse])
async def get_all_subscriptions():
    return list_subscriptions()
