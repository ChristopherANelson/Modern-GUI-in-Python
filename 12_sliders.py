'''
Sliders
05/06/2023
'''
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


## Create a window ###
window = tk.Tk()
window.title('Sliders')
#window.geometry('600x400')

### Silder ###
scale_double = tk.DoubleVar(value = 15)
scale = ttk.Scale(window, 
                  command = lambda value: print(scale_double.get()), 
                  from_=0, to=30,
                  length = 300, orient='vertical',
                  variable = scale_double)
scale.pack()


### Progress Bar ###
progress = ttk.Progressbar(window, variable = scale_double,
                           maximum=30, orient='horizontal',
                           mode = 'determinate',
                           length = 400)
progress.pack()


progress2 = ttk.Progressbar(window, maximum=30, orient='horizontal',
                            mode = 'indeterminate',
                            length = 400)
progress2.pack()
progress2.start(250) #250 millisec

### Scrolledtext ###
scrolled_text = scrolledtext.ScrolledText(window, 
                                          width = 100, height=20)
scrolled_text.pack()

### Loop ###
window.mainloop()

