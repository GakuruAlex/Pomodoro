from time import strftime, gmtime
from math import floor
WORK_MIN = 1
SHORT_BREAK_MIN = 0.25
LONG_BREAK_MIN = 0.5
class Pomodoro:
    TICK = "✓"
    running = True
    ticks ={1:0, 3:1, 5:2, 7:3}
    def __init__(self, canvas, timer_text, window, check_mark, status):
        self.canvas = canvas
        self.timer_text = timer_text
        self.window = window
        self.check_mark = check_mark
        self.status = status
        self.counter = 1

    def count_timer(self, count: int):
        if self.running:
            count_text = strftime("%M:%S", gmtime(count))
            self.canvas.itemconfig(self.timer_text, text=count_text )
            if count > 0:
                self.window.after(1000, self.count_timer, count - 1)
            if count == 0:
                self.mark_interval()
                self.counter += 1
                if self.counter < 9:
                    self.start_timer()
                else:
                    self.counter = 1
        else:
            self.counter = 1
            self.canvas.itemconfig(self.timer_text, text="00:00")

    def start_timer(self):
        self.running = True
        if self.counter == 8:
                self.count_timer(LONG_BREAK_MIN * 60)
                self.status.config(text= "LONG BREAK")
        elif self.counter % 2 == 1:
                self.count_timer(WORK_MIN * 60)
                self.status.config(text= "WORK")
        elif self.counter % 2 == 0:
                self.count_timer(SHORT_BREAK_MIN * 60)
                self.status.config(text = "SHORT BREAK")


    def reset_timer(self):
        self.running =False
        for checkmark in self.check_mark:
            checkmark.config(text="")
        self.status.config(text="")


    def mark_interval(self):
       if self.counter % 2 == 1:
            self.check_mark[self.ticks[self.counter]].config(text=self.TICK)

