import tempfile
from pathlib import Path
from unittest.mock import patch

from backend.services.parser import (
    extract_pdf_text,
    extract_docx_text,
    extract_text,
)


def test_extract_txt_file():
    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".txt",
        delete=False
    ) as f:
        f.write("Hello Resume Screening")
        path = f.name

    text = extract_text(path)

    assert text == "Hello Resume Screening"

    Path(path).unlink()


@patch("backend.services.parser.extract_pdf_text")
def test_extract_text_calls_pdf(mock_pdf):
    mock_pdf.return_value = "PDF Content"

    result = extract_text("resume.pdf")

    mock_pdf.assert_called_once_with("resume.pdf")
    assert result == "PDF Content"


@patch("backend.services.parser.extract_docx_text")
def test_extract_text_calls_docx(mock_docx):
    mock_docx.return_value = "DOCX Content"

    result = extract_text("resume.docx")

    mock_docx.assert_called_once_with("resume.docx")
    assert result == "DOCX Content"


def test_extract_unknown_file():
    result = extract_text("resume.csv")

    assert result == ""


@patch("backend.services.parser.docx2txt.process")
def test_extract_docx_text(mock_process):
    mock_process.return_value = (
        "Java Developer\n\nSpring Boot\n\nReact"
    )

    result = extract_docx_text("resume.docx")

    assert "Java Developer" in result
    assert "Spring Boot" in result
    assert "React" in result


@patch("backend.services.parser.docx2txt.process")
def test_extract_docx_exception(mock_process):
    mock_process.side_effect = Exception("DOCX Error")

    result = extract_docx_text("resume.docx")

    assert result == ""


@patch("backend.services.parser.fitz.open")
def test_extract_pdf_text(mock_open):
    page1 = type(
        "Page",
        (),
        {"get_text": lambda self: "Java "}
    )()

    page2 = type(
        "Page",
        (),
        {"get_text": lambda self: "Developer"}
    )()

    pdf = mock_open.return_value
    pdf.__iter__.return_value = [page1, page2]

    result = extract_pdf_text("resume.pdf")

    assert result == "Java Developer"

    pdf.close.assert_called_once()