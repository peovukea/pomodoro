from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0

    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text='Break', fg=RED)
    elif reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        title_label.config(text='Break', fg=PINK)
    else:
        count_down(WORK_MIN*60)
        title_label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=49, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

btnStart = Button()
btnStart.config(text="Start", width=4, height=1, command=start_timer)
btnStart.grid(column=0, row=2)
btnReset = Button()
btnReset.config(text="Reset", width=4, height=1, command=reset_timer)
btnReset.grid(row=2, column=2)

window.mainloop()
