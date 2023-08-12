import tkinter as tk
from tkinter import messagebox as mb
from random import choice, randint, shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """Create a secure password made with letters, numbers and symbols, using random module"""

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
               ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]

    number_list = [choice(numbers) for _ in range(randint(2, 4))]

    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]

    total_list = letter_list + number_list + symbol_list

    shuffle(total_list)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, "".join(total_list))


# ---------------------------- SAVE PASSWORD ------------------------------- #


def validate():
    """
    Pop up an error message box if there is at least one empty field. Otherwise, run 'save' fuction 
    in order to colect data and insert into a txt file.
    """
    empty_field = [
        len(website_entry.get()) == 0,
        len(email_user_entry.get()) == 0,
        len(password_entry.get()) == 0
    ]
    if any(empty_field):
        mb.showerror(title="Empty Field!",
                     message="You can not leave any fields empty!")
    else:
        save()


def save():
    """Colect data and insert into a txt file. Clears inserted data from window afterwards."""
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()

    confirmation = mb.askokcancel(
        title=website_entry.get(),
        message=(
            f"Do you confirm the following data?\n"
            f"Website: {website}\n"
            f"Email/Username: {email}\n"
            f"Password: {password}"
        )
    )

    # Creating json file
    new_data = {
        website: {
            "email" : email, 
            "password" : password
        }

    }
    if confirmation:
        try:
            with open("password_manager/data.json", "r") as data_file:
                data_readed = json.load(data_file)
        except FileNotFoundError:
            with open("password_manager/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data_readed.update(new_data)
            with open("password_manager/data.json", "w") as data_file:
                json.dump(data_readed, data_file, indent=4)
        finally:    
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")


canvas = tk.Canvas(height=200, width=200, bg="white", highlightthickness=0)
locker_img = tk.PhotoImage(file="password_manager/logo.png")
canvas.create_image(100, 100, image=locker_img)
canvas.grid(column=1, row=0)

# Website Layout
website_label = tk.Label(text="Website:", fg="black", bg="white")
website_label.grid(column=0, row=1)
website_entry = tk.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew")
website_entry.focus()

# E-mail/User Layout
email_user_label = tk.Label(text="Email/Username:", fg="black", bg="white")
email_user_label.grid(column=0, row=2)
email_user_entry = tk.Entry(width=35)
email_user_entry.insert(0, "digofarah@gmail.com")
email_user_entry.grid(column=1, row=2, columnspan=2, sticky="ew")

# Password Layout
password_label = tk.Label(text="Password:", fg="black", bg="white")
password_label.grid(column=0, row=3)
password_entry = tk.Entry(width=21)
password_entry.grid(column=1, row=3, sticky="nsew")

# Buttons Layout
generate_button = tk.Button(text="Generate Password", font=(
    "Arial", 10), fg="black", bg="white", height=1, command=generate_password)
generate_button.grid(column=2, row=3, sticky="nsew")
add_button = tk.Button(text="add", font=("Arial", 10),
                       width=32, fg="black", bg="white", command=validate)
add_button.grid(column=1, row=4, columnspan=2, sticky="nsew")

window.mainloop()
