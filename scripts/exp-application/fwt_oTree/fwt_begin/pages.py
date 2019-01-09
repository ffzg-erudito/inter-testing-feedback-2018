from ._builtin import Page
from .models import Constants
import random


# FIRST PAGE
class enter_id(Page):
    form_model = 'player'
    form_fields = ['identity']
    def before_next_page(self):
        self.participant.vars['identity'] = self.player.identity
        self.participant.vars['give_feedback'] = random.choice([True, False])
        print('Give feedback? ' + str(self.participant.vars['give_feedback']))


class instructions(Page):
    pass



page_sequence = [
    enter_id,
    instructions
]
