from tkinter import *
import time
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
    timer_label.config(text="Timer", fg=GREEN)
    global reps
    reps = 0
    checkmarks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_timer():
    working_sec = WORK_MIN * 60
    short_brk_sec = SHORT_BREAK_MIN * 60
    long_brk_sec = LONG_BREAK_MIN * 60
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(long_brk_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_brk_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(working_sec)
        timer_label.config(text="Work", fg=GREEN)


def count_down(seconds):
    minute_section = seconds // 60
    second_section = seconds % 60

    if second_section < 10:
        second_section = f"0{second_section}"

    canvas.itemconfig(timer_text, text=f"{minute_section}:{second_section}")

    if int(minute_section) == 0 and int(second_section) == 0:
        start_timer()
        working_sessions = reps // 2
        ticks = ""
        for _ in range(working_sessions):
            ticks += "✔"
        checkmarks.config(text=ticks)
        return
    global timer
    timer = window.after(1000, count_down, seconds - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Creating the Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

# Adding text to the canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Adding the label Timer
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

# Adding the Start button
start_btn = Button(text="Start", padx=20, pady=5, bg=RED, fg="white", command=start_timer)
start_btn.grid(column=0, row=2)

# Adding the reset button
reset_btn = Button(text="Reset",  padx=20, pady=5, bg=RED, fg="white", command=reset_timer)
reset_btn.grid(column=2, row=2)

# Adding the checkmark
checkmarks = Label(font=(FONT_NAME, 12, "normal"), fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)

window.mainloop()