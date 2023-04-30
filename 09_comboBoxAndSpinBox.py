'''
ComboBox and SpinBox
04/30/2023
'''

import tkinter as tk
from tkinter import ttk

''' Creating a window '''
window = tk.Tk()
window.title('Combo and Spin Box')
window.geometry('800x500')

''' ComboBox '''
items = ('Ice cream', 'Pizza', 'Brocoli')
food_string = tk.StringVar(value=items[0])
combo = ttk.Combobox(window, textvariable=food_string)
combo['values']=items
#combo.configure(values=items)
combo.pack()

''' Events '''
combo.bind('<<ComboboxSelected>>',
           lambda event: combo_label.config(text=f'Selected value: {food_string.get()}')) 

combo_label = ttk.Label(window, text = 'Label')
combo_label.pack()


''' Spinbox '''
spin_int = tk.IntVar(value=12)
spin = ttk.Spinbox(window, from_ = 3, to = 21,
                   command = lambda: print(f'({spin_int.get()})'),
                   textvariable=spin_int)
spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down'))
#spin['value']=(1,2,3,4,5)
spin.pack()

'''
Exercise: create a spinbox that contains the letters A B C D E
and print the value whenever the value is decreased
'''

'''
tk.Label(window, text = '\n\nEXERCISE').pack()

exercise_spin_str = tk.StringVar(value='A')
exercise_spin = ttk.Spinbox(window,
                            command = lambda: print(exercise_spin_str.get()),
                            textvariable=exercise_spin_str)
exercise_spin['values'] = ('A', 'B', 'C', 'D', 'E')
exercise_spin.bind('<<Decrement>>', lambda event: print(exercise_spin_str.get()))
exercise_spin.pack()
'''


tk.Label(window, text = '\n\nEXERCISE').pack()

exercise_letters = ('A', 'B', 'C', 'D', 'E')
exercise_string = tk.StringVar(value = exercise_letters[0])
exercise_spin2 = ttk.Spinbox(window,textvariable=exercise_string,
                             values=exercise_letters)
exercise_spin2.pack()

exercise_spin2.bind('<<Decrement>>', lambda event: print(exercise_string.get()))



''' Loop '''
window.mainloop()
