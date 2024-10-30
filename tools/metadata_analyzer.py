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
                "Título": props.title,
                "Autor": props.author,
                "Último autor": props.last_modified_by,
                "Fecha de creación": props.created,
                "Última modificación": props.modified,
                "Categoría": props.category,
                "Comentarios": props.comments
            }
    except Exception as e:
        messagebox.showerror("Error", f"Error al analizar el archivo: {e}")
