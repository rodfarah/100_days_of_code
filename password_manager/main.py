import tkinter as tk


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_entry.grid(column=1, row=1, columnspan=2, sticky="nsew")

# E-mail/User Layout
email_user_label = tk.Label(text="Email/Username:", fg="black", bg="white")
email_user_label.grid(column=0, row=2)
email_user_entry = tk.Entry(width=35)
email_user_entry.grid(column=1, row=2, columnspan=2, sticky="nsew")

# Password Layout
password_label = tk.Label(text="Password:", fg="black", bg="white")
password_label.grid(column=0, row=3)
password_entry = tk.Entry(width=21)
password_entry.grid(column=1, row=3, sticky="nsew")

# Buttons Layout
generate_button = tk.Button(text="Generate Password", fg="black", bg="white")
generate_button.grid(column=2, row=3, sticky="nsew")
add_button = tk.Button(text="add", width=32, fg="black", bg="white")
add_button.grid(column=1, row=4, columnspan=2, sticky="nsew")

window.mainloop()