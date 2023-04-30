"""
Canvas
04/30/2023
"""

import tkinter as tk
from tkinter import ttk

''' Create a window '''
window = tk.Tk()
window.title('Canvas')
window.geometry('600x400')

''' Canvas'''
canvas = tk.Canvas(window, bg = 'white')
canvas.pack()

#canvas.create_rectangle((left,top,right,bottom))
#canvas.create_line(start_x,start_y,end_x,end_y)
canvas.create_rectangle((50,20,100,200), fill = 'red', width=5, outline = 'blue')
canvas.create_line(0,0,100,150)

''' Loop '''
window.mainloop()
