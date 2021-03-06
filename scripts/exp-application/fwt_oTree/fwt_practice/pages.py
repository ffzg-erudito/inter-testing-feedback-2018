﻿from ._builtin import Page
from .models import Constants
import time 
import math
import os


class timer_instructions_0(Page):
#    form_model = 'player'
#    form_fields = ['predznanje']
#    
#    def predznanje_choices(self):
#        return [1, 2, 3, 4, 5, 6, 7]
    
    def is_displayed(self):
        return self.round_number == 1
    def before_next_page(self):
        # start timing the reading of the practice text
#        self.participant.vars['predznanje'] = self.player.predznanje
#        print(self.participant.vars['predznanje'])
        self.participant.vars['timer_start'] = time.time()



class practice_text(Page):
    def is_displayed(self):
        return self.round_number == 1
        
    def before_next_page(self):
        # estimate participant's reading time
        self.participant.vars['reading_time'] = time.time() - self.participant.vars['timer_start']
        
        # text filenames
        practice_text_filename = 'practice_text.txt'
        text_1_filename = 'text_1.txt'
        text_2_filename = 'text_2.txt'
        text_3_filename = 'text_3.txt'
        
        # text file paths relative to set working directory
        practice_text_path = os.path.join('..', '..', '..', 'texts', practice_text_filename)
        text_1_path = os.path.join('..', '..', '..', 'texts', text_1_filename)
        text_2_path = os.path.join('..', '..', '..', 'texts', text_2_filename)
        text_3_path = os.path.join('..', '..', '..', 'texts', text_3_filename)
        
        # import into variables
        with open(practice_text_path, 'r', newline = '', encoding='utf-8') as myfile:
            practice_text = myfile.read().replace('\n', '')
        with open(text_1_path, 'r', newline = '', encoding='utf-8') as myfile:
            text_1 = myfile.read().replace('\n', '')
        with open(text_2_path, 'r', newline = '', encoding='utf-8') as myfile:
            text_2 = myfile.read().replace('\n', '')
        with open(text_3_path, 'r', newline = '', encoding='utf-8') as myfile:
            text_3 = myfile.read().replace('\n', '')
            
        # lengths of texts
        length_practice = len(practice_text.split())
        length_text_1 = len(text_1.split())
        length_text_2 = len(text_2.split())
        length_text_3 = len(text_3.split())
        
        length_text_1/length_practice
        length_text_2/length_practice
        length_text_3/length_practice
        
        # multiply time spent reading first text by ratio of length of longest text over length of practice text - liberal estimate
        estimate = self.participant.vars['reading_time'] * (max(length_text_1, length_text_2, length_text_3)/length_practice) 
        
        # set reading time estimate in minutes and limit it
        self.participant.vars['reading_time_estimate'] = math.ceil(estimate / 60)
        if self.participant.vars['reading_time_estimate'] < 5:
           self.participant.vars['reading_time_estimate'] = 5
        elif self.participant.vars['reading_time_estimate'] > 8:
            self.participant.vars['reading_time_estimate'] = 8
        
        
class instructions_1(Page):
    
    def is_displayed(self):
        return self.round_number == 1
    
    def vars_for_template(self):
        
        if self.session.config['name'] == '1':
            message = ['Vaš sljedeći zadatak je odgovoriti na nekoliko pitanja vezanih za sadržaj pročitanog teksta.\
                       Pitanja su tipa višestrukog izbora, stoga označite onaj odgovor koji smatrate točnim\
                       te ga potvrdite pritiskom na tipku "Dalje". To će i automatski pokrenuti prikaz\
                       sljedećeg pitanja.',
                       'U glavnom dijelu istraživanja čitat ćete tri teksta. Nakon što pročitate prvi tekst,\
                       zadatak će Vam biti odgovoriti na nekoliko pitanja vezanih za sadržaj tog teksta koja će\
                       biti jednakog oblika. Isto tako ćete, nakon čitanja drugog teksta, odgovarati na pitanja\
                       vezana za sadržaj tog drugog teksta. Nakon toga ćete čitati treći tekst.',
                       'Sada Vas molimo da odgovorite na nekoliko pitanja vezanih za sadržaj prethodnog teksta.',
                       'Kada ste spremni započeti, pritisnite tipku "Dalje".']
        elif self.session.config['name'] == '2':
            message = ['Vaš sljedeći zadatak je odgovoriti na nekoliko pitanja općeg znanja.\
                       Pitanja su tipa višestrukog izbora, stoga označite onaj odgovor koji smatrate točnim\
                       te ga potvrdite pritiskom na tipku "Dalje". To će i automatski pokrenuti prikaz\
                       sljedećeg pitanja.',
                       'U glavnom dijelu istraživanja čitat ćete tri teksta. Nakon što pročitate prvi tekst,\
                       zadatak će Vam biti odgovoriti na nekoliko pitanja općeg znanja koja će biti jednakog\
                       oblika. Isto tako ćete, nakon čitanja drugog teksta, odgovarati na pitanja općeg znanja.\
                       Nakon toga ćete čitati treći tekst.',
                       'Sada Vas molimo da odgovorite na nekoliko pitanja općeg znanja.',
                       'Kada ste spremni započeti, pritisnite tipku "Dalje".']
        elif self.session.config['name'] == '3':
            message = ['Vaš sljedeći zadatak je još jednom pročitati tekst koji ste upravo pročitali.\
                       Sada Vam je vrijeme čitanja ograničeno na otprilike %s minuta. Tekst čitajte na jednak\
                       način i jednakom brzinom kao i prvi put jer ćete imati dovoljno vremena!' % (self.participant.vars['reading_time_estimate']),
                       '30 sekundi prije isteka vremena, na lijevoj strani ekrana prikazat će se\
                       okvir unutar kojega će se odbrojavati vrijeme do kraja.',
                       'U glavnom dijelu istraživanja čitat ćete tri teksta. Nakon što pročitate prvi tekst,\
                       zadatak će Vam biti pročitati ga još jednom. Isto tako ćete, nakon čitanja drugog teksta,\
                       još jednom pročitati taj drugi tekst. Nakon toga ćete čitati treći tekst.',
                       'Kada ste spremni započeti, pritisnite tipku "Dalje".']
               
        return {
            'rereading': (self.session.config['name'] == '3'),
            'message': message
        }




