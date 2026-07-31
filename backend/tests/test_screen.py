from fastapi.testclient import TestClient
from unittest.mock import patch

from backend.main import app

client = TestClient(app)


@patch("backend.routers.screen.generate_recommendation")
@patch("backend.routers.screen.calculate_similarity")
@patch("backend.routers.screen.extract_text")
def test_screen_candidates(
    mock_extract_text,
    mock_similarity,
    mock_generate_recommendation,
):
    mock_extract_text.return_value = "Java Spring Boot React"

    mock_similarity.return_value = 87.5

    mock_generate_recommendation.return_value = {
        "final_decision": "Shortlist",
        "recommendation_summary": "Strong profile",
        "evaluation": {
            "strengths": ["Java", "Spring Boot"],
            "missing_mandatory_requirements": [],
            "missing_preferred_requirements": [],
        },
    }

    files = [
        (
            "resumes",
            (
                "resume.txt",
                b"Java Resume",
                "text/plain",
            ),
        )
    ]

    data = {
        "job_description": "Java Developer with Spring Boot"
    }

    response = client.post(
        "/screen/",
        files=files,
        data=data,
    )

    assert response.status_code == 200

    body = response.json()

    assert body["total_candidates"] == 1

    assert body["results"][0]["candidate"] == "resume.txt"

    assert body["results"][0]["score"] == 87.5

    assert (
        body["results"][0]["recommendation"]["final_decision"]
        == "Shortlist"
    )

    assert body["results"][0]["rank"] == 1


def test_screen_without_job_description():
    files = [
        (
            "resumes",
            (
                "resume.txt",
                b"Resume",
                "text/plain",
            ),
        )
    ]

    response = client.post(
        "/screen/",
        files=files,
    )

    assert response.status_code == 422


def test_screen_without_resume():
    response = client.post(
        "/screen/",
        data={
            "job_description": "Python Developer"
        },
    )

    assert response.status_code == 422