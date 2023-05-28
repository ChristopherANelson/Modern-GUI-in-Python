'''
Different layouts
05/21/2023
'''

import tkinter as tk
from tkinter import ttk

### Create a window ###
window = tk.Tk()
window.title('Layout intro')
window.geometry('600x400')

### Widgets ###
label1 = ttk.Label(window, text='Label 1', background='red')
label2 = ttk.Label(window, text='Label 2', background='blue')

# Pack #
# label1.pack(side='left', expand = True, fill = 'both')
# label2.pack(side='left', expand = False, fill = 'y')

# Grid #
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=2)
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)

# label1.grid(row=0, column=1, sticky='nsew') #North South East West
# label2.grid(row=1, column=1,columnspan=2, sticky='nsew') #North South East West


# Place #
label1.place(x=100,y=300, width=200, height=100)
label2.place(relx=0.5, rely=0.5, relwidth=1, anchor='se')

### Loop ###
window.mainloop()
