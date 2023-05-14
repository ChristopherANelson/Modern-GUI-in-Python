'''
Treeview
05/06/2023
'''
import tkinter as tk
from tkinter import ttk
import random
from random import choices

### Create a window ###
window = tk.Tk()
window.title('Treeview')
window.geometry('800x600')

### DATA ###
first_names = ['Bob','Maria','Alex','James','Susan','Henry','Lisa','Anna','Lisa']
last_names = ['Smith','Brown','Wilson','Thomson','Cook','Taylor','Walker','Clark','Roberts']

### Treeview ###
table = ttk.Treeview(window, columns = ('number','first','last','email'),show = 'headings')
table.heading('number', text = 'n')
table.heading('first', text = 'First name')
table.heading('last', text = 'Surname')
table.heading('email', text = 'Email')
table.pack(fill='both',expand=True)

# insert data into tables
for i in range(100):
    number = i
    first = random.choice(first_names)
    last = random.choice(last_names)
    email = f'{first[0]}{last}@email.com'
    data = (number,first,last,email)
    table.insert(parent='',index=0, values=data)

table.insert(parent='',index=tk.END,values=('XXXX','YYYY','ZZZZ'))


### Events ###
def item_selection(event):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])

def delete_items(event):
    print('delete')
    for i in table.selection():
        table.delete(i)

table.bind('<<TreeviewSelect>>', item_selection)
table.bind('<Delete>',delete_items)


### Loop ###
window.mainloop()



