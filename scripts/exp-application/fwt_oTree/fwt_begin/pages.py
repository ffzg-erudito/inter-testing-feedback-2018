from ._builtin import Page
import random


# participant has to enter ID - to be implemented: check whether ID conforms to required format
class enter_id(Page):
    form_model = 'player'
    form_fields = ['identity']
    def before_next_page(self):
        self.participant.vars['identity'] = self.player.identity
        if self.session.config['name'] in ['1','2']:
            self.participant.vars['give_feedback'] = random.choice([True, False])
        else:
            self.participant.vars['give_feedback'] = False
        print(self.session.config['app_sequence'],'Give feedback? ' + str(self.participant.vars['give_feedback']))
        
# initial instructions        
class init_instructions(Page):
    pass


page_sequence = [
    enter_id,
    init_instructions
]
