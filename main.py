from itertools import count
from tkinter import *
import math

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
    timer_label.config(text="Timer")
    check_mark_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK) 
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.floor(count / 60)
    # Alternatively...use integer division
    # minutes = count // 60  
    seconds = count % 60
    # Use Dynamic Typing to change the data type of variable seconds from integer to string.
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if  count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        check_marks = ""
        completed_work_sessions = reps // 2
        for session in range(completed_work_sessions):
            check_marks += "✔"
        check_mark_label.config(text=check_marks)
            

# ---------------------------- UI SETUP ------------------------------- #
# Create Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
# timer_text canvas widget
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)


# Create Timer label
timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# Create Start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# Create Reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# Create check mark
check_mark_label = Label(text="", font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=1, row=3)


# Keep Window open and listen for events
window.mainloop()