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
from gui.frames import create_main_window

if __name__ == "__main__":
    root = tk.Tk()
    root.title("H4CK1NG_T00L")
    create_main_window(root)
    root.mainloop()
