import tkinter as tk
from tkinter import ttk

def button_func():
    entry_text = entry.get()

    # update label
    #label.configure(text = 'some other text')
    label['text'] = entry_text
    entry['state'] = 'disabled'
    #print(label.configure())


def reset_func():
    label['text'] = 'Label'
    entry['state'] = 'enabled'

# Creating a window
window = tk.Tk()
window.title('Getting and setting widgets')


# Create widgets
label = ttk.Label(master=window, text='Label')
label.pack()
entry = ttk.Entry(master=window)
entry.pack()
button = ttk.Button(master=window, text='Button',command=button_func)
button.pack()
reset_button = ttk.Button(master=window,text='Reset',command=reset_func)
reset_button.pack()



# Run 
window.mainloop()
