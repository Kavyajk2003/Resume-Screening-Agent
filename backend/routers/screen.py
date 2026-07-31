from fastapi import APIRouter, UploadFile, File, Form
from pathlib import Path
import shutil

from backend.services.parser import extract_text
from backend.services.embedding import calculate_similarity
from backend.services.llm import generate_recommendation

router = APIRouter(
    prefix="/screen",
    tags=["AI Resume Screening"]
)

UPLOAD_DIR = Path("backend/uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/")
async def screen_candidates(

    job_description: str = Form(...),

    resumes: list[UploadFile] = File(...)

):

    results = []

    for resume in resumes:

        resume_path = UPLOAD_DIR / resume.filename

        with open(resume_path, "wb") as buffer:
            shutil.copyfileobj(resume.file, buffer)

        resume_text = extract_text(str(resume_path))

        score = calculate_similarity(
            resume_text,
            job_description
        )

        recommendation = generate_recommendation(
            resume_text,
            job_description,
            score
        )

        results.append({

            "candidate": resume.filename,

            "score": score,

            "recommendation": recommendation

        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    for index, candidate in enumerate(results):

        candidate["rank"] = index + 1

    return {

        "total_candidates": len(results),

        "results": results

    }