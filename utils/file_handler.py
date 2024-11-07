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
