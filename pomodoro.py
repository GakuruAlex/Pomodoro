from time import strftime, gmtime
class Pomodoro:
    TICK = "✓"
    def __init__(self, canvas, timer_text, window, check_mark):
        self.canvas = canvas
        self.timer_text = timer_text
        self.window = window
        self.check_mark = check_mark
   
    def count_timer(self, count: int):
        count_text = strftime("%M:%S", gmtime(count))
        self.canvas.itemconfig(self.timer_text, text=count_text )
        if count > 0:
            self.window.after(1000, self.count_timer, count - 1)
        if count == 0:
            self.mark_interval()
    def start_timer(self):
        self.count_timer(300)
    def mark_interval(self):
        self.check_mark.config(text=self.TICK)