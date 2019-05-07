from ._builtin import Page
from .models import Constants

## FIRST TEXT SECTION
class text_2(Page):
    def get_timeout_seconds(self):       
        return self.participant.vars['reading_time_estimate'] * 60


class inter(Page):
    def get_timeout_seconds(self):
        return 20


class text_2_rep(Page):
    template_name = 'fwt_reread2/text_2.html'
    def get_timeout_seconds(self):
        return self.participant.vars['reading_time_estimate'] * 60


class get_ready(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    
    def vars_for_template(self):
        session_type = self.session.config['name']
        is_experiment = (self.session.config['name'] == 'fwt') 
        instruction = "This is the instruction, in case the experiment is taking place"
        next_message = "Pritisnite 'Dalje' kako biste nastavili sa sljedećim tekstom."
        exit_message = "Kraj!"
        if session_type == 'fwt':
            return {'is_exp': is_experiment, 'message': next_message, 'instruction': instruction}
        else:
            return {'is_exp': is_experiment, 'message': exit_message}


page_sequence = [text_2, inter, text_2_rep, get_ready]