class question(Page):
    def is_displayed(self):
        return (self.session.config['name'] in ['1', '2']) & (self.round_number < 5)

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
        question_id = 'practice_for_activity_' + str(self.player.question_id)
        if self.player.is_correct:
            self.participant.vars[question_id] = 1
        else:
            self.participant.vars[question_id] = 0

        print(question_id, self.participant.vars[question_id])
 
        
    def vars_for_template(self):
        num_questions = 4
        return {'num_questions': num_questions}



class practice_text_rep(Page):
    def is_displayed(self):
        return (self.session.config['name'] == '3') & (self.round_number == Constants.num_rounds - 4)
    
    def get_timeout_seconds(self):
        return self.participant.vars['reading_time_estimate'] * 60

    


class instructions_2(Page):
    def is_displayed(self):
        return (self.round_number == Constants.num_rounds - 4) & (self.participant.vars['give_feedback'])
    
    def vars_for_template(self):
        message = ['Treći dio sadrži povratnu informaciju o točnosti Vaših odgovora na prethodna pitanja.\
                   Tablica u prvom stupcu sadrži pitanje, u drugom Vaš odgovor, i u trećem točan odgovor.\
                   Zelenom bojom bojom označena su pitanja na koja ste točno odgovorili, a crvenom bojom\
                   pitanja na koja niste točno odgovorili.',
                   'Dobro proučite povratne informacije. Nakon 10 sekundi, prikazat će se tipka "Dalje",\
                   te ćete moći pritiskom na nju pokrenuti nastavak postupka. Postupak će se automatski\
                   nastaviti nakon 20 sekundi.',
                   'Pritisnite tipku "Dalje" kako biste vidjeli povratne informacije.']
               
        return {'message': message}




class results(Page):
    def is_displayed(self):
        if self.session.config['name'] in ['1','2']:
            return (self.round_number == Constants.num_rounds - 4) & (self.participant.vars['give_feedback'])
        else:
            return False
        
    def get_timeout_seconds(self):
            return 20  
        
    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()
        num_questions = 4
        return {
            'num_questions': num_questions,
            'player_in_all_rounds': player_in_all_rounds,
            'questions_correct': sum([p.is_correct for p in player_in_all_rounds])
        }
        
        
        
    
