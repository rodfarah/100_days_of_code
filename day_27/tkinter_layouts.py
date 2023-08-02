""" 
Diference between pack(), place() and grid() layouts
pack() is sort of automatic, centralized position.
On place() you have to specify x and y coordinates.
grid() create imaginary collums and rows (according to the number of elements(fields) my program has.

Notice on line 16 and 24 that it is possible to add pad to screen borders!
"""


import tkinter as tk

screen = tk.Tk()
screen.minsize(height= 600, width=600)
screen.title("My first GUI Program")
screen.config(padx= 20, pady=20)



label = tk.Label(text="New Text", font=("Times New Roman", 24, "bold"))
# label.pack()
# label.place(x=0, y=0)
label.grid(column=0, row=0)
label.config(padx=50, pady=50 )
def change_label():
    label.config(text=entry.get())

button = tk.Button(text="Click Me", command=change_label)
# button.pack()
# button.place(x=300, y=300)
button.grid(column=1, row=1)

entry = tk.Entry(width= 50)
# entry.pack()
# entry.place(x=480, y=550)
entry.grid(column=3, row=2)

def exit_program():
    exit()

new_button = tk.Button(text="Exit Button", command=exit_program)
new_button.grid(column=2, row=0)


screen.mainloop()