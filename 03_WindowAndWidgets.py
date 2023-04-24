"""
03_WindowAndWidgets.py
04/22/23
"""
import tkinter as tk
from tkinter import ttk

def button_func():
    print('a button has been pressed')

# Creating a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x800')

# ttk label
label = ttk.Label(master = window, text='This is text')
label.pack()


# tk.text
text = tk.Text(master = window)
text.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()


ttk.Label(master = window, text = 'This is a label').pack()
# ttk button
button = ttk.Button(master = window, text= 'Add', command = button_func)
button.pack()

ttk.Button(master = window, text = 'Say hello', command = lambda: print('hello')).pack()

#Main Loop
window.mainloop()
