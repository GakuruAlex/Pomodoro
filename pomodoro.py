
class Pomodoro:
    def __init__(self, canvas, timer_text, window):
        self.canvas = canvas
        self.timer_text = timer_text
        self.window = window
   
    def count_timer(self, count: int):
        self.canvas.itemconfig(self.timer_text, text=count )
        if count > 0:
            self.window.after(1000, self.count_timer, count - 1)
    def start_timer(self):
        self.count_timer(5)