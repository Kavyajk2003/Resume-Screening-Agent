import fitz
from docx import Document
import docx2txt

def extract_pdf_text(file_path):
    text = ""

    pdf = fitz.open(file_path)

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text

def extract_docx_text(file_path):
    """
    Extracts text from a .docx file while natively maintaining 
    the sequential flow of paragraphs and tables.
    """
    try:
        # docx2txt handles the underlying XML parsing automatically
        text = docx2txt.process(file_path)
        
        # Clean up excessive newlines that often come from Word formatting
        clean_text = "\n".join([line for line in text.splitlines() if line.strip()])
        return clean_text
    
    except Exception as e:
        print(f"Error parsing DOCX: {e}")
        return ""


def extract_text(file_path):

    if file_path.endswith(".pdf"):
        return extract_pdf_text(file_path)

    if file_path.endswith(".docx"):
        return extract_docx_text(file_path)

    if file_path.endswith(".txt"):
        with open(file_path, "r") as f:
            return f.read()

    return ""