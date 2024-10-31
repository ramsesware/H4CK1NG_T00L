from PyPDF2 import PdfReader
from docx import Document
from tkinter import messagebox

def analyze_metadata(filepath):
    try:
        if filepath.lower().endswith('.pdf'):
            with open(filepath, 'rb') as file:
                pdf = PdfReader(file)
                info = pdf.metadata
                return info
        elif filepath.lower().endswith('.docx'):
            doc = Document(filepath)
            props = doc.core_properties
            return {
                "Title": props.title,
                "Author": props.author,
                "Last author": props.last_modified_by,
                "Creation date": props.created,
                "Last modify": props.modified,
                "Category": props.category,
                "Comments": props.comments
            }
    except Exception as e:
        messagebox.showerror("Error", f"Error on file analyzing: {e}")
