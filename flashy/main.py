import tkinter as tk
import pandas as pd
from random import choice
from tkinter import messagebox as mb

BACKGROUND_COLOR = "#B1DDC6"


# -----------------  Data Setup ----------------------

try:
    loaded_data = pd.read_csv("flashy/data/saved_data.csv")
except FileNotFoundError:
    loaded_data = pd.read_csv("flashy/data/thousand_english.csv")
finally:
    words_dict = dict(zip(loaded_data["English"], loaded_data["Portuguese"]))

chosen_word = ""
wait = None


# ------------------- Program Setup----------------------


def hit_start_first():
    """Throw a warning message, telling user to click on 'start/stop' button first."""
    mb.showwarning(title="Give a try!",
                   message="Please, hit start/stop button first!")


def start_stop():
    """Start and stop the app"""
    if len(words_dict) == 0:
        card.itemconfig(upper_text, text="")
        card.itemconfig(lower_text, text="")
        mb.showinfo(title="CONGRATS!", message="You've learned all words!")
        quit()

    global running
    if running:
        card.itemconfig(upper_text, text="Thank You!")
        card.itemconfig(lower_text, text="")
        running = False
    else:
        global chosen_word, wait
        running = True
        chosen_word = choice([word for word in words_dict.keys()])
        card_to_english()
        wait = window.after(3000, card_to_portuguese)


def card_to_english():
    """Change card image and texts to english."""
    global upper_text, lower_text
    card.itemconfig(actual_card, image=frontc_image)
    card.itemconfig(upper_text, text="English", fill="black")
    card.itemconfig(lower_text, text=chosen_word, fill="black")


def card_to_portuguese():
    """Change card image and texts to english."""
    global chosen_word
    card.itemconfig(actual_card, image=backc_image)
    card.itemconfig(upper_text, text="Portuguese", fill="white")
    card.itemconfig(
        lower_text, text=f"{words_dict[chosen_word]}", fill="white")


def check_button_clicked():
    global running
    if not running:
        hit_start_first()
    else:
        global chosen_word, wait
        window.after_cancel(wait)
        words_dict.pop(chosen_word)
        running = False
        counter.config(text=f"Remaining Words: {len(words_dict)}")
        start_stop()
        saved_dict = pd.DataFrame.from_dict(
            words_dict, orient="index", columns=["Portuguese"])
        saved_dict.index.name = "English"
        saved_dict.to_csv("flashy/data/saved_data.csv")


def cross_button_clicked():
    global running
    if not running:
        hit_start_first()
    else:
        global chosen_word, wait
        window.after_cancel(wait)
        running = False
        start_stop()


# ---------------------- UI Setup ----------------------

# Creating Window
window = tk.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Creating Canvas
frontc_image = tk.PhotoImage(file="flashy/images/card_front.png")
backc_image = tk.PhotoImage(file="flashy/images/card_back.png")

card = tk.Canvas(width=800, height=526, highlightthickness=0,
                 background=BACKGROUND_COLOR)
actual_card = card.create_image(400, 265, image=frontc_image)
card.grid(column=0, row=0, columnspan=3)

# Creating Texts
upper_text = card.create_text(400, 150,
                              text="Flashy Test",
                              fill="black",
                              font=("Ariel", 40, "bold"))
lower_text = card.create_text(400, 300,
                              text="- An English word will appear.\n"
                              "- After three seconds,the word will be translated to Portuguese.\n"
                              "- Click on the cross button if did not know the translated word.\n"
                              "- Otherwise, click on the check button.\n\n"
                              "** Hit 'Start/Stop' button below when you are ready! **",
                              fill="black",
                              font=("Ariel", 14, "italic"),
                              anchor="center")


# Creating Buttons
cross_image = tk.PhotoImage(file="flashy/images/wrong.png")
cross_button = tk.Button(window, image=cross_image,
                         command=cross_button_clicked)
cross_button.grid(column=0, row=1, rowspan=2)

check_image = tk.PhotoImage(file="flashy/images/right.png")
check_button = tk.Button(window, image=check_image, bg="white",
                         highlightthickness=0, command=check_button_clicked)
check_button.grid(column=2, row=1, rowspan=2)

running = False
ss_button = tk.Button(text="Start / Stop", command=start_stop)
ss_button.grid(column=1, row=2)

# Creating Counter Label
counter = tk.Label(text=f"Remaining Words: {len(words_dict)}", font=(
    "Ariel", 12), bg=BACKGROUND_COLOR)
counter.grid(column=1, row=1)

window.mainloop()
