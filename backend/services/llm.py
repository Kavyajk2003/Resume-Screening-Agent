import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_recommendation(resume, job_description, score):

    prompt = f"""
You are an ATS Resume Screening AI.

Resume:
{resume}

Job Description:
{job_description}

Current Match Score:
{score}%

Provide:

1. Strengths
2. Missing Skills
3. Recommendation
4. Final Decision (Shortlist / Reject)

Return only plain text.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content