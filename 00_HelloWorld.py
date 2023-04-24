"""
01_Demo.py 
04/21/23
Hello World
"""

import tkinter as tk            # Basic Logic
from tkinter import ttk         # Widgets

# Creating a window
window = tk.Tk()
window.title('Demo')
window.geometry('800x500')


# Title
title_label = ttk.Label(master = window, text = 'Hello World', font = 'Calibri 24 bold')
title_label.pack()
# Running a main loop
window.mainloop()
