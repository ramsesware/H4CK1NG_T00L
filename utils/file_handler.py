from tkinter import filedialog

def select_file(filetypes):
    filepath = filedialog.askopenfilename(filetypes=filetypes)
    return filepath
