from fastapi import FastAPI
from backend.config import UPLOAD_DIR, OUTPUT_DIR
from backend.routers import resume, jd, match, screen
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Resume Screening Agent",
    description="AI Powered Resume Screening System",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://resume-screening-agent-ui.onrender.com/"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume.router)
app.include_router(jd.router)
app.include_router(match.router)
app.include_router(screen.router)

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