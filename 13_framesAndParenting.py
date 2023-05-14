import tkinter as tk
from tkinter import ttk

### Create a window ###
window = tk.Tk()
#window.geometry('600x400')
window.title('Frames and parenting')

### Frame ###
frame = ttk.Frame(window, width = 200, height = 200, borderwidth = 10, relief= tk.GROOVE)
frame.pack_propagate(False) 
#Frames will automatically adjust to size of widgets inside. pack_propagate will change that behavior
frame.pack(side = 'left')


### Master setting ###
label = ttk.Label(frame, text = 'Label in frame')
label.pack()

button = tk.Button(frame, text = 'Button in frame')
button.pack()

# Example
label2 = ttk.Label(window, text = 'Label outside frame')
label2.pack(side='left')

'''
Exercise: 
    * Create another frame with a label, a button, 
        and an entry and place it to the right of the other widgets
'''

exercise_frame = ttk.Frame(window, width=250, height=200,
                           borderwidth=10, relief=tk.GROOVE)
exercise_frame.pack(side='right')
exercise_frame.pack_propagate(False)

exercise_label = tk.Label(exercise_frame, text='Label')
exercise_label.pack()

exercise_entry_string = tk.StringVar(value='Entry widget')
exercise_entry = ttk.Entry(exercise_frame, textvariable=exercise_entry_string)
exercise_entry.pack(side='left')

exercise_button = ttk.Button(exercise_frame, text='Button')
exercise_button.pack(side='right')

### Loop ### 
window.mainloop()
