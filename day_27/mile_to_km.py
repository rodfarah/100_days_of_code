""" 1 mile = 1.60934 km"""


import tkinter as tk

screen = tk.Tk()
screen.title("Mile to Km Converter")
screen.minsize(width=600, height=300)
screen.config(padx=(300/4), pady=(300/4))

miles_input = tk.Entry(width=10)
miles_input.insert(0, string="0")
miles_input.focus()
miles_input.grid(column=1, row=0)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = tk.Label(text="is equal to")
equal_label.grid(column=0, row=1)

result_label = tk.Label(width=10, text="0")
result_label.grid(column=1, row=1)
# result_label.config(padx=100, pady=100)

km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1)


def convert():
    result = float(miles_input.get()) * 1.60934
    result_label.config(text=result)


click_to_convert = tk.Button(text="Calculate", command=convert)
click_to_convert.grid(column=1, row=3)

screen.mainloop()
