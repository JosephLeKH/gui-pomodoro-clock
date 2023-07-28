"""
Purpose: Create a responsive GUI Pomodoro app
Tools: Tkinter, time (window.after), global var
"""
from tkinter import *
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
    window.after_cancel(timer)
    title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(clock, text="00:00")
    checks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
#Determine work/break and the amount of time
def start_timer():
    global reps
    reps += 1

    sec = WORK_MIN * 60
    title.config(text="Work", fg=GREEN)

    #Take a short break after every work session and a long one after every 4
    if reps % 8 == 0:
        sec = LONG_BREAK_MIN * 60
        title.config(text="Break", fg=PINK)
    elif reps % 2 == 0:
        sec = SHORT_BREAK_MIN * 60
        title.config(text="Break", fg=RED)

    count_down(sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
#Count down the timer
def count_down(count):
    global timer
    count_min = count // 60
    count_sec = count % 60
    check_nums=""
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(clock, text=f"{count_min}:{count_sec}")
    #Count down 1s by delaying 1s and calling the method again
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        #Add a check mark after each work session
        if reps % 2 == 1:
            check_nums += "✔"
            checks.config(text=check_nums)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title.grid(column=1, row=0)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(103, 112, image=tomato_img)
clock = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", font=(FONT_NAME, 12, "normal"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 12, "normal"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checks = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
checks.grid(column=1, row=3)


window.mainloop()