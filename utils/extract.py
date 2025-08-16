import io
from PyPDF2 import PdfReader
from docx import Document


def extract_text_from_pdf(file_stream) -> str:
    try:
        reader = PdfReader(file_stream)
        texts = []
        for p in reader.pages:
            t = p.extract_text()
            if t:
                texts.append(t)
        return "\n".join(texts)
    except Exception as e:
        return ""


def extract_text_from_docx(file_stream) -> str:
    try:
        # file_stream is a BytesIO-like object
        doc = Document(file_stream)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception:
        return ""


def extract_text(uploaded_file) -> str:
    """Accepts a Streamlit UploadedFile or a file path. Returns extracted text."""
    if uploaded_file is None:
        return ""

    name = getattr(uploaded_file, "name", None)
    if name and name.lower().endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)
    elif name and name.lower().endswith(".docx"):
        return extract_text_from_docx(uploaded_file)
    else:
        # fallback: try reading decoded text
        try:
            uploaded_file.seek(0)
            raw = uploaded_file.read()
            if isinstance(raw, bytes):
                return raw.decode("utf-8", errors="ignore")
            return str(raw)
        except Exception:
            return ""