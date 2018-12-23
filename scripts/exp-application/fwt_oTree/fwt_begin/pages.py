from ._builtin import Page, WaitPage
from .models import Constants


# FIRST PAGE
class enter_id(Page):
    form_model = 'player'
    form_fields = ['identity']
    def before_next_page(self):
        self.participant.vars['identity'] = self.form_fields


class instructions(Page):
    pass



page_sequence = [
    enter_id,
    instructions
]
