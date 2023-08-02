"""How to create a screen, a label, an interactive button and an entry field"""

import tkinter

# SCREEN:
screen = tkinter.Tk()
screen.minsize(width=800, height=800)
screen.title("My First GUI")

# LABEL:
label = tkinter.Label(text="Button not clicked")
label.pack()

# ENTRY (Input Field):
input_field = tkinter.Entry(width=50)
input_field.pack()


# BUTTON (and it's function used for a command):
def button_clicked():
    user_text = input_field.get()
    label.config(text=user_text)


button = tkinter.Button(text="Click here", command=button_clicked)
button.pack()

# ENTRY FIELD (generally used for a short text):
entry_field = tkinter.Entry(width=30)
entry_field.insert(0, string="SHORT TEXT box")
entry_field.pack()
print(entry_field.get())

# TEXT FIELDS (generally used for long texts):
text_field = tkinter.Text(height=6, width=30)
text_field.pack()
text_field.focus()
text_field.insert(
    tkinter.END, "Testing this LONG TEXT FIELD.\nI want to see if everything is ok. Hard to know all of this by heart!")
print(text_field.get("1.0", tkinter.END))

# SPINBOX (A small box containing an int. Beside there are up and down arrows and when user clicks on it, there is increase or decrease):


def get_spinbox_num():
    print(spinbox.get())


# ... notice that spinbox function may get a command (function) as parameter:
spinbox = tkinter.Spinbox(from_=8, to=16, increment=2, command=get_spinbox_num)
spinbox.pack()

# CHECK BUTTON ("XLD if not answered?")


def yes_or_no():
    if check_state.get() == 1:
        print("Yes")
    else:
        print("No")


check_state = tkinter.IntVar()
check_button = tkinter.Checkbutton(
    text="XLD if not answered?", variable=check_state, command=yes_or_no)
check_button.pack()

# RadioButton ("Where did you find me? Instagram, facebook, blog, etc..." ONLY ONE can be selected!)


def which_radio():
    if radio_check.get() == 0:
        print("Instagram")
    elif radio_check.get() == 1:
        print("Facebook")
    elif radio_check.get() == 2:
        print("Blog")


radio_check = tkinter.IntVar()
radio_one = tkinter.Radiobutton(
    text="Instagram", value=0, variable=radio_check, command=which_radio)
radio_one.pack()
radio_two = tkinter.Radiobutton(
    text="Facebook", value=1, variable=radio_check, command=which_radio)
radio_two.pack()
radio_three = tkinter.Radiobutton(
    text="Blog", value=2, variable=radio_check, command=which_radio)
radio_three.pack()

# LISTBOX ("Which ocaions you would like to hire? Waiting Room, Ceremony, Cocktail, etc). ONLY ONE can be selected")


def chosen_ocasion(event):
    print(list_box.get(list_box.curselection()))


list_box = tkinter.Listbox(height=4)
ocasions = ["Waiting Room", "Ceremony", "Cocktail", "Lunch or Dinner", "Party"]

for ocasion in ocasions:
    list_box.insert(ocasions.index(ocasion), ocasion)

list_box.bind("<<ListboxSelect>>", chosen_ocasion)
list_box.pack()
screen.mainloop()
