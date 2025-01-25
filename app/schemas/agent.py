from pydantic import BaseModel

class AgentBase(BaseModel):
    name: str
    description: str

class AgentCreate(AgentBase):
    pass

class AgentResponse(AgentBase):
    id: int

    class Config:
        orm_mode = True

