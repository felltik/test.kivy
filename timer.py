from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProperty

class Timer(Label):
    done = BooleanProperty(False)
    def __init__(self, total=5, **kwargs):
        super().__init__(**kwargs)
        self.total = total
        self.current = 0
        self.text = '0s'
        self.event = None

    def restart(self, total=5):
        if self.event:
            self.event.cancel()
        self.total = total
        self.current = 0
        self.text = '0s'
        self.done = False
        self.start()

    def start(self):
        self.event = Clock.schedule_interval(self.change, 1)
    
    def change(self, dt):
        self.current += 1
        self.text = str(self.current) + 's'
        if self.current >= self.total:
            self.done = True
            return False