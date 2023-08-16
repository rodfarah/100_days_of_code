import tkinter as tk
import pandas as pd
from random import choice
from tkinter import messagebox as mb

BACKGROUND_COLOR = "#B1DDC6"


# ----------------- INPUT DATA Setup --------------------

data_frame = pd.read_csv("flashy/data/french_words.csv")
data_frame.set_index("French")
words_dict = dict(zip(data_frame["French"], data_frame["English"]))

french_list = [key for key in words_dict.keys()]
initial_len = len(french_list)
chosen_word = ""

# ---------------------- Program Setup -------------------------

def hit_start_first():
    mb.showwarning(title="Give a try!", message="Please, hit start/stop button first!")

def start_stop():
    if len(french_list) == 0:
        card.itemconfig(upper_text, text="")
        card.itemconfig(lower_text, text="")
        mb.showinfo(title="CONGRATS!", message="You've learned all words!")
        quit()

    global running
    if running:
        card.itemconfig(upper_text, text="")
        card.itemconfig(lower_text, text="Thank You!")
        running = False
    else:
        global chosen_word
        running = True
        chosen_word = choice(french_list)
        card.itemconfig(upper_text, text="French")
        card.itemconfig(lower_text, text=chosen_word)

        # Set changes after 3 seconds:
        window.after(3000, lambda: card.create_image(400, 265, image=backc_back))
        window.after(3000, lambda: card.itemconfig(upper_text, text="English", fill="white"))
        window.after(3000, lambda: card.itemconfig(lower_text, text=f"{words_dict[chosen_word]}", fill="white"))
        

def check_button_clicked():
    if card.cget("text") == "Flashy Test":
        hit_start_first()
    else:
        global running
        global chosen_word
        french_list.remove(chosen_word)
        running = False
        card.create_image(400, 265, image=frontc_back)
        start_stop()


def cross_button_clicked():
    if len(french_list) == initial_len:
        hit_start_first()
    else:
        global running
        running = False
        card.create_image(400, 265, image=frontc_back)
        start_stop()


# ---------------------- UI Setup ----------------------

# Creating Window
window = tk.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Creating Canvas
frontc_back = tk.PhotoImage(file="flashy/images/card_front.png")
backc_back = tk.PhotoImage(file="flashy/images/card_back.png")

card = tk.Canvas(width=800, height=526, highlightthickness=0,
                 background=BACKGROUND_COLOR)
card.create_image(400, 265, image=frontc_back)
card.grid(column=0, row=0, columnspan=3)

# Creating Texts
upper_text = card.create_text(400, 150,
    text="Flashy Test", 
    fill="black",
    font=("Ariel", 40, "bold")
)
lower_text = card.create_text(400, 263,
    text="Hit 'Start/Stop' button below!", 
    fill= "black",
    font=("Ariel", 20, "italic")
)


# Creating Buttons
cross_image = tk.PhotoImage(file="flashy/images/wrong.png")
cross_button = tk.Button(window, image=cross_image, command=cross_button_clicked)
cross_button.grid(column=0, row=1)

check_image = tk.PhotoImage(file="flashy/images/right.png")
check_button = tk.Button(window, image=check_image, bg="white", highlightthickness=0, command=check_button_clicked)
check_button.grid(column=2, row=1)

running = False
ss_button = tk.Button(text="Start / Stop", command=start_stop)
ss_button.grid(column=1, row=1)


window.mainloop()
