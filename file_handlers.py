"""
File handling utilities for processing different file types.
"""
import json
import base64
import os
from PyPDF2 import PdfReader


def pdf_to_text(filepath):
    """Extract text from PDF files."""
    reader = PdfReader(filepath)
    all_text = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            all_text.append(text)
    return "\n".join(all_text)


def ipynb_to_text(filepath):
    """Extract text from Jupyter Notebook cells."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        texts = []
        for cell in data.get("cells", []):
            if "source" in cell:
                cell_text = "".join(cell["source"])
                texts.append(cell_text)
        return "\n\n".join(texts)
    except Exception as e:
        return f"[Error reading ipynb: {e}]"


def image_to_base64(filepath):
    """Convert image file to base64 string with proper MIME type."""
    ext = os.path.splitext(filepath)[1].lower()
    mime = "image/png" if ext == ".png" else "image/jpeg"
    with open(filepath, "rb") as f:
        b = f.read()
    return base64.b64encode(b).decode("utf-8"), mime


def read_text_file(filepath):
    """Read content from text files."""
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception as e:
        return f"[Error reading file: {e}]"
