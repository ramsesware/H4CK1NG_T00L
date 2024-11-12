import tkinter as tk
from tkinter import ttk

def apply_dark_theme(style):
    style.configure("TFrame", background="#2d2d2d")
    style.configure("TLabel", background="#2d2d2d", foreground="lime")
    style.configure("TEntry", fieldbackground="#3c3f41", foreground="lime")
    style.configure("Custom.Horizontal.TProgressbar", troughcolor="#3c3f41", background="#5a5e62")
