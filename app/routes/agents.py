from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.agent import AgentCreate, AgentResponse
from app.models.agent import Agent
from app.database.db import get_db

router = APIRouter()

@router.post("/agents", response_model=AgentResponse, tags=["Agents"])
async def create_agent(agent: AgentCreate, db: Session = Depends(get_db)):
    """
    Create a new AI agent.
    """
    db_agent = Agent(**agent.dict())
    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)
    return db_agent

@router.get("/agents/{agent_id}", response_model=AgentResponse, tags=["Agents"])
async def read_agent(agent_id: int, db: Session = Depends(get_db)):
    """
    Retrieve an AI agent by ID.
    """
    db_agent = db.query(Agent).filter(Agent.id == agent_id).first()
    if db_agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    return db_agent

