import math
import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.2
LONG_BREAK_MIN = 4
REPS = 0

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        session_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif REPS % 2 == 0:
        session_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        session_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_minute = math.floor(count / 60)
    count_sec = int(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224,
                        bg=YELLOW, highlightthickness=0)
bg_img = tkinter.PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=bg_img)
timer_text = canvas.create_text(100, 130,
                                text="00:00",
                                fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

session_label = tkinter.Label(text="Timer",
                              fg=GREEN,
                              bg=YELLOW,
                              font=(FONT_NAME, 40, "bold"))
session_label.grid(column=1, row=0)

start_button = tkinter.Button(text="Start",
                              # font=(FONT_NAME, 12, "normal"),
                              # bg="white",
                              highlightthickness=0,
                              command=start_timer)
start_button.grid(column=0, row=2)

check_label = tkinter.Label(text="✔",
                            # font=(FONT_NAME, 12, "normal"),
                            fg=GREEN,
                            bg=YELLOW)
check_label.grid(column=1, row=3)

reset_button = tkinter.Button(text="Reset",
                              # font=(FONT_NAME, 12, "normal"),
                              # bg="white",
                              highlightthickness=0,
                              command=None,)
reset_button.grid(column=2, row=2)


window.mainloop()
