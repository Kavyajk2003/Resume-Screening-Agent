from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
import shutil

from backend.services.parser import extract_text

router = APIRouter(
    prefix="/jd",
    tags=["Job Description"]
)

UPLOAD_DIR = Path("backend/uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/upload")
async def upload_job_description(file: UploadFile = File(...)):
    allowed_extensions = [".pdf", ".docx", ".txt"]

    extension = Path(file.filename).suffix.lower()

    if extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, DOCX and TXT files are allowed."
        )

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    if extension == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = extract_text(str(file_path))

    return {
        "message": "Job Description uploaded successfully",
        "filename": file.filename,
        "characters": len(text),
        "preview": text[:1000]
    }