from pydantic import BaseModel

class SubscriptionBase(BaseModel):
    plan: str
    status: str

class SubscriptionCreate(SubscriptionBase):
    user_id: int

class SubscriptionResponse(SubscriptionBase):
    id: int

    class Config:
        orm_mode = True
