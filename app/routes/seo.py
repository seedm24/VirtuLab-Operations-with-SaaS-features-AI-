from fastapi import APIRouter
from app.schemas.seo import SEOAnalysisRequest, SEOAnalysisResponse
from app.services.seo_service import analyze_seo

router = APIRouter()

@router.post("/seo/analyze", response_model=SEOAnalysisResponse)
async def analyze_website_seo(request: SEOAnalysisRequest):
    return analyze_seo(request.url)

