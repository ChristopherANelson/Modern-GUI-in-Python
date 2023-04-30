import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f'x: {event.x} y: {event.y}')

''' Window '''
window = tk.Tk()
window.geometry('600x500')
window.title('Event Binding')

''' Widgets '''
text = tk.Text(window).pack()
entry = ttk.Entry(window).pack()
button = ttk.Button(window, text='A button').pack()

''' Events ''' 
# window.bind(event,function)
# event = '<Alt-KeyPress-a>'

window.bind('<Alt-KeyPress-a>', lambda event: print(event))
window.bind('<Motion>', get_pos)
window.bind('<KeyPress>', lambda event: print(f'A button was pressed. ({event.char})'))

entry.bind('<FocusIn>', lambda event: print('entry field was selected'))











''' Loop '''
window.mainloop()
