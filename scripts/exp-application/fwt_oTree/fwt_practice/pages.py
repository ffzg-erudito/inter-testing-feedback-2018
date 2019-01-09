from ._builtin import Page
from .models import Constants
import time
from pandas import DataFrame


class Question(Page):
    form_model = 'player'
    form_fields = ['submitted_answer']

    def submitted_answer_choices(self):
        qd = self.player.current_question()
        return [
            qd['choice1'],
            qd['choice2'],
            qd['choice3'],
            qd['choice4'],
        ]

    def before_next_page(self):
        self.player.check_correct()
        self.participant.vars[str(self.player.question_id)] = self.player.is_correct
        print(str(self.player.question_id), self.participant.vars[str(self.player.question_id)])

class timer_start(Page):
    def is_displayed(self):
        return self.round_number == 1
    def before_next_page(self):
        # user has 5 minutes to complete as many pages as possible
        self.participant.vars['timer_start'] = time.time()

      
## PRACTICE TEXT AND QUESTION PAGES
class practice_text(Page):
    def is_displayed(self):
        return self.round_number == 1
    def before_next_page(self):
        # user has 5 minutes to complete as many pages as possible
        self.participant.vars['reading_time_estimate'] = time.time() - self.participant.vars['timer_start']


class Results(Page):
    def is_displayed(self):
        return (self.round_number == Constants.num_rounds) & (self.participant.vars['give_feedback'])


    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()
        return {
            'player_in_all_rounds': player_in_all_rounds,
            'questions_correct': sum([p.is_correct for p in player_in_all_rounds])
        }

class get_ready(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [timer_start, practice_text, Question, Results, get_ready]