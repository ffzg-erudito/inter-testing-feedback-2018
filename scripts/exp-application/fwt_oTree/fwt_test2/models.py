from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)
import csv

author = 'Matej Pavlić'

doc = """
A quiz app that reads its questions from a spreadsheet
(see quiz.csv in this directory).
There is 1 question per page; the number of pages in the game
is determined by the number of questions in the CSV.
See the comment below about how to randomize the order of pages.
"""


class Constants(BaseConstants):
    name_in_url = 'test2'
    players_per_group = None

    with open('fwt_test2/test2.csv', encoding = 'utf8') as questions_file:
        test2_questions = list(csv.DictReader(questions_file))

    num_rounds = len(test2_questions)


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.session.vars['test2_questions'] = Constants.test2_questions.copy()
            ## ALTERNATIVE DESIGN:
            ## to randomize the order of the questions, you could instead do:

            # import random
            # randomized_questions = random.sample(Constants.questions, len(Constants.questions))
            # self.session.vars['questions'] = randomized_questions

            ## and to randomize differently for each participant, you could use
            ## the random.sample technique, but assign into participant.vars
            ## instead of session.vars.

        for p in self.get_players():
            question_data = p.current_question()
            p.question_id = int(question_data['id'])
            p.question = question_data['question']
            p.solution = question_data['solution']
            p.intrusor = question_data['intrusor']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question_id = models.IntegerField()
    question = models.StringField()
    solution = models.StringField()
    intrusor = models.StringField()
    submitted_answer = models.StringField(widget=widgets.RadioSelect)
    is_correct = models.BooleanField()
    is_intrusor = models.BooleanField()
    feedback = models.StringField()

    def current_question(self):
        return self.session.vars['test2_questions'][self.round_number - 1]

    def check_answer(self):
        self.is_correct = (self.submitted_answer == self.solution)
        self.is_intrusor = (self.submitted_answer == self.intrusor)

        if self.is_correct:
            self.feedback = u'\u2713'
        else:
            self.feedback = u'\u2717'