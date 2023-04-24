import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('button pressed')

# Window
window = tk.Tk()
window.title('Tkinter Variables')
window.geometry('300x300')

# tkinter variable
string_var = tk.StringVar(value = 'start value')
exercise_string_var = tk.StringVar(value = 'Exercise Value')

# widgets
label = ttk.Label(master = window, text = 'Label', textvariable=string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable=string_var)
entry.pack()

button = ttk.Button(master = window, text='button',command=button_func)
button.pack()


# exercise
ttk.Label(master = window, text = 'Enter Text', textvariable=exercise_string_var).pack()
ttk.Entry(master=window,textvariable=exercise_string_var).pack()
ttk.Entry(master=window,textvariable=exercise_string_var).pack()

# Run
window.mainloop()
