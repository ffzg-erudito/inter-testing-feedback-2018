from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants
import math


  
# THIRD AND FINAL TEXT SECTION
class text_3(Page):
    def is_displayed(self):
        return self.round_number == 1
    def get_timeout_seconds(self):
        estimate = self.participant.vars['reading_time_estimate'] * 3 # multiplied by 3 because the main text sections have about 3x more words
        minutes = math.ceil(estimate / 60)
        return minutes * 60



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
        

class Results(Page):

    
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        for x in self.participant.vars:
            print(x, self.participant.vars[x])
            
        player_in_all_rounds = self.player.in_all_rounds()
        return {
            'player_in_all_rounds': player_in_all_rounds,
            'questions_correct': sum([p.is_correct for p in player_in_all_rounds])
        }
        
class end_page(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    text_3,
    Question,
    Results,
    end_page
]
