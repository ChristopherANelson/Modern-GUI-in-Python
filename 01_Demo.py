"""
01_Demo.py 
04/21/23
Miles to Kilometer Demo using tkinter
"""

import tkinter as tk            # Basic Logic
#from tkinter import ttk         # Widgets
import ttkbootstrap as ttk


def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)


# Creating a window
window = ttk.Window(themename='journal')
window.title('Demo')
window.geometry('800x500')


# Title
title_label = ttk.Label(master = window, text = 'Miles to Kilometers', font = 'Calibri 24 bold')
title_label.pack()

# Input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable=entry_int)
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
# The button and entry -> Input field
# Input field -> window
entry.pack(side = 'left', padx = 10); button.pack(side = 'left')
input_frame.pack(pady = 10)



output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24 bold', textvariable=output_string)
output_label.pack(pady = 5)


# Running a main loop
window.mainloop()
