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
#canvas.create_polygon((x1,y1, x2,y2, x3,y3))
#canvas.create_arc()

'''
canvas.create_rectangle((50,20,100,200), fill = 'red', width=5, outline = 'blue')
canvas.create_oval((200,0,300,100),fill = 'green')
canvas.create_line(0,0,100,150, fill = 'blue')
#canvas.create_polygon((0,0, 100,200, 300,50), fill = 'grey')
canvas.create_arc((200,0,300,100),fill='red', start=45,
                  extent = 270, style = tk.ARC, outline = 'red',
                  width = 10)
'''

#canvas.create_text((100,100), text = 'this is some text', fill = 'green')
# canvas.create_window((150,100),
#                      window=ttk.Button(window,
#                                       text=' this is text in a canvas'))

'''
Exercise: use event binding to create a basic app
'''
colors = ('black', 'blue', 'red', 'green')
color_string = tk.StringVar(value=colors[0])
color_picker = ttk.Combobox(window, textvariable=color_string)
color_picker['values']=colors
color_picker.pack()

def brush_size_adjust(event):
    global brush_size

def draw_func(event):
    print(f'x: {event.x} y: {event.y}')
    canvas.create_oval(event.x,event.y,event.x+5,event.y+5,
                       fill=color_string.get(),outline=color_string.get())

canvas.bind('<B1-Motion>', draw_func)


''' Loop '''
window.mainloop()
