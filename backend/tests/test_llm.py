from unittest.mock import patch, MagicMock

from backend.services.llm import generate_recommendation


@patch("backend.services.llm.client.chat.completions.create")
def test_generate_recommendation_success(mock_create):
    mock_response = MagicMock()

    mock_response.choices = [
        MagicMock(
            message=MagicMock(
                content="""
{
  "evaluation": {
    "meets_all_mandatory_requirements": true,
    "missing_mandatory_requirements": [],
    "missing_preferred_requirements": [],
    "strengths": ["Java", "Spring Boot"],
    "experience_gap_flag": false
  },
  "recommendation_summary": "Excellent candidate",
  "final_decision": "Shortlist"
}
"""
            )
        )
    ]

    mock_create.return_value = mock_response

    result = generate_recommendation(
        "Java Spring Boot Resume",
        "Need Java Developer",
        90.5,
    )

    assert result["final_decision"] == "Shortlist"

    assert result["evaluation"][
        "meets_all_mandatory_requirements"
    ] is True

    assert result["recommendation_summary"] == "Excellent candidate"


@patch("backend.services.llm.client.chat.completions.create")
def test_generate_recommendation_invalid_json(mock_create):
    mock_response = MagicMock()

    mock_response.choices = [
        MagicMock(
            message=MagicMock(
                content="INVALID JSON"
            )
        )
    ]

    mock_create.return_value = mock_response

    result = generate_recommendation(
        "Resume",
        "Job Description",
        75.0,
    )

    assert result["final_decision"] == "Review"

    assert (
        result["recommendation_summary"]
        == "System encountered an error parsing the evaluation."
    )


@patch("backend.services.llm.client.chat.completions.create")
def test_generate_recommendation_api_failure(mock_create):
    mock_create.side_effect = Exception("API Failure")

    result = generate_recommendation(
        "Resume",
        "Job Description",
        80.0,
    )

    assert result == {
        "error": "API communication failed."
    }


@patch("backend.services.llm.client.chat.completions.create")
def test_generate_recommendation_calls_groq(mock_create):
    mock_response = MagicMock()

    mock_response.choices = [
        MagicMock(
            message=MagicMock(
                content="""
{
  "evaluation":{
    "meets_all_mandatory_requirements":true,
    "missing_mandatory_requirements":[],
    "missing_preferred_requirements":[],
    "strengths":[],
    "experience_gap_flag":false
  },
  "recommendation_summary":"Good",
  "final_decision":"Shortlist"
}
"""
            )
        )
    ]

    mock_create.return_value = mock_response

    generate_recommendation(
        "Resume",
        "Job",
        95.0,
    )

    mock_create.assert_called_once()