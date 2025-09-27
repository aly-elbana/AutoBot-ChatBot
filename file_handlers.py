"""
File handling utilities for processing different file types.
"""
import json
import base64
import os
import csv
import xml.etree.ElementTree as ET
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


def csv_to_text(filepath):
    """Extract text from CSV files."""
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            csv_reader = csv.reader(f)
            rows = []
            for row in csv_reader:
                rows.append(", ".join(row))
            return "\n".join(rows)
    except Exception as e:
        return f"[Error reading CSV: {e}]"


def xml_to_text(filepath):
    """Extract text from XML files."""
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
        
        def extract_text(element):
            text = element.text or ""
            for child in element:
                text += " " + extract_text(child)
            if element.tail:
                text += " " + element.tail
            return text.strip()
        
        return extract_text(root)
    except Exception as e:
        return f"[Error reading XML: {e}]"


def get_file_type_info(filepath):
    """Get file type information and appropriate icon."""
    ext = os.path.splitext(filepath)[1].lower()
    
    # Programming languages
    if ext in [".py"]:
        return "🐍", "Python"
    elif ext in [".js", ".jsx"]:
        return "🟨", "JavaScript"
    elif ext in [".ts", ".tsx"]:
        return "🔷", "TypeScript"
    elif ext in [".html"]:
        return "🌐", "HTML"
    elif ext in [".css", ".scss", ".sass", ".less"]:
        return "🎨", "CSS"
    elif ext in [".cpp", ".c", ".h", ".hpp", ".cc", ".cxx"]:
        return "⚙️", "C/C++"
    elif ext in [".java"]:
        return "☕", "Java"
    elif ext in [".kt"]:
        return "🟣", "Kotlin"
    elif ext in [".php"]:
        return "🐘", "PHP"
    elif ext in [".rb"]:
        return "💎", "Ruby"
    elif ext in [".go"]:
        return "🐹", "Go"
    elif ext in [".rs"]:
        return "🦀", "Rust"
    elif ext in [".swift"]:
        return "🦉", "Swift"
    elif ext in [".dart"]:
        return "🎯", "Dart"
    elif ext in [".r"]:
        return "📊", "R"
    elif ext in [".scala"]:
        return "🔺", "Scala"
    elif ext in [".m", ".mm"]:
        return "🍎", "Objective-C"
    elif ext in [".cs", ".csx"]:
        return "🔷", "C#"
    
    # Data formats
    elif ext in [".json"]:
        return "📋", "JSON"
    elif ext in [".yaml", ".yml"]:
        return "⚙️", "YAML"
    elif ext in [".xml"]:
        return "📄", "XML"
    elif ext in [".csv"]:
        return "📊", "CSV"
    elif ext in [".sql"]:
        return "🗄️", "SQL"
    
    # Documentation
    elif ext in [".md"]:
        return "📝", "Markdown"
    elif ext in [".rst"]:
        return "📖", "reStructuredText"
    elif ext in [".tex"]:
        return "📚", "LaTeX"
    
    # Scripts
    elif ext in [".sh", ".bash"]:
        return "🐚", "Bash"
    elif ext in [".zsh"]:
        return "🐚", "Zsh"
    elif ext in [".fish"]:
        return "🐟", "Fish"
    elif ext in [".ps1"]:
        return "💻", "PowerShell"
    elif ext in [".bat", ".cmd"]:
        return "🪟", "Batch"
    
    # Config files
    elif ext in [".ini", ".cfg"]:
        return "⚙️", "Config"
    elif ext in [".log"]:
        return "📋", "Log"
    
    # Images
    elif ext in [".png", ".jpg", ".jpeg"]:
        return "🖼️", "Image"
    
    # Documents
    elif ext == ".pdf":
        return "📄", "PDF"
    elif ext == ".ipynb":
        return "📓", "Jupyter Notebook"
    
    # Default
    else:
        return "📄", "Text"
