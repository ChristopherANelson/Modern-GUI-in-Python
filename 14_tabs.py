'''
Tabs
05/14/2023
'''
import tkinter as tk
from tkinter import ttk

### Create a window ###
window = tk.Tk()
window.geometry('600x400')
window.title('Tabs')


### Notebook Widget ###
notebook = ttk.Notebook(window)

# Tab 1
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text='Text in tab 1')
label1.pack()
button1 = ttk.Button(tab1, text='Button in tab1')
button1.pack()

# Tab 2
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text='Text in tab 2')
label2.pack()
entry2 = ttk.Entry(tab2)
entry2.pack()




'''
Exercise: 
    * add another tab with 2 buttons and one label inside
'''


# Exercise Tab
exercise_tab = ttk.Frame(notebook)

exercise_label = tk.Label(exercise_tab, text='exercise label')
exercise_label.pack()

exercise_button1 = tk.Button(exercise_tab, text='Button 1')
exercise_button2 = tk.Button(exercise_tab, text='Button 2')
exercise_button1.pack(side='left')
exercise_button2.pack(side='right')


notebook.add(tab1,text='Tab 1')
notebook.add(tab2,text='Tab 2')
notebook.add(exercise_tab,text='Tab 3')
notebook.pack()

### Loop ###
window.mainloop()
