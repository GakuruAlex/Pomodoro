from tkinter import Canvas, PhotoImage, Tk
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

def main()-> None:
    window = Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=50, bg=YELLOW)
    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness= 0)
    tomato_img =PhotoImage(file="tomato.png")
    canvas.create_image(100,112 ,image=tomato_img )
    canvas.create_text(120, 125, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
    canvas.pack()

    window.mainloop()

if __name__ == "__main__":
    main()