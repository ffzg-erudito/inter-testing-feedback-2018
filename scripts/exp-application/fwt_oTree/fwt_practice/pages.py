from ._builtin import Page
from .models import Constants
import time 
import math


class timer_instructions_0(Page):
    def is_displayed(self):
        return self.round_number == 1
    def before_next_page(self):
        # start timing the reading of the practice text
        self.participant.vars['timer_start'] = time.time()




class practice_text(Page):
    def is_displayed(self):
        return self.round_number == 1
        
    def before_next_page(self):
        # estimate participant's reading time
        self.participant.vars['reading_time_estimate'] = time.time() - self.participant.vars['timer_start']
        
        
        
        
class instructions_1(Page):
    
    def is_displayed(self):
        return self.round_number == 1
    
    def vars_for_template(self):
        estimate = self.participant.vars['reading_time_estimate'] * 3 # multiplied by 3 because the main text sections have about 3x more words
        minutes = math.ceil(estimate / 60)
        
        if minutes == 1:
            koliko_min = " minutu"
        elif minutes > 4:
            koliko_min = " minuta"
        else:
            koliko_min = " minute"
        
        
        if self.session.config['name'] == '1':
            message = ['Vaš sljedeći zadatak je odgovoriti na nekoliko pitanja vezanih za sadržaj pročitanog teksta.\
                       Pitanja su tipa višestrukog izbora, stoga označite onaj odgovor koji smatrate točnim\
                       te ga potvrdite pritiskom na tipku "Dalje". To će i automatski pokrenuti prikaz\
                       sljedećeg pitanja.',
                       'U glavnom dijelu istraživanja čitat ćete tri teksta. Nakon prvog, a onda i nakon drugog teksta,\
                       također ćete odgovarati na pitanja vezana za sadržaj pročitanog teksta koja će biti jednakog oblika.',
                       'Sada ćete odgovoriti na nekoliko pitanja vezanih za sadržaj prethodnog teksta.',
                       'Kada ste spremni započeti, pritisnite tipku "Dalje".']
        elif self.session.config['name'] == '2':
            message = ['Vaš sljedeći zadatak je odgovoriti na nekoliko pitanja općeg znanja.\
                       Pitanja su tipa višestrukog izbora, stoga označite onaj odgovor koji smatrate točnim\
                       te ga potvrdite pritiskom na tipku "Dalje". To će i automatski pokrenuti prikaz\
                       sljedećeg pitanja.',
                       'U glavnom dijelu istraživanja čitat ćete tri teksta. Nakon prvog, a onda i nakon drugog teksta,\
                       također ćete odgovarati na pitanja općeg znanja koja će biti jednakog oblika.',
                       'Sada ćete odgovoriti na nekoliko pitanja općeg znanja.',
                       'Kada ste spremni započeti, pritisnite tipku "Dalje".']
        elif self.session.config['name'] == '3':
            message = ['Vaš sljedeći zadatak je još jednom pročitati tekst koji ste upravo pročitali.\
                       Sada Vam je vrijeme čitanja ograničeno na otprilike %s %s. Tekst čitajte na jednak\
                       način i jednakom brzinom kao i prvi put jer ćete imati dovoljno vremena!' % (minutes, koliko_min),
                       '30 sekundi prije isteka vremena, na lijevoj strani ekrana prikazat će se\
                       okvir unutar kojega će se odbrojavati vrijeme do kraja.',
                       'U glavnom dijelu istraživanja čitat ćete tri teksta. Nakon što jednom pročitate prvi\
                       tekst, zadatak će Vam biti pročitati ga još jednom. Isto tako ćete dva puta pročitati\
                       i drugi tekst.',
                       'Kada ste spremni započeti, pritisnite tipku "Dalje".']
               
        return {
            'rereading': (self.session.config['name'] == '3'),
            'message': message
        }




class Question(Page):
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
        self.participant.vars[str(self.player.question_id)] = self.player.is_correct
        print(str(self.player.question_id), self.participant.vars[str(self.player.question_id)])
        
    def vars_for_template(self):
        num_questions = 4
        return {'num_questions': num_questions}



class practice_text_rep(Page):
    def is_displayed(self):
        return (self.session.config['name'] == '3') & (self.round_number == Constants.num_rounds - 4)
    
    def get_timeout_seconds(self):
            estimate = self.participant.vars['reading_time_estimate'] * 3 # multiplied by 3 because the main text sections have about 3x more words
            minutes = math.ceil(estimate / 60)
            return minutes * 60
    
    


