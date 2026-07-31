from fastapi import FastAPI

app = FastAPI(
    title="Resume Screening Agent",
    description="AI Powered Resume Screening System",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Resume Screening Agent 🚀",
        "status": "Backend Running Successfully"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }