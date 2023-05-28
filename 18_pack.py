'''
Pack method
05/28/2023
'''
import tkinter as tk
from tkinter import ttk

### Create a window ###
window = tk.Tk()
window.title('Pack')
window.geometry('400x600')

### Widgets ###
label1 = ttk.Label(window, text='First label', background='red')
label2 = ttk.Label(window, text='label 2', background='blue')
label3 = ttk.Label(window, text='Last of the labels', background='green')
button = ttk.Button(window, text='Button')


### Layout ###
label1.pack(side = 'top', expand=True, fill ='both')
label3.pack(side = 'top')
button.pack(side = 'top', expand=True, fill='y')

### Loop ###
window.mainloop()
