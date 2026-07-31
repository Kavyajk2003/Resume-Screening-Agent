from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.embedding import calculate_similarity
from backend.services.llm import generate_recommendation

router = APIRouter(
    prefix="/match",
    tags=["Matching"]
)


class MatchRequest(BaseModel):
    resume: str
    job_description: str


@router.post("/")
def match_resume(request: MatchRequest):

    score = calculate_similarity(
        request.resume,
        request.job_description
    )

    recommendation = generate_recommendation(
        request.resume,
        request.job_description,
        score
    )

    return {
        "match_score": score,
        "recommendation": recommendation
    }