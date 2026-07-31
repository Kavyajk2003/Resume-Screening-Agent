from fastapi.testclient import TestClient
from unittest.mock import patch

from backend.main import app

client = TestClient(app)


@patch("backend.routers.resume.extract_text")
def test_upload_pdf_resume(mock_extract_text):
    mock_extract_text.return_value = (
        "Java Spring Boot React Developer"
    )

    files = {
        "file": (
            "resume.pdf",
            b"Dummy PDF Content",
            "application/pdf",
        )
    }

    response = client.post(
        "/resume/upload",
        files=files,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Resume uploaded successfully"
    assert data["filename"] == "resume.pdf"
    assert data["characters"] == len(
        "Java Spring Boot React Developer"
    )
    assert data["preview"] == "Java Spring Boot React Developer"


@patch("backend.routers.resume.extract_text")
def test_upload_docx_resume(mock_extract_text):
    mock_extract_text.return_value = (
        "Python Django Developer"
    )

    files = {
        "file": (
            "resume.docx",
            b"Dummy DOCX Content",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
    }

    response = client.post(
        "/resume/upload",
        files=files,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["filename"] == "resume.docx"
    assert data["message"] == "Resume uploaded successfully"


def test_invalid_resume_file_type():
    files = {
        "file": (
            "resume.txt",
            b"Text Resume",
            "text/plain",
        )
    }

    response = client.post(
        "/resume/upload",
        files=files,
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "Only PDF and DOCX files are allowed."
    }


def test_resume_upload_without_file():
    response = client.post("/resume/upload")

    assert response.status_code == 422