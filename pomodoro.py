from time import strftime, gmtime
class Pomodoro:
    def __init__(self, canvas, timer_text, window):
        self.canvas = canvas
        self.timer_text = timer_text
        self.window = window
   
    def count_timer(self, count: int):
        count_text = strftime("%M:%S", gmtime(count))
        self.canvas.itemconfig(self.timer_text, text=count_text )
        if count > 0:
            self.window.after(1000, self.count_timer, count - 1)
    def start_timer(self):
        self.count_timer(300)