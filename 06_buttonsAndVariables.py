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
'''
EXERCISE:
    create another checkbutton and 2 radiobuttons
    radio button:
        values for the buttons are A and B
        ticking either prints the value of the checkbutton
        ticking the radio button unchecks the checkbutton
    check button:
        ticking the checkbutton prints the value of the radio button value
        use tkinter var for booleans
'''
tk.Label(window,text='\nEXERCISE\n').pack()

def radio_func():
    print(check_bool.get())
    check_bool.set(False)

radio_string = tk.StringVar()
check_bool = tk.BooleanVar()

exercise_radio1 = ttk.Radiobutton(window,text='Radio A',
                                  value='A', variable=radio_string,
                                  command=radio_func)
exercise_radio2 = ttk.Radiobutton(window,
                                  text='Radio B',value='B',
                                  variable=radio_string, command=radio_func)
exercise_check = ttk.Checkbutton(window, text='exercise_check',variable=check_bool,
                                 command = lambda: print(radio_string.get()))

exercise_radio1.pack()
exercise_radio2.pack()
exercise_check.pack()

# Loop
window.mainloop()
