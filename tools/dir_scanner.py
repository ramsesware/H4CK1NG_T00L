import requests
import tkinter as tk
from concurrent.futures import ThreadPoolExecutor
from utils.http_requests import make_request
from tkinter import messagebox
import threading
detener_escaneo = False

def realizar_peticion(url, directorio):
    full_url = f"{url}/{directorio}"
    response = make_request(full_url)
    if response.status_code == 200:
        return directorio 

def start_directory_analysis(url, diccionario, progress_bar, resultado_texto, parent):
    global detener_escaneo
    detener_escaneo = False  # Resetear el control de detención
    
    if diccionario:
        progress_bar["maximum"] = len(diccionario)
        
        def realizar_peticiones():

            def peticion_individual(url, directorio):
                if detener_escaneo:  # Si se ha activado la bandera de detención
                    return None
                result = realizar_peticion(url, directorio)
                
                if result:
                    # Actualiza el área de texto en tiempo real con el directorio encontrado
                    resultado_texto.insert(tk.END, f"Directorio encontrado: {result}\n", "green_text")
                    resultado_texto.see(tk.END)  # Hacer scroll automáticamente al final
                return result

            # Crea un ejecutor para paralelizar las peticiones
            with ThreadPoolExecutor(max_workers=10) as executor:  # 10 hilos para paralelizar
                future_to_directorio = {executor.submit(peticion_individual, url, directorio): directorio for directorio in diccionario}
                
                for i, future in enumerate(future_to_directorio):
                    if detener_escaneo:  # Si se ha activado la bandera de detención, salir del bucle
                        break
                    future.result()  # Bloquea hasta que el thread actual termine

                    # Actualiza la barra de progreso y la interfaz
                    progress_bar["value"] = i + 1
                    parent.update_idletasks()  # Asegura que la interfaz se actualice inmediatamente

            if not detener_escaneo:
                messagebox.showinfo("Finalizado", "Análisis completado.")
        
        thread = threading.Thread(target=realizar_peticiones)
        thread.start()
    else:
        messagebox.showwarning("Advertencia", "No se seleccionó ningún diccionario")

def stop_analysis():
    global detener_escaneo
    detener_escaneo = True
    messagebox.showinfo("Escaneo detenido", "El escaneo de directorios ha sido detenido.")

def clear_results(resultado_texto, progress_bar):
    resultado_texto.delete("1.0", tk.END)
    progress_bar["value"] = 0
    messagebox.showinfo("Resultados limpiados", "El cuadro de texto y la barra de progreso han sido limpiados.")