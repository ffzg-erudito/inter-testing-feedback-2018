from ._builtin import Page
from .models import Constants

  
# THIRD AND FINAL TEXT SECTION
class text_3(Page):
    def is_displayed(self):
        return self.round_number == 1
    def get_timeout_seconds(self):
        return self.participant.vars['reading_time_estimate'] * 60



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
        return (self.round_number == Constants.num_rounds) & (self.participant.vars['give_feedback'])

    def get_timeout_seconds(self):
        return 60
    
    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()
        return {
            'player_in_all_rounds': player_in_all_rounds,
            'questions_correct': sum([p.is_correct for p in player_in_all_rounds])
        }
        
        
        
class end_page(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [text_3, Question, Results, end_page]