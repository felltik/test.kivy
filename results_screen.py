from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ObjectProperty


class ResultScr(Screen):
    def __init__(self, name='result'):
        super().__init__(name=name)

        self.user = ObjectProperty()

        title_txt = Label(text='Result')
        # self.username_txt = Label(text=f'User: {self.user.username}')
        self.username_txt = Label(text='User: ')
        self.result_txt = Label(text='Right:')
        self.time_txt = Label(text='Total time:')

        next_btn = Button(text='Main menu')
        next_btn.on_press = self.next

        main_line = BoxLayout(orientation='vertical')
        main_line.add_widget(title_txt)
        main_line.add_widget(self.username_txt)
        main_line.add_widget(self.result_txt)
        main_line.add_widget(self.time_txt)
        main_line.add_widget(next_btn)
        self.add_widget(main_line)

    def next(self):
        next_scr = 'main'
        self.manager.get_screen(next_scr).user = self.user
        self.manager.transition.direction = 'right'
        self.manager.current = next_scr

    def on_enter(self):
        if self.user:
            username = self.user.username
            self.username_txt.text = 'User: ' + username
            self.result_txt.text = f'Statistics: {self.user.score}/{self.user.total}'
            self.time_txt.text = f'Total time: {self.user.time} s'