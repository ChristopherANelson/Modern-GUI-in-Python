'''
Menu using tkinter
05/15/2023
'''
import tkinter as tk
from tkinter import ttk

### Create a window ###
window = tk.Tk()
window.title('Menu')
window.geometry('600x400')



### Menu ###
menu = tk.Menu(window)

# sub menu
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label='New', command=lambda: print('New file'))
file_menu.add_command(label='Open', command=lambda: print('Open file'))
file_menu.add_separator()
menu.add_cascade(label = 'File', menu = file_menu)


# another sub menu
help_menu = tk.Menu(menu, tearoff = False)
file_menu.add_command(label='Help entry', command=lambda: print(help_check_string.get()))

help_check_string = tk.StringVar()
help_menu.add_checkbutton(label = 'check', onvalue= 'on', offvalue='off', variable=help_check_string)

menu.add_cascade(label='Help', menu=help_menu)



'''
Example:
    add another menu to the main menu, this one should have a sub menu
'''

pref_menu = tk.Menu(menu, tearoff=False)
pref_menu.add_checkbutton(label = 'Fullscreen',
                          command=lambda: print('Fullscreen'))
menu.add_cascade(label='Preferences', menu=pref_menu)



window.configure(menu=menu)



# menu button
menu_button = ttk.Menubutton(window, text = 'Menu Button')
menu_button.pack()

button_sub_menu = tk.Menu(menu_button, tearoff=False)
button_sub_menu.add_command(label = 'entry1', command = lambda: print('test 1'))
button_sub_menu.add_checkbutton(label='check 1')
menu_button.configure(menu = button_sub_menu)



### Loop ###
window.mainloop()
