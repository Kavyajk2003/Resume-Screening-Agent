from backend.services.parser import extract_text
from backend.services.embedding import calculate_similarity
from backend.services.llm import generate_recommendation


def screen_resume(resume_path, jd_path):

    # Extract text
    resume_text = extract_text(resume_path)
    jd_text = extract_text(jd_path)

    # Calculate similarity
    score = calculate_similarity(
        resume_text,
        jd_text
    )

    # Generate AI recommendation
    recommendation = generate_recommendation(
        resume_text,
        jd_text,
        score
    )

    return {
        "resume_text": resume_text,
        "jd_text": jd_text,
        "score": score,
        "recommendation": recommendation
    }