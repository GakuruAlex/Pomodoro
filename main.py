from tkinter import Canvas, PhotoImage, Tk, Label, Button
from pomodoro import Pomodoro
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"



def main()-> None:
    window = Tk()
    check_mark = []
    
    window.title("Pomodoro App")
    window.config(padx=100, pady=50, bg=YELLOW)
    timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
    timer.grid(row=0, column=2)
    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness= 0)
    tomato_img =PhotoImage(file="/home/aleyg/projects/Python/100DaysOfCode/DayTwentyEight/Pomodoro/tomato.png")
    canvas.create_image(100,112 ,image=tomato_img )
    timer_text = canvas.create_text(120, 125, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
    canvas.grid(row=1, column=2)
    for i in range(1,5):
        checkmark = Label(text= "",fg=GREEN, bg=YELLOW, font=("DejaVu Sans",25))
        checkmark.grid(row = 4, column= i)
        check_mark.append(checkmark)
    pomodoros = Pomodoro(canvas=canvas, window=window, timer_text=timer_text, check_mark=check_mark, timer = timer)
    start = Button(text="Start", font=(FONT_NAME, 14, "bold"), highlightthickness=0, bg=YELLOW, borderwidth=0, command=pomodoros.start_timer)

    start.grid(row=3, column=1)
    reset = Button(text="Reset", font=(FONT_NAME, 14, "bold"), highlightthickness=0, bg=YELLOW, borderwidth=0, command=pomodoros.reset_timer)
    reset.grid(row=3, column=3)
    
    
    
    
    window.mainloop()

if __name__ == "__main__":
    main()