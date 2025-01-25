from pydantic import BaseModel

class SEOBase(BaseModel):
    title: str
    description: str
    keywords: str

class SEOCreate(SEOBase):
    pass

class SEOResponse(SEOBase):
    id: int

    class Config:
        orm_mode = True
