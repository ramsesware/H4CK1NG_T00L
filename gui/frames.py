import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tools.dir_scanner import start_directory_analysis, stop_analysis, clear_results
from tools.metadata_analyzer import analyze_metadata
from utils.file_handler import select_file
from gui.dark_theme import apply_dark_theme

# Diccionario para almacenar los frames de las herramientas
herramientas_frames = {}

def create_main_window(root):
    root.title("Herramientas de Ciberseguridad - Modo Oscuro")
    root.geometry("1200x900")
    root.configure(bg="#2d2d2d")

    # Aplicar tema oscuro
    style = ttk.Style()
    apply_dark_theme(style)

    # Crear contenedor principal
    contenedor = ttk.Frame(root, padding="10")
    contenedor.pack(fill="both", expand=True)

    # Crear menú de herramientas
    menu = tk.Menu(root, bg="#2d2d2d", fg="lime", activebackground="gray", activeforeground="black", font=("Consolas", 16))
    root.config(menu=menu)

    # Menú de Herramientas
    herramientas_menu = tk.Menu(menu, font=("Consolas", 16), tearoff=0, bg="#2d2d2d", fg="lime")
    menu.add_cascade(label="Herramientas", menu=herramientas_menu)

    # Crear frames para cada herramienta y añadirlos al diccionario
    herramientas_frames["analisis_directorios"] = create_directory_analysis_frame(contenedor)
    herramientas_frames["analisis_metadatos"] = create_metadata_analysis_frame(contenedor)

    # Añadir opciones al menú
    herramientas_menu.add_command(label="Análisis de Directorios Web", command=lambda: cambiar_herramienta("analisis_directorios"))
    herramientas_menu.add_command(label="Análisis de Metadatos", command=lambda: cambiar_herramienta("analisis_metadatos"))

    # Mostrar inicialmente el frame de análisis de directorios
    cambiar_herramienta("analisis_directorios")

def cambiar_herramienta(herramienta):
    """Oculta todos los frames y muestra solo el frame seleccionado."""
    for frame in herramientas_frames.values():
        frame.pack_forget()  # Ocultar todos los frames

    # Mostrar el frame correspondiente a la herramienta seleccionada
    herramientas_frames[herramienta].pack(fill="both", expand=True)

def create_directory_analysis_frame(parent):
    frame_directorios = ttk.Frame(parent)
    
    # Campo para ingresar la URL
    ttk.Label(frame_directorios, text="URL:", font=("Consolas", 16), foreground="lime", background="#2d2d2d").grid(row=0, column=0, padx=5, pady=5)
    url_entry = ttk.Entry(frame_directorios, width=50, font=("Consolas", 16))
    url_entry.grid(row=0, column=1, padx=5, pady=5)

    diccionario_seleccionado = []

    # Botón para seleccionar diccionario
    def seleccionar_diccionario():
        nonlocal diccionario_seleccionado
        filepath = select_file([("Text Files", "*.txt")])
        if filepath:
            with open(filepath, "r") as f:
                diccionario_seleccionado = f.read().splitlines()
            diccionario_label.config(text=f"Diccionario seleccionado: {os.path.basename(filepath)}")
        else:
            messagebox.showwarning("Advertencia", "No se seleccionó ningún diccionario")


    # Área de texto para mostrar resultados
    frame_resultado = ttk.Frame(frame_directorios)
    frame_resultado.grid(row=5, columnspan=2, padx=5, pady=5)
    resultado_texto = tk.Text(frame_resultado, height=20, width=80, font=("Consolas", 16), bg="#3c3f41", fg="lime", insertbackground="white")
    resultado_texto.tag_configure("green_text", foreground="lime")
    scrollbar = ttk.Scrollbar(frame_resultado, orient="vertical", command=resultado_texto.yview)
    resultado_texto.configure(yscrollcommand=scrollbar.set)
    resultado_texto.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    diccionario_btn = tk.Button(frame_directorios, text="Seleccionar Diccionario", command=seleccionar_diccionario, font=("Consolas", 16), bg="#3c3f41", fg="lime")
    diccionario_btn.grid(row=1, column=0, padx=5, pady=5)

    diccionario_label = ttk.Label(frame_directorios, text="Diccionario no seleccionado", font=("Consolas", 16), foreground="lime", background="#2d2d2d")
    diccionario_label.grid(row=1, column=1, padx=5, pady=5)

    # Botones para análisis
    analizar_btn = tk.Button(frame_directorios, text="Analizar", command=lambda: start_directory_analysis(url_entry.get(), diccionario_seleccionado, progreso, resultado_texto, parent), font=("Consolas", 16), bg="#3c3f41", fg="lime")
    analizar_btn.grid(row=2, column=0, padx=5, pady=5)

    detener_btn = tk.Button(frame_directorios, text="Detener", command=stop_analysis, font=("Consolas", 16), bg="#3c3f41", fg="lime")
    detener_btn.grid(row=3, column=0, padx=5, pady=5)

    progreso = ttk.Progressbar(frame_directorios, orient="horizontal", length=500, mode="determinate", style="Custom.Horizontal.TProgressbar")
    progreso.grid(row=4, columnspan=2, padx=5, pady=5)

    limpiar_btn = tk.Button(frame_directorios, text="Limpiar", command=lambda: clear_results(resultado_texto, progreso), font=("Consolas", 16), bg="#3c3f41", fg="lime")
    limpiar_btn.grid(row=3, column=1, padx=5, pady=5)

    return frame_directorios

def create_metadata_analysis_frame(parent):
    frame_metadatos = ttk.Frame(parent)

    # Crear área de texto para mostrar resultados de metadatos
    frame_resultado_metadatos = ttk.Frame(frame_metadatos)
    frame_resultado_metadatos.grid(row=1, columnspan=2, padx=5, pady=5)
    resultado_texto_metadatos = tk.Text(frame_resultado_metadatos, height=20, width=80, font=("Consolas", 16), bg="#3c3f41", fg="lime", insertbackground="white")
    resultado_texto_metadatos.tag_configure("green_text", foreground="lime")
    scrollbar_metadatos = ttk.Scrollbar(frame_resultado_metadatos, orient="vertical", command=resultado_texto_metadatos.yview)
    resultado_texto_metadatos.configure(yscrollcommand=scrollbar_metadatos.set)
    resultado_texto_metadatos.pack(side="left", fill="both", expand=True)
    scrollbar_metadatos.pack(side="right", fill="y")

    seleccionar_btn = tk.Button(frame_metadatos, text="Seleccionar Archivo", command=lambda: mostrar_metadatos(analyze_metadata(select_file([("Archivos PDF", "*.pdf"), ("Archivos Word", "*.docx")])), resultado_texto_metadatos), font=("Consolas", 16), bg="#3c3f41", fg="lime")
    seleccionar_btn.grid(row=0, column=0, padx=5, pady=5)

    return frame_metadatos

def mostrar_metadatos(datos, resultado_texto_metadatos):
    if datos:
        resultado_texto_metadatos.delete("1.0", tk.END)
        for key, value in datos.items():
            resultado_texto_metadatos.insert(tk.END, f"{key}: {value}\n")
    else:
        messagebox.showwarning("Advertencia", "No se encontraron metadatos o no se seleccionó un archivo válido.")