class instructions_3(Page):
    def is_displayed(self):
        return (self.session.config['name'] in ['1', '2', '3']) & (self.round_number == Constants.num_rounds - 4)
        
    def vars_for_template(self):
        if self.session.config['name'] is '1':
            rereading = False
            message = ['U glavnom dijelu istraživanja čitat ćete tri teksta. Nakon prvog, a onda i nakon drugog teksta,\
                       također ćete odgovarati na pitanja vezana za sadržaj pročitanog teksta koja će biti jednakog oblika\
                       kao ova na koja ste upravo odgovarali.',
                       'Nakon čitanja trećeg teksta, odgovarat ćete na pitanja koja će obuhvaćati sadržaj sva tri pročitana\
                       teksta. ',
                       'Pitanja su ponovno tipa višestrukog izbora, stoga označite onaj odgovor koji smatrate točnim\
                       te ga potvrdite pritiskom na tipku "Dalje". To će i automatski pokrenuti prikaz sljedećeg pitanja.',
                       'Pritisnite tipku "Dalje" kako biste dobili završnu uputu.']
        elif self.session.config['name'] is '2':
            rereading = False
            message = ['U glavnom dijelu istraživanja čitat ćete tri teksta. Nakon prvog, a onda i nakon drugog teksta,\
                       također ćete odgovarati na pitanja općeg znanja koja će biti jednakog oblika kao ova na koja ste\
                       upravo odgovarali.',
                       'Nakon čitanja trećeg teksta, odgovarat ćete na pitanja koja će obuhvaćati sadržaj sva tri pročitana\
                       teksta. ',
                       'Sada Vas molimo da odgovorite na nekoliko pitanja vezanih za sadržaj prethodnog teksta kako biste se\
                       upoznali s oblikom pitanja u završnom dijelu. Pitanja su ponovno tipa višestrukog izbora, stoga označite\
                       onaj odgovor koji smatrate točnim te ga potvrdite pritiskom na tipku "Dalje". To će i automatski pokrenuti\
                       prikaz sljedećeg pitanja.',
                       'Kada ste spremni započeti, pritisnite tipku "Dalje".']
        else:
            rereading = True
            message = ['U glavnom dijelu istraživanja čitat ćete tri teksta. Nakon što jednom pročitate prvi tekst, \
                       zadatak će Vam biti pročitati ga još jednom. Isto tako ćete dva puta pročitati i drugi tekst.',
                       'Nakon čitanja trećeg teksta, odgovarat ćete na pitanja koja će obuhvaćati sadržaj sva tri pročitana\
                       teksta. ',
                       'Pitanja su tipa višestrukog izbora, stoga označite onaj odgovor koji smatrate točnim te ga\
                       potvrdite pritiskom na tipku "Dalje". To će i automatski pokrenuti prikaz sljedećeg pitanja.',
                       'Sada Vas molimo da odgovorite na nekoliko pitanja vezanih za sadržaj prethodnog teksta kako biste se\
                       upoznali s oblikom pitanja u završnom dijelu.',
                       'Kada ste spremni započeti, pritisnite tipku "Dalje".']
            
            # because whether giving feedback determines the number of "parts" of a single taks, here, depending
            # on whether feedback is given, a variable is returned to the template that specifies the label of the
            # final part of the instructions
            
        if self.participant.vars['give_feedback'] is True:
            instr_3_title = 'Završni dio'
        else:
            instr_3_title = 'Završni dio'
        
        return {
            'message': message,
            'title': instr_3_title,
            'rereading': rereading
        }
        





class question_genKnowledge_rereading(Page):
    def is_displayed(self):
        return (self.session.config['name'] in ['2', '3']) & (self.round_number > Constants.num_rounds - 4)
    
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
        
        
    def vars_for_template(self):
        q_num = self.round_number - 4
        
        return {'q_num': q_num}
        

    def before_next_page(self):
        self.player.check_correct()
        question_id = 'practice_for_final_' + str(self.player.question_id)
        if self.player.is_correct:
            self.participant.vars[question_id] = 1
        else:
            self.participant.vars[question_id] = 0

        print(question_id, self.participant.vars[question_id])






class get_ready(Page):
    
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    
    
    def vars_for_template(self):
        is_experiment = (self.session.config['name'] is not 'proba')
