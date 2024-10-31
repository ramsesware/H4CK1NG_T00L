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

def analyze_metadata_directory(file_list):
    try:
        info_list = []
        for file_read in file_list:
            if file_read.lower().endswith('.pdf'):
                with open(file_read, 'rb') as file:
                    pdf = PdfReader(file)
                    info = pdf.metadata
                    info_list.append({
                        "filename": file_read,
                        "metadata": info
                    }) 
            elif file_read.lower().endswith('.docx'):
                doc = Document(file_read)
                props = doc.core_properties
                doc_info = {
                    "Title": props.title,
                    "Author": props.author,
                    "Last author": props.last_modified_by,
                    "Creation date": props.created,
                    "Last modify": props.modified,
                    "Category": props.category,
                    "Comments": props.comments
                }
                info_list.append({
                    "filename": file_read,
                    "metadata": doc_info
                })
        return info_list
    except Exception as e:
        messagebox.showerror("Error", f"Error on file analyzing: {e}")
