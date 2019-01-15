from ._builtin import Page
import random
import re



# participant has to enter ID - to be implemented: check whether ID conforms to required format
class enter_id(Page):
    form_model = 'player'
    form_fields = ['participant_code', 'dob', 'spol']
    
    def before_next_page(self):
        self.participant.vars['participant_code'] = self.player.participant_code.upper()
        print(self.participant.vars['participant_code'])
        self.participant.vars['dob'] = self.player.dob
        self.participant.vars['spol'] = self.player.spol
        
        if self.session.config['name'] in ['1','2']:
            self.participant.vars['give_feedback'] = random.choice([True, False])
        else:
            self.participant.vars['give_feedback'] = False
        print(self.session.config['app_sequence'],'Give feedback? ' + str(self.participant.vars['give_feedback']))
        
        
    def spol_choices(self):
        return ['Ž', 'M']
    
    
    def error_message(self, values):
        pattern = re.compile('^[a-zA-Z]{4}[0-9]{2}$')
        if not bool(pattern.match(values['participant_code'])):
            return "Upisana šifra ne odgovara uputi za njenu konstrukciju!"
        
# initial instructions        
class init_instructions(Page):
    pass


page_sequence = [
    enter_id,
    init_instructions
]
