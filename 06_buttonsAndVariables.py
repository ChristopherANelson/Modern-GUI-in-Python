import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

#window = tk.Tk()
window = ttk.Window(themename='lumen')
window.title('Buttons and Variables')
window.geometry('600x400')

# Button
def button_func():
    print('A basic function')

button_string = tk.StringVar(value = 'A button with string var')
button = ttk.Button(window,command=button_func,textvariable=button_string)
button.pack()

# Check Button
check_var = tk.IntVar(value=10)
check = ttk.Checkbutton(window,text='checkbox 1',
                        command=lambda: print(check_var.get()),
                        variable=check_var,
                        onvalue=10,
                        offvalue=5)
check.pack()

check2 = ttk.Checkbutton(window,text='checkbox 2',
                        command=lambda: check_var.set(5))
check2.pack()


# Radio button
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(window,
                         text='Radio Button 1',
                         value = 'radio 1',
                         variable = radio_var,
                         command = lambda: print(radio_var.get()))
radio1.pack()
radio2 = ttk.Radiobutton(window, 
                         text='Radio Button 2',
                         value = 2,
                         variable = radio_var,
                         command = lambda: print(radio_var.get()))
radio2.pack()




### EXERCISE
tk.Label(window,text='\nEXERCISE\n').pack()

exercise_check = tk.Checkbutton(window,text='CheckButton',
                                onvalue = 'A',
                                offvalue = 0,
                                command=lambda:print(radio_value.get())).pack()
radio_value = tk.StringVar()
radio3 = ttk.Radiobutton(window,text='A', value='A',
                         variable = radio_value,
                         command = lambda: print(radio_value.get())).pack()
radio4 = ttk.Radiobutton(window,text='B', value='B',
                         variable = radio_value,
                         command = lambda: print(radio_value.get())).pack()




# Loop
window.mainloop()
