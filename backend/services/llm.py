import os
from groq import Groq
from dotenv import load_dotenv
import re
import json
import logging

load_dotenv()
logger = logging.getLogger("uvicorn.error")

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_recommendation(resume, job_description, score):
    logger.info(f"resume: {resume}, score: {score}")
    # 1. System Prompt: Contains the persona, rules, and output schema
    system_prompt = """You are an expert ATS (Applicant Tracking System) and Senior Technical Recruiter. 
Your objective is to evaluate a candidate's resume against a specific Job Description (JD) impartially, accurately, and strictly based on the provided text.

INSTRUCTIONS & LOGIC (Follow Strictly):
1. SOURCE OF TRUTH: The Job Description is the absolute source of truth. Evaluate the resume ONLY against the criteria listed in the JD. Do not hallucinate or assume skills.
2. MANDATORY VS. PREFERRED: 
   - Reject if ANY mandatory requirement is missing.
3. SMART SYNONYMS & CONTEXT: 
   - Recognize industry-standard acronyms (e.g., "AWS" = "Amazon Web Services", "React.js" = "React").
4. YEARS OF EXPERIENCE (YoE): 
   - Calculate based on dates provided. If missing, flag in the evaluation.
5. BIAS ELIMINATION: Ignore demographic data. Judge solely on merit.
6. INCORPORATING THE SEMANTIC SCORE: 
   - If the score is high but a mandatory requirement is missing, Reject.

OUTPUT FORMAT:
Return your response EXCLUSIVELY as a valid JSON object matching this schema exactly:
{
  "evaluation": {
    "meets_all_mandatory_requirements": true/false,
    "missing_mandatory_requirements": [],
    "missing_preferred_requirements": [],
    "strengths": [],
    "experience_gap_flag": true/false
  },
  "recommendation_summary": "string",
  "final_decision": "Shortlist" | "Partial Match" | "Reject"
}"""

    # 2. User Prompt: Contains only the specific data for this run
    user_prompt = f"""
Job Description:
----------------
{job_description}

Candidate Resume:
-----------------
{resume}

Pre-calculated Semantic Score:
------------------------------
{score:.2f}%
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.1, # Lowered slightly for strict deterministic formatting
            response_format={"type": "json_object"} # Forces valid JSON output at the API level
        )

        raw_output = response.choices[0].message.content.strip()

        # 3. Fallback cleanup just in case the API ignores response_format
        # Removes ```json and ``` if they exist
        raw_output = re.sub(r"^```(?:json)?\n?", "", raw_output)
        raw_output = re.sub(r"\n?```$", "", raw_output)

        # Parse into a Python dictionary before returning
        parsed_json = json.loads(raw_output)
        return parsed_json

    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse LLM JSON output. Error: {e}\nRaw Output: {raw_output}")
        # Return a safe fallback object so your frontend/database doesn't crash
        return {
            "evaluation": {"meets_all_mandatory_requirements": False, "missing_mandatory_requirements": ["Parsing Error"], "missing_preferred_requirements": [], "strengths": [], "experience_gap_flag": False},
            "recommendation_summary": "System encountered an error parsing the evaluation.",
            "final_decision": "Review"
        }
    except Exception as e:
        logger.error(f"LLM API call failed: {e}")
        return {"error": "API communication failed."}