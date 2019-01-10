from ._builtin import Page
from .models import Constants
import time 
import math


class Question(Page):
    def is_displayed(self):
        return self.session.config['name'] == 'fwt'

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
        if self.session.config['name'] == 'fwt':
            return (self.round_number == Constants.num_rounds) & (self.participant.vars['give_feedback'])
        else:
            return False


    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()
        return {
            'player_in_all_rounds': player_in_all_rounds,
            'questions_correct': sum([p.is_correct for p in player_in_all_rounds])
        }

class get_ready(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    
    
    def vars_for_template(self):
        is_experiment = (self.session.config['name'] == 'fwt') 
        estimate = self.participant.vars['reading_time_estimate'] * 3 # multiplied by 3 because the main text sections have about 3x more words
        minutes = math.ceil(estimate / 60)
        
        if minutes == 1:
            koliko_min = " minutu"
        elif minutes > 4:
            koliko_min = " minuta"
        else:
            koliko_min = " minute"
            
        next_message = "Pritisnite 'Dalje' kako biste nastavili s čitanjem prvog teksta u glavnom dijelu istraživanja."

        
        practice_message = ["Sljedeći prikaz sadrži nešto duži tekst.",
                            "Sada Vam je vrijeme čitanja ograničeno na otprilike %s %s. \
                            Vaš zadatak je čitati tekst na jednak način i jednakom brzinom kao prethodni!" % (minutes, koliko_min),
                            "30 sekundi prije isteka vremena, na lijevoj strani ekrana prikazat će se\
                            okvir unutar kojega će se odbrojavati vrijeme do kraja.", 
                            "Pritisnite 'Dalje' kako biste nastavili s čitanjem drugog teksta."]
        
        
        if self.session.config['name'] == 'fwt':
            return {'is_exp': is_experiment, 'message': next_message}
        else:
            return {'is_exp': is_experiment, 'message': practice_message}


page_sequence = [timer_start, practice_text, Question, Results, get_ready]
