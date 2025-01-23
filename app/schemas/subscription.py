from pydantic import BaseModel

class SubscriptionRequest(BaseModel):
    name: str
    price: int
    features: list[str]

class SubscriptionResponse(BaseModel):
    id: int
    name: str
    price: int
    features: list[str]
    is_active: bool