class instructions_2(Page):
    def is_displayed(self):
        return (self.round_number == Constants.num_rounds - 4) & (self.participant.vars['give_feedback'])
    
    def vars_for_template(self):
        message = ['Treći dio sadrži povratnu informaciju o točnosti Vaših odgovora na prethodna pitanja.\
                   Tablica u prvom stupcu sadrži pitanje, u drugom Vaš odgovor, i u trećem točan odgovor.\
                   Crvenom bojom označena su pitanja na koja niste točno odgovorili.',
                   'Dobro proučite povratne informacije. Nakon 10 sekundi, prikazat će se tipka "Dalje",\
                   te ćete moći pritiskom na nju pokrenuti nastavak postupka. Postupak će se automatski\
                   nastaviti nakon 20 sekundi.',
                   'Pritisnite tipku "Dalje" kako biste vidjeli povratne informacije.']
               
        return {
            'message': message
        }




class Results(Page):
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
                       teksta. Pitanja su ponovno tipa višestrukog izbora, stoga označite onaj odgovor koji smatrate točnim\
                       te ga potvrdite pritiskom na tipku "Dalje". To će i automatski pokrenuti prikaz sljedećeg pitanja.',
                       'Pritisnite tipku "Dalje" kako biste dobili završnu uputu.']
        elif self.session.config['name'] is '2':
            rereading = False
            message = ['U glavnom dijelu istraživanja čitat ćete tri teksta. Nakon prvog, a onda i nakon drugog teksta,\
                       također ćete odgovarati na pitanja općeg znanja koja će biti jednakog oblika kao ova na koja ste\
                       upravo odgovarali.',
                       'Nakon čitanja trećeg teksta, odgovarat ćete na pitanja koja će obuhvaćati sadržaj sva tri pročitana\
                       teksta. Pitanja su ponovno tipa višestrukog izbora, stoga označite onaj odgovor koji smatrate točnim\
                       te ga potvrdite pritiskom na tipku "Dalje". To će i automatski pokrenuti prikaz sljedećeg pitanja.',
                       'Pritisnite tipku "Dalje" kako biste dobili završnu uputu.']
        else:
            rereading = True
            message = ['U glavnom dijelu istraživanja čitat ćete tri teksta. Nakon što jednom pročitate prvi tekst, \
                       zadatak će Vam biti pročitati ga još jednom. Isto tako ćete dva puta pročitati i drugi tekst.',
                       'Nakon čitanja trećeg teksta, odgovarat ćete na pitanja koja će obuhvaćati sadržaj sva tri pročitana\
                       teksta. Pitanja su tipa višestrukog izbora, stoga označite onaj odgovor koji smatrate točnim te ga\
                       potvrdite pritiskom na tipku "Dalje". To će i automatski pokrenuti prikaz sljedećeg pitanja.',
                       'Sada ćete odgovoriti na nekoliko pitanja vezana za sadržaj prethodnog teksta kako biste se\
                       upoznali s oblikom pitanja u završnom testu.',
                       'Kada ste spremni započeti, pritisnite tipku "Dalje".']
            
            # because whether giving feedback determines the number of "parts" of a single taks, here, depending
            # on whether feedback is given, a variable is returned to the template that specifies the label of the
            # final part of the instructions
            
        if self.participant.vars['give_feedback'] is True:
            instr_3_title = 'Četvrti, završni dio'
        else:
            instr_3_title = 'Treći, završni dio'
        
        return {
            'message': message,
            'title': instr_3_title,
            'rereading': rereading
        }
        





class Question_rereading(Page):
    def is_displayed(self):
        return (self.session.config['name'] == '3') & (self.round_number > Constants.num_rounds - 4)
    
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
        self.participant.vars[str(self.player.question_id)] = self.player.is_correct
        print(str(self.player.question_id), self.participant.vars[str(self.player.question_id)])






