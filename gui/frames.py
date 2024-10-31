import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tools.dir_scanner import start_directory_analysis, stop_analysis, clear_results
from tools.metadata_analyzer import analyze_metadata
from utils.file_handler import select_file
from gui.dark_theme import apply_dark_theme

frames_tools = {}

def create_main_window(root):
    root.title("Cibersecurity tools")
    root.geometry("1200x900")
    root.configure(bg="#2d2d2d")

    # Apply dark theme
    style = ttk.Style()
    apply_dark_theme(style)

    # Create principal container
    container = ttk.Frame(root, padding="10")
    container.pack(fill="both", expand=True)

    # Create tools menu
    menu = tk.Menu(root, bg="#2d2d2d", fg="lime", activebackground="gray", activeforeground="black", font=("Consolas", 16))
    root.config(menu=menu)

    # Tools menu
    tools_menu = tk.Menu(menu, font=("Consolas", 16), tearoff=0, bg="#2d2d2d", fg="lime")
    menu.add_cascade(label="Tools", menu=tools_menu)

    # Create frames for each tool
    frames_tools["directory_analyzer"] = create_directory_analysis_frame(container)
    frames_tools["metadata_analyzer"] = create_metadata_analysis_frame(container)

    # Add options to menu
    tools_menu.add_command(label="Web Directory Analyzer", command=lambda: tool_swap("directory_analyzer"))
    tools_menu.add_command(label="Metadata Analyzer", command=lambda: tool_swap("metadata_analyzer"))

    # Show initially Web Directory Analyzer
    tool_swap("directory_analyzer")

def tool_swap(tool):
    for frame in frames_tools.values():
        frame.pack_forget()  # Hide all frames

    # Show frame of selected tool
        frames_tools[tool].pack(fill="both", expand=True)

def create_directory_analysis_frame(parent):
    directories_frame = ttk.Frame(parent)
    
    # Field to insert URL
    ttk.Label(directories_frame, text="URL:", font=("Consolas", 16), foreground="lime", background="#2d2d2d").grid(row=0, column=0, padx=5, pady=5)
    url_entry = ttk.Entry(directories_frame, width=50, font=("Consolas", 16))
    url_entry.grid(row=0, column=1, padx=5, pady=5)

    selected_dictionary = []

    # Botón para seleccionar diccionario
    def select_dictionary():
        nonlocal selected_dictionary
        filepath = select_file([("Text Files", "*.txt")])
        if filepath:
            with open(filepath, "r") as f:
                selected_dictionary = f.read().splitlines()
            dictionary_label.config(text=f"Selected dictionary: {os.path.basename(filepath)}")
        else:
            messagebox.showwarning("Warning", "Dictionary not selected")


    # Área de texto para mostrar resultados
    result_frame = ttk.Frame(directories_frame)
    result_frame.grid(row=5, columnspan=2, padx=5, pady=5)
    result_text = tk.Text(result_frame, height=20, width=80, font=("Consolas", 16), bg="#3c3f41", fg="lime", insertbackground="white")
    result_text.tag_configure("green_text", foreground="lime")
    scrollbar = ttk.Scrollbar(result_frame, orient="vertical", command=result_text.yview)
    result_text.configure(yscrollcommand=scrollbar.set)
    result_text.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    dictionary_btn = tk.Button(directories_frame, text="Select Dictionary", command=select_dictionary, font=("Consolas", 16), bg="#3c3f41", fg="lime")
    dictionary_btn.grid(row=1, column=0, padx=5, pady=5)

    dictionary_label = ttk.Label(directories_frame, text="Dictionary not selected", font=("Consolas", 16), foreground="lime", background="#2d2d2d")
    dictionary_label.grid(row=1, column=1, padx=5, pady=5)

    # Botones para análisis
    analyze_btn = tk.Button(directories_frame, text="Analyze", command=lambda: start_directory_analysis(url_entry.get(), selected_dictionary, progress, result_text, parent), font=("Consolas", 16), bg="#3c3f41", fg="lime")
    analyze_btn.grid(row=2, column=0, padx=5, pady=5)

    stop_btn = tk.Button(directories_frame, text="Stop", command=stop_analysis, font=("Consolas", 16), bg="#3c3f41", fg="lime")
    stop_btn.grid(row=3, column=0, padx=5, pady=5)

    progress = ttk.Progressbar(directories_frame, orient="horizontal", length=500, mode="determinate", style="Custom.Horizontal.TProgressbar")
    progress.grid(row=4, columnspan=2, padx=5, pady=5)

    clean_btn = tk.Button(directories_frame, text="Clean", command=lambda: clear_results(result_text, progress), font=("Consolas", 16), bg="#3c3f41", fg="lime")
    clean_btn.grid(row=3, column=1, padx=5, pady=5)

    return directories_frame

def create_metadata_analysis_frame(parent):
    metadata_frame = ttk.Frame(parent)

    # Create text area to show results of metadata
    result_metadata_frame = ttk.Frame(metadata_frame)
    result_metadata_frame.grid(row=1, columnspan=2, padx=5, pady=5)
    result_text_metadata = tk.Text(result_metadata_frame, height=20, width=80, font=("Consolas", 16), bg="#3c3f41", fg="lime", insertbackground="white")
    result_text_metadata.tag_configure("green_text", foreground="lime")
    scrollbar_metadata = ttk.Scrollbar(result_metadata_frame, orient="vertical", command=result_text_metadata.yview)
    result_text_metadata.configure(yscrollcommand=scrollbar_metadata.set)
    result_text_metadata.pack(side="left", fill="both", expand=True)
    scrollbar_metadata.pack(side="right", fill="y")

    select_btn = tk.Button(metadata_frame, text="Select File", command=lambda: show_metadata(analyze_metadata(select_file([("PDF Files", "*.pdf"), ("Word Files", "*.docx")])), result_text_metadata), font=("Consolas", 16), bg="#3c3f41", fg="lime")
    select_btn.grid(row=0, column=0, padx=5, pady=5)

    return metadata_frame

def show_metadata(data, result_text_metadata):
    if data:
        result_text_metadata.delete("1.0", tk.END)
        for key, value in data.items():
            result_text_metadata.insert(tk.END, f"{key}: {value}\n")
    else:
        messagebox.showwarning("Warning", "Didn't find metadata or not selected a correct file.")