#        if self.session.config['name'] is '1':
#            is_content = True
#            is_gk = False
#            is_rereading = False
#        elif self.session.config['name'] is '2':
#            is_content = False
#            is_gk = True
#            is_rereading = False
#        else:
#            is_content = False
#            is_gk = False
#            is_rereading = True
            
        if (self.session.config['name'] in ['1', '2']) & (self.participant.vars['give_feedback'] == True):
            message = ['Slijedi glavni dio istraživanja u kojemu ćete proći kroz tri teksta o korovima.\
                        Nakon prvog, a onda i nakon drugog teksta, odgovarat ćete na pitanja poput onih\
                        s kojima ste se upravo upoznali, ',
                        'a nakon zadnjeg teksta ćete odgovarati na pitanja koja će obuhvaćati sadržaj sva tri\
                        pročitana teksta.',
                        'Tekstovi će biti otprilike jednake dužine, a vrijeme čitanja ograničeno na otprilike %s minuta.\
                        Tekstove čitajte na jednak način i jednakom brzinom kao ovaj koji ste upravo čitali jer ćete imati\
                        dovoljno vremena! 30 sekundi prije isteka vremena za čitanje, na lijevoj strani ekrana prikazat će se\
                        okvir unutar kojega će se odbrojavati vrijeme do kraja prikaza teksta.' % (self.participant.vars['reading_time_estimate']),
                        'Vrijeme za proučavanje povratne informacije produženo je. 40 sekundi od početka prikaza\
                        povratne informacije, pojavit će se tipka "Dalje" pri dnu tablice. Pritiskom na nju možete sami\
                        pokrenuti nastavak postupka. Nakon što prođe još 20 sekundi (od prikaza tipke "Dalje"), program\
                        će automatski pokrenuti nastavak postupka. Ukupno, dakle, imate 1 minutu za proučavanje povratne\
                        informacije. Molimo Vas, proučite povratne informacije o točnosti Vaših odgovora jer ćete nakon čitanja\
                        trećeg teksta odgovarati na pitanja koja će se odnositi na sva tri teksta.',
                        'Molimo Vas da zadatke rješavate najbolje što možete. Daljnjih specifičnih uputa neće biti.\
                        Ako imate bilo kakvih pitanja, sada ih postavite eksperimentatoru.', 
                        "Pritisnite 'Dalje' kako biste počeli čitati prvi tekst u glavnom dijelu postupka."]
            
        elif (self.session.config['name'] in ['1', '2']) & (self.participant.vars['give_feedback'] == False):
            message = ['Slijedi glavni dio istraživanja u kojemu ćete proći kroz tri teksta o korovima.\
                        Nakon prvog, a onda i nakon drugog teksta, odgovarat ćete na pitanja poput onih\
                        s kojima ste se upravo upoznali, ',
                        'a nakon zadnjeg teksta ćete odgovarati na pitanja koja će obuhvaćati sadržaj sva tri\
                        pročitana teksta.',
                        'Tekstovi će biti otprilike jednake dužine, a vrijeme čitanja ograničeno na otprilike %s minuta.\
                        Tekstove čitajte na jednak način i jednakom brzinom kao ovaj koji ste upravo čitali jer ćete imati\
                        dovoljno vremena! 30 sekundi prije isteka vremena za čitanje, na lijevoj strani ekrana prikazat će se\
                        okvir unutar kojega će se odbrojavati vrijeme do kraja prikaza teksta.' % (self.participant.vars['reading_time_estimate']),
                        'Molimo Vas da zadatke rješavate najbolje što možete. Daljnjih specifičnih uputa neće biti.\
                        Ako imate bilo kakvih pitanja, sada ih postavite eksperimentatoru.', 
                        "Pritisnite 'Dalje' kako biste počeli čitati prvi tekst u glavnom dijelu postupka."]
        else:
            message = ['Slijedi glavni dio istraživanja u kojemu ćete proći kroz tri teksta o korovima. Nakon što jednom\
                       pročitate prvi tekst, zadatak će Vam biti pročitati ga još jednom. Isto tako ćete dva puta pročitati\
                       i drugi tekst, ',
                       'a nakon zadnjeg teksta ćete odgovarati na pitanja koja će obuhvaćati sadržaj sva tri\
                       pročitana teksta.',
                       'Tekstovi će biti otprilike jednake dužine, a vrijeme čitanja ograničeno na otprilike %s minuta.\
                        Tekstove čitajte na jednak način i jednakom brzinom kao ovaj koji ste upravo čitali jer ćete imati\
                        dovoljno vremena! 30 sekundi prije isteka vremena za čitanje, na lijevoj strani ekrana prikazat će se\
                        okvir unutar kojega će se odbrojavati vrijeme do kraja prikaza teksta.' % (self.participant.vars['reading_time_estimate']),
                       'Molimo Vas da zadatke rješavate najbolje što možete. Daljnjih specifičnih uputa neće biti.\
                       Ako imate bilo kakvih pitanja, sada ih postavite eksperimentatoru.', 
                       "Pritisnite 'Dalje' kako biste počeli čitati prvi tekst u glavnom dijelu postupka."]
                

        practice_message = ["Sljedeći prikaz sadrži nešto duži tekst.",
                            "Sada Vam je vrijeme čitanja ograničeno na otprilike %s minuta. \
                            Vaš zadatak je čitati tekst na jednak način i jednakom brzinom kao prethodni!" % (self.participant.vars['reading_time_estimate']),
                            "30 sekundi prije isteka vremena, na lijevoj strani ekrana prikazat će se\
                            okvir unutar kojega će se odbrojavati vrijeme do kraja.", 
                            "Pritisnite 'Dalje' kako biste počeli čitati drugi tekst."]
        
        
        if self.session.config['name'] == 'proba':
            return {'is_exp': is_experiment, 'message': practice_message}
        else:
            return {'is_exp': is_experiment, 
                    'feedback': self.participant.vars['give_feedback'],
                    'message': message}             




page_sequence = [timer_instructions_0, practice_text, instructions_1, question, practice_text_rep, instructions_2, results, instructions_3, question_genKnowledge_rereading, get_ready]
