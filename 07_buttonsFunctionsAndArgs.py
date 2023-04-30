import tkinter as tk
from tkinter import ttk

def button_func(entry_string):
    print('A button was pressed.')
    print(entry_string.get())
    

# Setup
window = tk.Tk()
window.title('Buttons Functions and Arguments')
window.geometry('800x500')

# Widgets
entry_string = tk.StringVar(value = 'Enter Text')
entry = ttk.Entry(window, textvariable=entry_string).pack()

button = ttk.Button(window, text='Set', command=lambda: button_func(entry_string))
button.pack()

# Loop
window.mainloop()
