from time import strftime, gmtime
from math import floor
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
class Pomodoro:
    TICK = "✓"
    ticks ={1:0, 3:1, 5:2, 7:3}
    def __init__(self, canvas, timer_text, window, check_mark, timer):
        self.canvas = canvas
        self.timer_text = timer_text
        self.window = window
        self.check_mark = check_mark
        self.timer = timer
        self.counter = 1
        self.timer_window = None

    def count_timer(self, count: int):
            count_text = strftime("%M:%S", gmtime(count))
            self.canvas.itemconfig(self.timer_text, text=count_text )
            if count > 0:
                self.timer_window =self.window.after(1000, self.count_timer, count - 1)
            if count == 0:
                self.mark_interval()
                self.counter += 1
                if self.counter < 9:
                    self.start_timer()
                else:
                    self.counter = 1


    def start_timer(self):
        self.running = True
        if self.counter == 8:
                self.count_timer(LONG_BREAK_MIN * 60)
                self.timer.config(text= "LONG BREAK")
        elif self.counter % 2 == 1:
                self.count_timer(WORK_MIN * 60)
                self.timer.config(text= "WORK")
        elif self.counter % 2 == 0:
                self.count_timer(SHORT_BREAK_MIN * 60)
                self.timer.config(text = "SHORT BREAK")


    def reset_timer(self):
        self.window.after_cancel(self.timer_window)
        for checkmark in self.check_mark:
            checkmark.config(text="")
        self.timer.config(text="Timer")
        self.canvas.itemconfig(self.timer_text,text="00:00")


    def mark_interval(self):
       if self.counter % 2 == 1:
            self.check_mark[self.ticks[self.counter]].config(text=self.TICK)

