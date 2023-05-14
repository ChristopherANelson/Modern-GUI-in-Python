import tkinter as tk
from tkinter import ttk

### Create a window ###
window = tk.Tk()
window.geometry('600x400')
window.title('Frames and parenting')

### Frame ###
frame = ttk.Frame(window, width = 100, height = 200, borderwidth = 10, relief= tk.GROOVE)
frame.pack_propagate(False)
frame.pack()


### Master setting ###
label = ttk.Label(frame, text = 'Label in frame')
label.pack()

### Loop ### 
window.mainloop()
