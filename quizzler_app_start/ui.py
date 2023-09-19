import tkinter as tk
from data import question_data

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        self.score_label = tk.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="OPA!!!", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        wright_img = tk.PhotoImage(file="quizzler_app_start/images/true.png")
        self.wright_button = tk.Button(image=wright_img, highlightthickness=0)
        self.wright_button.grid(row=2, column=0)
        wrong_img = tk.PhotoImage(file="quizzler_app_start/images/false.png")
        self.wrong_button = tk.Button(image=wrong_img, highlightthickness=0)
        self.wrong_button.grid(row=2, column=1)

        self.window.mainloop()