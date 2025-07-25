from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from login_screen import LoginScr
from main_screen import MainScr
from test_screen import TestScr
from results_screen import ResultScr


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScr())
        sm.add_widget(MainScr())
        sm.add_widget(TestScr())
        sm.add_widget(ResultScr())
        return sm
    
if __name__ == '__main__':
    app = MyApp()
    app.run()
