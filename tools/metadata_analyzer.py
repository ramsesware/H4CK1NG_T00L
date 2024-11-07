# Copyright (C) 2024 Moisés Ceñera Fernández
# This file is part of H4CK1NG_T00L.
# 
# H4CK1NG_T00L is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# H4CK1NG_T00L is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with H4CK1NG_T00L. If not, see <https://www.gnu.org/licenses/>.

from PyPDF2 import PdfReader, PdfWriter
from docx import Document
from tkinter import messagebox
import os
from PIL import Image
import piexif
import tkinter as tk

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
        elif filepath.lower().endswith('.jpg') | filepath.lower().endswith('.jpeg') | filepath.lower().endswith('.png'):
            
            image = Image.open(filepath)
            
            if "exif" in image.info:
                
                exif_data = piexif.load(image.info["exif"])
                metadata = {}
                
                for ifd in exif_data:
                    for tag, value in exif_data[ifd].items():
                        tag_name = piexif.TAGS[ifd].get(tag, tag)
                        metadata[tag_name] = value
                        
                return metadata
            
    except Exception as e:
        messagebox.showerror("Error", f"Error on file analyzing: {e}")

def remove_metadata_pdf(filepath):
    reader = PdfReader(filepath)
    writer = PdfWriter()
    for page in range(len(reader.pages)):
        writer.add_page(reader.pages[page])

    writer.add_metadata({})

    with open(filepath, "wb") as f:
        writer.write(f)

def remove_metadata_word(filepath):
    document = Document(filepath)
    propieties = document.core_properties
    propieties.author = None
    propieties.title = None
    propieties.subject = None
    propieties.keywords = None
    propieties.last_modified_by = None
    propieties.created = None
    propieties.modified = None

    document.save(filepath)

def remove_metadata_image(filepath):
    imagen = Image.open(filepath)
    if "exif" in imagen.info:
        imagen.info.pop("exif")
    imagen.save(filepath)


def remove_metadata_file(filepath):
    try:
        extension = os.path.splitext(filepath)[1].lower()

        if extension in ['.jpg', '.jpeg', '.png']:
            remove_metadata_image(filepath)
            return f"File: {os.path.basename(filepath)} metadata has been removed correctly"
        elif extension == '.pdf':
            remove_metadata_pdf(filepath)
            return f"File: {os.path.basename(filepath)} metadata has been removed correctly"
        elif extension == '.docx':
            remove_metadata_word(filepath)
            return f"File: {os.path.basename(filepath)} metadata has been removed correctly"
        else:
            return f"Couldn't have removed metadata from file: {os.path.basename(filepath)}"
            
    except Exception as e:
        messagebox.showerror("Error", f"Error on removing metadata from a file: {e}")


def remove_metadata_directory(file_list):
    try:
        info_list = []
        for file in file_list:
            info_list.append(remove_metadata_file(file))
        return info_list
    except Exception as e:
        messagebox.showerror("Error", f"Error on removing metadata from a directory: {e}")


def analyze_metadata_directory(file_list):
    try:
        info_list = []
        for file_read in file_list:
            info = analyze_metadata(file_read)
            info_list.append({
                "filename": file_read,
                "metadata": info
            }) 
        return info_list
    except Exception as e:
        messagebox.showerror("Error", f"Error on file analyzing: {e}")

def clear_results_metadata(result_text):
    result_text.delete("1.0", tk.END)
    messagebox.showinfo("Results cleared", "Text area have been cleared.")
