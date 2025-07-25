from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ObjectProperty

from random import shuffle

from const import *
from timer import Timer


class TestScr(Screen):
    def __init__(self, name='test'):
        super().__init__(name=name)
        self.answer = None
        self.user = ObjectProperty()

        self.timer_txt = Timer()
        self.timer_txt.bind(done=self.time_finished)
        self.counter_txt = Label(text='0 / ?')

        self.question_txt = Label(text='Question')
        # self.username_txt = Label(text=f'User: {self.user.username}')
        ans_1_btn = Button(text='1')
        ans_2_btn = Button(text='2')
        ans_3_btn = Button(text='3')
        ans_4_btn = Button(text='4')

        self.ans_btns = [ans_1_btn, ans_2_btn, ans_3_btn, ans_4_btn]
        for btn in self.ans_btns:
            btn.bind(on_press=self.callback)
    
        next_btn = Button(text='Next question')
        next_btn.on_press = self.next

        stats_line = BoxLayout()
        stats_line.add_widget(self.timer_txt)
        stats_line.add_widget(self.counter_txt)

        h_line_1 = BoxLayout()
        h_line_1.add_widget(ans_1_btn)
        h_line_1.add_widget(ans_2_btn)
        h_line_2 = BoxLayout()
        h_line_2.add_widget(ans_3_btn)
        h_line_2.add_widget(ans_4_btn)

        main_line = BoxLayout(orientation='vertical')
        main_line.add_widget(stats_line)
        main_line.add_widget(self.question_txt)
        main_line.add_widget(h_line_1)
        main_line.add_widget(h_line_2)
        main_line.add_widget(next_btn)
        self.add_widget(main_line)

    def ask(self):
        question: dict = self.user.questions[self.user.current_question]
        shuffle(self.ans_btns)
        self.ans_btns[0].text = question[RIGHT]
        self.ans_btns[1].text = question[WRONG][0]
        self.ans_btns[2].text = question[WRONG][1]
        self.ans_btns[3].text = question[WRONG][2]
        self.question_txt.text = question[TEXT]

    def on_enter(self):
        self.timer_txt.restart()
        self.counter_txt.text = str(self.user.answered + 1) + '/' + str(self.user.total)
        self.ask()

    def check_answer(self):
        if self.answer == self.ans_btns[0].text:
            self.user.score += 1

    def callback(self, instance): # кнопка, которая нажата
        for btn in self.ans_btns:
            btn.background_color = BTN_DEFAULT
        self.answer = instance.text
        instance.background_color = COLOR_BTN

    def next(self):
        if self.answer:
            self.timer_txt.done = False
            next_scr = 'test'
            self.check_answer()
            self.answer = None
            for btn in self.ans_btns:
                btn.background_color = BTN_DEFAULT
            self.user.next_question()
            self.counter_txt.text = f'{self.user.answered + 1}/{self.user.total}'
            if self.user.current_question == -1:
                self.user.end_test()
                next_scr = 'result'
                self.manager.get_screen(next_scr).user = self.user
                self.manager.transition.direction = 'left'
                self.manager.current = next_scr
            else:
                self.ask()

    def time_finished(self, *args):
        self.timer_txt.done = False
        self.answer = 'wrong answer'
        self.next()
        self.timer_txt.restart()