from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ObjectProperty



class MainScr(Screen):
    def __init__(self, name='main'):
        super().__init__(name=name)

        self.user = ObjectProperty()

        title_txt = Label(text='Main page')
        # self.username_txt = Label(text=f'User: {self.user.username}')
        self.username_txt = Label(text='User: ')
        self.stats_txt = Label(text='Statistics:')
        next_btn = Button(text='Start test')
        next_btn.on_press = self.next
        back_btn = Button(text='Back')
        back_btn.on_press = self.back

        btns_line = BoxLayout()
        btns_line.add_widget(next_btn)
        btns_line.add_widget(back_btn)

        main_line = BoxLayout(orientation='vertical')
        main_line.add_widget(title_txt)
        main_line.add_widget(self.username_txt)
        main_line.add_widget(self.stats_txt)
        main_line.add_widget(btns_line)
        self.add_widget(main_line)

    def on_enter(self):  # Этот метод вызывается при переходе на экран
        if self.user:
            username = self.user.username
            self.username_txt.text = 'User: ' + username
            self.stats_txt.text = f'Statistics: {self.user.score}/{self.user.time} s'

    def next(self):
        self.user.start_test()
        self.user.set_questions()
        next_scr = 'test'
        self.manager.get_screen(next_scr).user = self.user
        self.manager.transition.direction = 'left'
        self.manager.current = next_scr
    
    def back(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'login'
