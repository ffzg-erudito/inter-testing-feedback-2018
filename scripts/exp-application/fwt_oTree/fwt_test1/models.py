from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv

author = 'Your name here'

doc = """
A quiz app that reads its questions from a spreadsheet
(see quiz.csv in this directory).
There is 1 question per page; the number of pages in the game
is determined by the number of questions in the CSV.
See the comment below about how to randomize the order of pages.
"""

#def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
#    csv_reader = csv.reader(utf8_data, dialect = dialect, **kwargs)
#    for row in csv_reader:
#        yield [unicode(cell, 'utf-8') for cell in row]
#     

#with open('C:/Users/Matej/inter-testing-feedback-2018/scripts/exp-application/fwt_oTree/fwt_practice/test0.csv', encoding = 'utf8') as questions_file:
#    practice_questions = list(csv.DictReader(questions_file))

class Constants(BaseConstants):
    name_in_url = 'test1'
    players_per_group = None

    with open('fwt_test1/test1.csv', encoding = 'utf8') as questions_file:
        test1_questions = list(csv.DictReader(questions_file))

    num_rounds = len(test1_questions)
    

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.session.vars['test1_questions'] = Constants.test1_questions.copy()
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


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question_id = models.IntegerField()
    question = models.StringField()
    solution = models.StringField()
    submitted_answer = models.StringField(widget=widgets.RadioSelect)
    is_correct = models.BooleanField()
    feedback = models.StringField()

    def current_question(self):
        return self.session.vars['test1_questions'][self.round_number - 1]

    def check_correct(self):
        self.is_correct = (self.submitted_answer == self.solution)
        if self.is_correct:
            self.feedback = "Točno"
        else:
            self.feedback = "Netočno" 
