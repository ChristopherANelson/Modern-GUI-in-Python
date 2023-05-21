'''
Changing the window
05/20/2023
'''

import tkinter as tk
from tkinter import ttk

### Create a window ###
window = tk.Tk()
window.title('Changing the window')
window.geometry('600x400+100+200') # +left +top
#window.iconbitmap('python.ico') # creates an icon on titlebar


### Window sizes ###
window.minsize(200,100)
# window.maxsize(800,700)
window.resizable(True, False)

### Screen attributes ###
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

### Window attributes ###
window.attributes('-alpha', 1)
# window.attributes('-topmost', True) #sets window on top of all windows
window.attributes('-fullscreen', True)

### Security event ###
window.bind('<Escape>', lambda event: window.quit())


### Title bar ###
# window.overrideredirect(True) #REMOVES TITLE BAR


### Loop ###
window.mainloop()
