import requests
import tkinter as tk
from concurrent.futures import ThreadPoolExecutor
from utils.http_requests import make_request
from tkinter import messagebox
import threading
stop_scan = False

def make_request_to_directory(url, directory):
    full_url = f"{url}/{directory}"
    response = make_request(full_url)
    if response.status_code == 200:
        return directory 

def start_directory_analysis(url, dictionary, progress_bar, result_text, parent):
    global stop_scan
    stop_scan = False  # Reset scan control
    
    if dictionary:
        progress_bar["maximum"] = len(dictionary)
        
        def make_requesting():

            def individual_request(url, directory):
                if stop_scan:  # If flag of scan control is activated
                    return None
                result = make_request_to_directory(url, directory)
                
                if result:
                    # Update text area on real time with found directory
                    result_text.insert(tk.END, f"Directory found: {result}\n", "green_text")
                    result_text.see(tk.END)  # Make scroll automatically 
                return result

            # Create an executor to parallelize requests
            with ThreadPoolExecutor(max_workers=10) as executor:  # 10 thread to parallelize
                future_to_directory = {executor.submit(individual_request, url, directory): directory for directory in dictionary}
                
                for i, future in enumerate(future_to_directory):
                    if stop_scan:  # If flag of scan control is activated, exit loop
                        break
                    future.result()  # Block since actual thread finish

                    # Update progress bar and interface
                    progress_bar["value"] = i + 1
                    parent.update_idletasks()  # Ensure that interface is updated inmediattly

            if not stop_scan:
                messagebox.showinfo("Finished", "Analyze completed.")
        
        thread = threading.Thread(target=make_requesting)
        thread.start()
    else:
        messagebox.showwarning("Warning", "Didn't select any dictionary")

def stop_analysis():
    global stop_scan
    stop_scan = True
    messagebox.showinfo("Scan stoped", "The directory scan has been stoped.")

def clear_results(result_text, progress_bar):
    result_text.delete("1.0", tk.END)
    progress_bar["value"] = 0
    messagebox.showinfo("Results cleared", "Text area and progress bar have been cleared.")