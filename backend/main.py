from fastapi import FastAPI
from backend.config import UPLOAD_DIR, OUTPUT_DIR
from backend.routers import resume

app = FastAPI(
    title="Resume Screening Agent",
    description="AI Powered Resume Screening System",
    version="1.0.0",
)

app.include_router(resume.router)

@app.get("/")
def home():
    return {
        "message": "Welcome to Resume Screening Agent 🚀",
        "status": "Backend Running Successfully",
        "upload_directory": str(UPLOAD_DIR),
        "output_directory": str(OUTPUT_DIR),
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }