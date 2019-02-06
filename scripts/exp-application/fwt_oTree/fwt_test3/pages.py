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
        self.player.check_answer()
        question_id = 'content_3_' + str(self.player.question_id)
        intrusor_id = 'isIntrusor_3_' + str(self.player.question_id)
        
        if self.player.is_correct:
            self.participant.vars[question_id] = 1
            self.participant.vars[intrusor_id] = 0

        else:
            self.participant.vars[question_id] = 0
            if self.player.is_intrusor:
                self.participant.vars[intrusor_id] = 1
            else:
                self.participant.vars[intrusor_id] = 0
             

        print(question_id, self.participant.vars[question_id], self.participant.vars[intrusor_id])
        


# class Results(Page):
#    def is_displayed(self):
#        return (self.round_number == Constants.num_rounds) & (self.participant.vars['give_feedback'])
#
#    def get_timeout_seconds(self):
#        return 60
#    
#    def vars_for_template(self):
#        player_in_all_rounds = self.player.in_all_rounds()
#        return {
#            'player_in_all_rounds': player_in_all_rounds,
#            'questions_correct': sum([p.is_correct for p in player_in_all_rounds])
#        }


class koliko_procitao(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    
    def vars_for_template(self):
        if self.session.config['name'] in ['1', '2']:
            message = ['Molimo Vas da za svaki od tri dijela procijenite koliko ste teksta uspjeli pročitati prije nego\
                       što je program automatski pokrenuo sljedeću stranicu.']
        else:
            message = ['Molimo Vas da za svaki od tri dijela procijenite koliko ste teksta uspjeli pročitati tijekom prvog\
                       od dva čitanja prije nego što je program automatski pokrenuo sljedeću stranicu.']
        
        return {'message': message}
    
    
    form_model = 'player'
    form_fields = ['text1', 'text2', 'text3']

    def text1_choices(self):
        return ['nisam uspjela/uspio pročitati do kraja ili sam žurila/žurio da bih pročitala/pročitao',
                'jednom cijeli tekst',
                'jednom cijeli tekst i preletjeti "ključne" dijelove',
                'oko jedan i pol put',
                'više nego jednom, ali nešto manje od jedan i pol put',
                'više od jedan i pol put, ali manje od dva puta',
                'dva ili više puta']

    def text2_choices(self):
         return ['nisam uspjela/uspio pročitati do kraja ili sam žurila/žurio da bih pročitala/pročitao',
                'jednom cijeli tekst',
                'jednom cijeli tekst i preletjeti "ključne" dijelove',
                'oko jedan i pol put',
                'više nego jednom, ali nešto manje od jedan i pol put',
                'više od jedan i pol put, ali manje od dva puta',
                'dva ili više puta']
         
         
    def text3_choices(self):
        return ['nisam uspjela/uspio pročitati do kraja ili sam žurila/žurio da bih pročitala/pročitao',
                'jednom cijeli tekst',
                'jednom cijeli tekst i preletjeti "ključne" dijelove',
                'oko jedan i pol put',
                'više nego jednom, ali nešto manje od jedan i pol put',
                'više od jedan i pol put, ali manje od dva puta',
                'dva ili više puta']
        
        
    def before_next_page(self):
        self.participant.vars['koliko_procitao_text1'] = self.player.text1
        self.participant.vars['koliko_procitao_text2'] = self.player.text2
        self.participant.vars['koliko_procitao_text3'] = self.player.text3
        
        


        
        
class end_page(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    
    def get_timeout_seconds(self):
        return 3
    
    def before_next_page(self):
        
        # save data to .csv in /inter-testing-feedback-2018/results/        
        results_file_exists = os.path.exists('../../../results/results.csv')
        writefile = '../../../results/results.csv'
        
        data_to_store = self.participant.vars    
        
        fieldnames = ['when', 'participant_code', 'spol', 'dob', 'predznanje', 'give_feedback', 'condition', 
              'timer_start', 'reading_time', 'reading_time_estimate', 
              'koliko_procitao_text1', 'koliko_procitao_text2', 'koliko_procitao_text3',
              'practice_1', 'practice_2', 'practice_3', 'practice_4', 'practice_5', 'practice_6', 'practice_7', 'practice_8',              'genKnowledge_1_1', 'genKnowledge_1_2', 'genKnowledge_1_3', 'genKnowledge_1_4', 'genKnowledge_1_5', 
              'genKnowledge_1_6', 'genKnowledge_1_7', 'genKnowledge_1_8', 'genKnowledge_1_9', 'genKnowledge_1_10',
              'genKnowledge_2_1', 'genKnowledge_2_2', 'genKnowledge_2_3', 'genKnowledge_2_4', 'genKnowledge_2_5', 
              'genKnowledge_2_6', 'genKnowledge_2_7', 'genKnowledge_2_8', 'genKnowledge_2_9', 'genKnowledge_2_10',
              'content_1_1', 'content_1_2', 'content_1_3', 'content_1_4', 'content_1_5', 'content_1_6', 'content_1_7',
              'content_1_8', 'content_1_9', 'content_1_10', 'content_2_1', 'content_2_2', 'content_2_3', 'content_2_4',
              'content_2_5', 'content_2_6', 'content_2_7', 'content_2_8', 'content_2_9', 'content_2_10',
              'content_3_1', 'content_3_2', 'content_3_3', 'content_3_4', 'content_3_5', 'content_3_6', 'content_3_7',
              'content_3_8', 'content_3_9', 'content_3_10', 'content_3_11', 'content_3_12', 'content_3_13', 'content_3_14',
              'content_3_15', 'content_3_16', 'content_3_17', 'content_3_18', 'content_3_19', 'content_3_20',
              'isIntrusor_2_1', 'isIntrusor_2_2', 'isIntrusor_2_3', 'isIntrusor_2_4', 'isIntrusor_2_5', 'isIntrusor_2_6',
              'isIntrusor_2_7', 'isIntrusor_2_8', 'isIntrusor_2_9', 'isIntrusor_2_10',
              'isIntrusor_3_1', 'isIntrusor_3_2', 'isIntrusor_3_3', 'isIntrusor_3_4', 'isIntrusor_3_5', 'isIntrusor_3_6',
              'isIntrusor_3_7', 'isIntrusor_3_8', 'isIntrusor_3_9', 'isIntrusor_3_10', 'isIntrusor_3_11', 'isIntrusor_3_12',
              'isIntrusor_3_13', 'isIntrusor_3_14', 'isIntrusor_3_15', 'isIntrusor_3_16', 'isIntrusor_3_17',
              'isIntrusor_3_18', 'isIntrusor_3_19', 'isIntrusor_3_20']
        
        
        with open(writefile, 'a', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, restval = None, fieldnames = fieldnames, lineterminator = '\n')
        
            if not results_file_exists:
                writer.writeheader()
                writer.writerow(data_to_store)
            else:
                writer.writerow(data_to_store)
        

        print(data_to_store)
        


    

# page_sequence = [text_3, Question, Results, end_page]

page_sequence = [text_3, Question, koliko_procitao, end_page]
