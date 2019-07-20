from ._builtin import Page
from .models import Constants


## FIRST TEXT SECTION
class text_1(Page):
    def get_timeout_seconds(self):
        return self.participant.vars['reading_time_estimate'] * 60


class inter(Page):
    def get_timeout_seconds(self):
        return 20


class text_1_rep(Page):
    template_name = 'fwt_reread1/text_1.html'
    def get_timeout_seconds(self):
        return self.participant.vars['reading_time_estimate'] * 60

class get_ready(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    
    def vars_for_template(self):
        is_experiment = (self.session.config['name'] in ['1', '2', '3']) 
        instruction = "This is the instruction, in case the experiment is taking place"
        next_message = "Pritisnite 'Dalje' kako biste počeli čitati sljedeći tekst."
        exit_message = "Kraj!"
        if is_experiment:
            return {'is_exp': is_experiment, 'message': next_message, 'instruction': instruction}
        else:
            return {'is_exp': is_experiment, 'message': exit_message}


page_sequence = [text_1, inter, text_1_rep, get_ready]