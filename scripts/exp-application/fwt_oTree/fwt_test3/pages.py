from ._builtin import Page
from .models import Constants
import csv
import os


  
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
        question_id = 'c_3.' + str(self.player.question_id)
        self.participant.vars[question_id] = self.player.is_correct
        # self.participant.
        print(question_id, self.participant.vars[question_id])
        


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
    
    def get_timeout_seconds(self):
        return 5
    
    def before_next_page(self):
        
    #        data_to_store = [self.participant.vars['participant_code'], self.participant.vars['spol'], self.participant.vars['dob'], self.participant.vars['predznanje']]
        data_to_store = self.participant.vars
        print(data_to_store)
            
            # output = open('result.xls', 'w+')
            
            
    #        excel_writer = pd.ExcelWriter('result.xls')
    #        data_to_store.to_excel(excel_writer, 'Sheet1', index = False)
    #        excel_writer.save()
    #        
    
        writefile = '../../../results/results.csv'
        fieldnames = [*data_to_store]
        values = data_to_store.values()
        with open( writefile, 'a' ) as f:
            writer = csv.writer(f, lineterminator = '\n')
            
            if os.path.exists('../../../results/results.csv'):
                writer.writerow(values)
            else:
                writer.writerow(fieldnames)
                writer.writerow(values)


    

page_sequence = [text_3, Question, Results, end_page]