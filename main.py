
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer_ob=None
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def reset_timer():
    global timer_ob
    window.after_cancel(timer_ob)
    canvas.itemconfig(timer, text="00:00")
    timer_title.config(text="Timer")
    checkmark.config(text="")

def start_timer():
    global reps
    reps+=1
    session=0
    mark=""

    if reps%2==1:
        minutes=WORK_MIN
        timer_title.config(text="WORK", fg=GREEN)
        session+=1
        for i in range(session-1):
            mark+="✔"
            checkmark.config(text=mark)
    elif reps%8==0:
        minutes=LONG_BREAK_MIN
        timer_title.config(text="BREAK", fg=RED)
    else:
        minutes=SHORT_BREAK_MIN
        timer_title.config(text="BREAK", fg=PINK)
    if session==4:
        session=0
    window.grab_set()
    countdown(minutes*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer_ob
    if count>=0:
        min=int(count/60)
        sec=int(count%60)
        if sec==0:
            sec="00"
        elif sec<10:
            sec="0"+str(sec)
        canvas.itemconfig(timer, text=f"{min} : {sec}")
        timer_ob=window.after(1000, countdown, count-1)
# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Pomodoro")
window.config(height=600, width=600, padx=100, pady=100, bg=YELLOW)

timer_title=Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_title.grid(column=1, row=0)

start_b=Button(text="Start", command=start_timer)
reset_b=Button(text="Reset", command=reset_timer)

checkmark=Label(text="", fg=GREEN)

start_b.grid(column=0, row=2)
checkmark.grid(column=1,row=2)
reset_b.grid(column=2, row=2)

canvas= Canvas(height=300, width=300, bg=YELLOW)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(150,150, image=tomato)
timer=canvas.create_text(150,170, text="00:00", fill="white",  font=(FONT_NAME, 17, "bold"))
canvas.grid(column=1, row=1)
start_timer()

window.mainloop()