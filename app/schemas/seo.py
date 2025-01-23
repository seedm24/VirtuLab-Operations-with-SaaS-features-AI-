from pydantic import BaseModel

class SEOAnalysisRequest(BaseModel):
    url: str

class SEOAnalysisResponse(BaseModel):
    url: str
    score: int
    top_keywords: list[str]
    recommendations: list[str]