class get_ready(Page):
    form_model = 'player'
    form_fields = ['predznanje']
    
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    
    def predznanje_choices(self):
        return [1, 2, 3, 4, 5, 6, 7]
    
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
            
        estimate = self.participant.vars['reading_time_estimate'] * 3 # multiplied by 3 because the main text sections have about 3x more words
        minutes = math.ceil(estimate / 60)
        
        
        if minutes == 1:
            koliko_min = " minutu"
        elif minutes > 4:
            koliko_min = " minuta"
        else:
            koliko_min = " minute"
            
        if (self.session.config['name'] in ['1', '2']) & (self.participant.vars['give_feedback'] == True):
            message = ['Slijedi glavni dio istraživanja u kojemu ćete proći kroz tri teksta o korovima.\
                        Nakon prvog, a onda i nakon drugog teksta, odgovarat ćete na pitanja poput onih\
                        s kojima ste se upravo upoznali, a nakon zadnjeg teksta ćete odgovarati na pitanja\
                        koja će obuhvaćati sadržaj sva tri pročitana teksta.',
                        'Tekstovi će biti duži, a vrijeme čitanja ograničeno na otprilike %s %s. Tekstove čitajte na jednak\
                        način i jednakom brzinom kao ovaj koji ste upravo čitali jer ćete imati dovoljno vremena!\
                        30 sekundi prije isteka vremena za čitanje, na lijevoj strani ekrana prikazat će se okvir unutar\
                        kojega će se odbrojavati vrijeme do kraja prikaza teksta.' % (minutes, koliko_min),
                        'Vrijeme za proučavanje povratne informacije produženo je. 40 sekundi od početka prikaza\
                        povratne informacije, pojavit će se tipka "Dalje" pri dnu tablice. Pritiskom na nju možete sami\
                        pokrenuti nastavak postupka. Nakon što prođe još 20 sekundi (od prikaza tipke "Dalje"), program\
                        će automatski pokrenuti nastavak postupka. Ukupno, dakle, imate 1 minutu za proučavanje povratne\
                        informacije. Molimo Vas, proučite povratne informacije o Vašoj točnosti jer ćete nakon čitanja\
                        trećeg teksta odgovarati na pitanja koja će se odnositi na sva tri teksta.',
                        'Daljnjih specifičnih uputa neće biti. Ako imate bilo kakvih pitanja, sada ih postavite eksperimentatoru.', 
                        "Pritisnite 'Dalje' kako biste počeli čitati prvi tekst u glavnom dijelu postupka."]
            
        elif (self.session.config['name'] in ['1', '2']) & (self.participant.vars['give_feedback'] == False):
            message = ['Slijedi glavni dio istraživanja u kojemu ćete proći kroz tri teksta o korovima.\
                        Nakon prvog, a onda i nakon drugog teksta, odgovarat ćete na pitanja poput onih\
                        s kojima ste se upravo upoznali, a nakon zadnjeg teksta ćete odgovarati na pitanja\
                        koja će obuhvaćati sadržaj sva tri pročitana teksta.',
                        'Tekstovi će biti duži, a vrijeme čitanja ograničeno na otprilike %s %s. Tekstove čitajte na jednak\
                        način i jednakom brzinom kao ovaj koji ste upravo čitali jer ćete imati dovoljno vremena!\
                        30 sekundi prije isteka vremena za čitanje, na lijevoj strani ekrana prikazat će se okvir unutar\
                        kojega će se odbrojavati vrijeme do kraja prikaza teksta.' % (minutes, koliko_min),
                        'Daljnjih specifičnih uputa neće biti. Ako imate bilo kakvih pitanja, sada ih postavite eksperimentatoru.', 
                        "Pritisnite 'Dalje' kako biste počeli čitati prvi tekst u glavnom dijelu postupka."]
        else:
            message = ['Slijedi glavni dio istraživanja u kojemu ćete proći kroz tri teksta o korovima. Nakon prvog,\
                        a onda i nakon drugog teksta, ponovno ćete čitati netom pročitani tekst, a nakon zadnjeg\
                        ćete odgovarati na pitanja koja će obuhvaćati sadržaj sva tri pročitana teksta.',
                        'Tekstovi će biti duži, a vrijeme čitanja ograničeno na otprilike %s %s. Tekstove čitajte na jednak\
                        način i jednakom brzinom kao ovaj koji ste upravo čitali jer ćete imati dovoljno vremena!\
                        30 sekundi prije isteka vremena za čitanje, na lijevoj strani ekrana prikazat će se okvir unutar\
                        kojega će se odbrojavati vrijeme do kraja prikaza teksta.' % (minutes, koliko_min),
                        'Daljnjih specifičnih uputa neće biti. Ako imate bilo kakvih pitanja, sada ih postavite eksperimentatoru.', 
                        "Pritisnite 'Dalje' kako biste počeli čitati prvi tekst u glavnom dijelu postupka."]
                

        practice_message = ["Sljedeći prikaz sadrži nešto duži tekst.",
                            "Sada Vam je vrijeme čitanja ograničeno na otprilike %s %s. \
                            Vaš zadatak je čitati tekst na jednak način i jednakom brzinom kao prethodni!" % (minutes, koliko_min),
                            "30 sekundi prije isteka vremena, na lijevoj strani ekrana prikazat će se\
                            okvir unutar kojega će se odbrojavati vrijeme do kraja.", 
                            "Pritisnite 'Dalje' kako biste počeli čitati drugi tekst."]
        
        
        if self.session.config['name'] == 'proba':
            return {'is_exp': is_experiment, 'message': practice_message}
        else:
            return {'is_exp': is_experiment, 
                    'feedback': self.participant.vars['give_feedback'],
                    'message': message}             

    def before_next_page(self):
        self.participant.vars['predznanje'] = self.player.predznanje



page_sequence = [timer_instructions_0, practice_text, instructions_1, Question, practice_text_rep, instructions_2, Results, instructions_3, Question_rereading, get_ready]
