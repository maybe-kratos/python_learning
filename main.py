import math
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
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_time.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():

    global reps
    reps += 1
    print(reps)

    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label_time.config(text="Long Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 35, "bold"), highlightthickness=0)
    elif reps % 2 == 0:
        label_time.config(text="Short Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 35, "bold"), highlightthickness=0)
        count_down(short_break_sec)
    else:
        label_time.config(text="Work Time", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"), highlightthickness=0)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    min = int(count / 60)
    sec = count % 60
    if sec < 10 and min < 10:
        canvas.itemconfig(timer_text, text=f"0{min}:0{sec}")
    elif sec < 10:
        canvas.itemconfig(timer_text, text=f"{min}:0{sec}")
    elif sec > 10 > min:
        canvas.itemconfig(timer_text, text=f"0{min}:{sec}")
    elif sec > 10:
        canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    else:
        print("something went wrong")
    if count > 0:
        global timer
        timer = window.after(750, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"

        check_marks = Label(text=marks, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
        check_marks.grid(column=1, row=4)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Method")
window.config(padx=100, pady=50, bg=YELLOW, )

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label_time = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
label_time.grid(column=1, row=0)

start_button = Button(text="start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_marks.grid(column=1, row=4)

window.mainloop()
