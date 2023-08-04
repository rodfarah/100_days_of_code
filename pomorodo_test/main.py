"""Pomodoro Technique is a way of improving productivity when studying"""

import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

check_mark = "✔"
repetition_num = 0
after_function = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(after_function)
    upper_label.config(text="Timer")
    check_label.config(text="")
    canvas.itemconfig(clock, text="00:00")
    global repetition_num
    repetition_num = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global repetition_num
    repetition_num += 1
    if repetition_num == 9:
        global after_function
        window.after_cancel(after_function)
    elif repetition_num == 8:
        upper_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif repetition_num % 2 == 0:
        upper_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        upper_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def sec_to_minsec(secs: int) -> tuple[str, str]:
    """Return a tuple that convert a given integer of seconds into (minutes[str] and seconds[str]) format"""
    m_s = divmod(secs, 60)
    (m, s) = m_s
    m = str(m)
    s = str(s)
    if len(m) == 1:
        m = "0"+m
    if len(s) == 1:
        s = "0"+s
    return m, s


def count_down(secs: int):
    m, s = sec_to_minsec(secs)
    canvas.itemconfig(clock, text=f"{m}:{s}")
    if secs > 0:
        global after_function
        after_function = window.after(1000, count_down, secs-1)
    else:
        start_timer()
        how_many_checks = {1: "", 2: "✔", 3: "✔", 4: "✔✔",
                           5: "✔✔", 6: "✔✔✔", 7: "✔✔✔", 8: "✔✔✔✔", 9: "✔✔✔✔"}
        global repetition_num
        check_label.config(text=how_many_checks[repetition_num])


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

canvas = tk.Canvas(width=203, height=224, bg=YELLOW, highlightthickness=0)
photo = tk.PhotoImage(file="pomorodo_test/tomato.png")
canvas.create_image(101, 112, image=photo)
clock = canvas.create_text(103, 140, text="00:00",
                           fill="white", font=(FONT_NAME, 33, "bold"))
canvas.grid(column=1, row=1)

upper_label = tk.Label(text="Timer", font=(FONT_NAME, 42),
                       fg=GREEN, bg=YELLOW, highlightthickness=0)
upper_label.grid(column=1, row=0)

start_button = tk.Button(text="Start", bg="white",
                         highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)


reset_button = tk.Button(text="Reset", bg="white",
                         highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=2)

check_label = tk.Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()
