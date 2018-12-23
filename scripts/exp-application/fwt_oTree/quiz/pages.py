from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants
import time
import math


# FIRST PAGE
#class enter_id(Page):
#    template_name = 'fwt/auxiliary/enter_id.html'
#    form_model = 'player'
#    form_fields = ['identity']
#
#
#class instructions(Page):
#    template_name = 'fwt/auxiliary/instructions.html'
#    pass
#
#
class timer_start(Page):
    template_name = 'fwt/auxiliary/timer_start.html'
    def before_next_page(self):
        # user has 5 minutes to complete as many pages as possible
        self.participant.vars['timer_start'] = time.time()
#        
#        
## PRACTICE TEXT AND QUESTION PAGES
#class practice_text(Page):
#    template_name = 'fwt/texts/practice_text.html'
#    def before_next_page(self):
#        # user has 5 minutes to complete as many pages as possible
#        self.participant.vars['reading_time_estimate'] = time.time() - self.participant.vars['timer_start']
#
#
## First text section
class text_1(Page):
    template_name = 'fwt/texts/text_1.html'
    def get_timeout_seconds(self):
        estimate = self.participant.vars['reading_time_estimate'] * 3 # multiplied by 3 because the main text sections have about 3x more words
        minutes = math.ceil(estimate / 60)
        return minutes * 60
#
## SECOND TEXT SECTION
#class text_2(Page):
#    template_name = 'fwt/texts/text_2.html'
#    def get_timeout_seconds(self):
#        estimate = self.participant.vars['reading_time_estimate'] * 3 # multiplied by 3 because the main text sections have about 3x more words
#        minutes = math.ceil(estimate / 60)
#        return minutes * 60
#    
#    # THIRD AND FINAL TEXT SECTION
#class text_3(Page):
#    template_name = 'fwt/texts/text_3.html'
#    def get_timeout_seconds(self):
#        estimate = self.participant.vars['reading_time_estimate'] * 3 # multiplied by 3 because the main text sections have about 3x more words
#        minutes = math.ceil(estimate / 60)
#        return minutes * 60




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
        

#class test_2(Page):
#    form_model = 'player'
#    form_fields = ['submitted_answer']
#
#    def submitted_answer_choices(self):
#        qd = self.player.current_question()
#        return [
#            qd['choice1'],
#            qd['choice2'],
#            qd['choice3'],
#            qd['choice4'],
#        ]
#
#    def before_next_page(self):
#        self.player.check_correct()
#        
#        
#class test_3(Page):
#    form_model = 'player'
#    form_fields = ['submitted_answer']
#
#    def submitted_answer_choices(self):
#        qd = self.player.current_question()
#        return [
#            qd['choice1'],
#            qd['choice2'],
#            qd['choice3'],
#            qd['choice4'],
#        ]
#
#    def before_next_page(self):
#        self.player.check_correct()




class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()
        return {
            'player_in_all_rounds': player_in_all_rounds,
            'questions_correct': sum([p.is_correct for p in player_in_all_rounds])
        }


page_sequence = [     
    Question,
    Results
]
