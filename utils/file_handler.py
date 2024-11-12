from tkinter import filedialog
import os

def select_file(filetypes):
    filepath = filedialog.askopenfilename(filetypes=filetypes)
    return filepath

def select_directory():
    directory_path = filedialog.askdirectory()
    if not directory_path:
        return None  # Return None if no directory is selected
    file_list = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    return file_list