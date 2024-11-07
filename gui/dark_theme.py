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

import tkinter as tk
from tkinter import ttk

def apply_dark_theme(style):
    style.configure("TFrame", background="#2d2d2d")
    style.configure("TLabel", background="#2d2d2d", foreground="lime")
    style.configure("TEntry", fieldbackground="#3c3f41", foreground="lime")
    style.configure("Custom.Horizontal.TProgressbar", troughcolor="#3c3f41", background="#5a5e62")
