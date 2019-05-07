from ._builtin import Page
import random
import re
import datetime



# participant has to enter ID
class enter_id(Page):
    form_model = 'player'
    form_fields = ['participant_code', 'dob', 'spol']
    
    def before_next_page(self):
        
        # set basic info
        self.participant.vars['when'] = str(datetime.datetime.now())
        self.participant.vars['participant_code'] = self.player.participant_code.upper()
        print(self.participant.vars['participant_code'])
        self.participant.vars['spol'] = self.player.spol
        self.participant.vars['dob'] = self.player.dob
        
        
        # set feedback
        if self.session.config['name'] in ['1','2']:
            self.participant.vars['give_feedback'] = random.choice([True, False])
        else:
            self.participant.vars['give_feedback'] = False
        print(self.session.config['app_sequence'],'Give feedback? ' + str(self.participant.vars['give_feedback']))
        
        
        # set condition name
        if self.session.config['name'] == '1':
            if self.participant.vars['give_feedback'] == False:
                self.participant.vars['condition'] = 'content_noFeedback'
            else:
                self.participant.vars['condition'] = 'content_feedback'
        elif self.session.config['name'] == '2':
            if self.participant.vars['give_feedback'] == False:
                self.participant.vars['condition'] = 'general_noFeedback'
            else:
                self.participant.vars['condition'] = 'general_feedback'
        else:
            self.participant.vars['condition'] = 'rereading'
              
        
    def spol_choices(self):
        return ['Ž', 'M']
    
    # check whether ID conforms to required format
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
