from const import *
from time import time
from random import randint


class User:
    def __init__(self, username):
        self.username = username
        self.time = 0
        self.score = 0
        self.questions = None
        self.total = None
        self.current_question = None
        self.answered = 0

    def set_questions(self, qs=QS):
        self.questions = qs
        self.total = len(qs)
        self.current_question = randint(0, len(qs) - 1)

    def next_question(self):
        self.answered += 1
        if self.answered == self.total:
            self.current_question = -1
        elif self.current_question < self.total - 1:
            self.current_question += 1
        else:
            self.current_question = 0

    def start_test(self):
        self.time = time()
        self.score = 0
        self.answered = 0

    def end_test(self):
        end = time()
        self.time = round(end - self.time, 2)