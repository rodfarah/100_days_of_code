import tkinter as tk


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    entries = [website_entry.get(), email_user_entry.get(), password_entry.get()]
    item_to_add = " | ".join(entries) + "\n"
    with open("password_manager/logfile.txt", "a") as logfile:
        logfile.writelines(item_to_add)
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
generate_button = tk.Button(text="Generate Password", font=("Arial", 10), fg="black", bg="white", height=1)
generate_button.grid(column=2, row=3, sticky="nsew")
add_button = tk.Button(text="add", font=("Arial", 10), width=32, fg="black", bg="white", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="nsew")

window.mainloop()