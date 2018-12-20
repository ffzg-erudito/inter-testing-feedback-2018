from otree.api import Currency as c, currency_range
from ._builtin import Page
from .models import Constants
import time
import math

# this function outputs an integer in the range from 1 to 4 which
# represents a particular experimental situation
def switch(x):
    return {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }[x]




# FIRST PAGE
class enter_id(Page):
    template_name = 'fwt/auxiliary/enter_id.html'
    form_model = 'player'
    form_fields = ['identity']


class instructions(Page):
    template_name = 'fwt/auxiliary/instructions.html'
    pass


class timer_start(Page):
    template_name = 'fwt/auxiliary/timer_start.html'
    def before_next_page(self):
        # user has 5 minutes to complete as many pages as possible
        self.participant.vars['timer_start'] = time.time()

    
    
    


# PRACTICE TEXT AND QUESTION PAGES
class practice_text(Page):
    template_name = 'fwt/texts/practice_text.html'
    def before_next_page(self):
        # user has 5 minutes to complete as many pages as possible
        self.participant.vars['reading_time_estimate'] = time.time() - self.participant.vars['timer_start']

class practice_q1(Page):    
    template_name = 'fwt/practice/q1.html'
    form_model = 'player'
    form_fields = ['practice_q1']
    
    def before_next_page(self):
        self.player.feedback(self.player.practice_q1)
        print(self.player.practice_q1)

class practice_q2(Page):
    template_name = 'fwt/practice/q2.html'
    form_model = 'player'
    form_fields = ['practice_q2']
    
class practice_q3(Page):
    template_name = 'fwt/practice/q3.html'
    form_model = 'player'
    form_fields = ['practice_q3']

class practice_q4(Page):
    template_name = 'fwt/practice/q4.html'
    form_model = 'player'
    form_fields = ['practice_q4']


# GET READY PAGE
class get_ready(Page):
    template_name = 'fwt/auxiliary/get_ready.html'
    pass



# SECTION DEFINING TEXT PAGES AND ACTIVITIES
    
# First text section
class text_1(Page):
    template_name = 'fwt/texts/text_1.html'
    def get_timeout_seconds(self):
        estimate = self.participant.vars['reading_time_estimate'] * 3 # multiplied by 3 because the main text sections have about 3x more words
        minutes = math.ceil(estimate / 60)
        return minutes * 60
    
# PAGES FOR ACTIVITIES AFTER FIRST SECTION
class activity1_task1(Page):
    template_name = 'fwt/content/test1/q1.html'
    form_model = 'player'
    form_fields = ['test1_q1']
#    exp_sit = switch()
#    if exp_sit == 1:
#        template_name = 'fwt/content/test1/q1.html'
#    elif exp_sit == 2:
#        template_name = 'fwt/general/test1/q1.html'
#    elif exp_sit == 3:
#        template_name = 'fwt/math/test1/q1.html'
#    else:
#        template_name = 'fwt/text_1.html'
          
    pass

class activity1_task2(Page):
    template_name = 'fwt/content/test1/q2.html'
    form_model = 'player'
    form_fields = ['test1_q2']
#    exp_sit = switch()
#    if exp_sit == 1:
#        template_name = 'fwt/content/test1/q2.html'
#    elif exp_sit == 2:
#        template_name = 'fwt/general/test1/q2.html'
#    elif exp_sit == 3:
#        template_name = 'fwt/math/test1/q2.html'

          
    pass


class activity1_task3(Page):
    template_name = 'fwt/content/test1/q3.html'
    form_model = 'player'
    form_fields = ['test1_q3']
#    exp_sit = switch()
#    if exp_sit == 1:
#        template_name = 'fwt/content/test1/q3.html'
#    elif exp_sit == 2:
#        template_name = 'fwt/general/test1/q3.html'
#    elif exp_sit == 3:
#        template_name = 'fwt/math/test1/q3.html'

          
    pass


class activity1_task4(Page):
    template_name = 'fwt/content/test1/q4.html'
    form_model = 'player'
    form_fields = ['test1_q4']
#    exp_sit = switch()
#    if exp_sit == 1:
#        template_name = 'fwt/content/test1/q4.html'
#    elif exp_sit == 2:
#        template_name = 'fwt/general/test1/q4.html'
#    elif exp_sit == 3:
#        template_name = 'fwt/math/test1/q4.html'

          
    pass


class activity1_task5(Page):
    template_name = 'fwt/content/test1/q5.html'
    form_model = 'player'
    form_fields = ['test1_q5']
#    exp_sit = switch()
#    if exp_sit == 1:
#        template_name = 'fwt/content/test1/q5.html'
#    elif exp_sit == 2:
#        template_name = 'fwt/general/test1/q5.html'
#    elif exp_sit == 3:
#        template_name = 'fwt/math/test1/q5.html'

          
    pass


class activity1_task6(Page):
    template_name = 'fwt/content/test1/q6.html'
    form_model = 'player'
    form_fields = ['test1_q6']
#    exp_sit = switch()
#    if exp_sit == 1:
#        template_name = 'fwt/content/test1/q6.html'
#    elif exp_sit == 2:
#        template_name = 'fwt/general/test1/q6.html'
#    elif exp_sit == 3:
#        template_name = 'fwt/math/test1/q6.html'

          
    pass


class activity1_task7(Page):
    template_name = 'fwt/content/test1/q7.html'
    form_model = 'player'
    form_fields = ['test1_q7']
#    exp_sit = switch()
#    if exp_sit == 1:
#        template_name = 'fwt/content/test1/q7.html'
#    elif exp_sit == 2:
#        template_name = 'fwt/general/test1/q7.html'
#    elif exp_sit == 3:
#        template_name = 'fwt/math/test1/q7.html'

          
    pass


class activity1_task8(Page):
    template_name = 'fwt/content/test1/q8.html'
    form_model = 'player'
    form_fields = ['test1_q8']
#    exp_sit = switch()
#    if exp_sit == 1:
#        template_name = 'fwt/content/test1/q8.html'
#    elif exp_sit == 2:
#        template_name = 'fwt/general/test1/q8.html'
#    elif exp_sit == 3:
#        template_name = 'fwt/math/test1/q8.html'

    pass


class activity1_task9(Page):
    template_name = 'fwt/content/test1/q9.html'
    form_model = 'player'
    form_fields = ['test1_q9']
#    exp_sit = switch()
#    if exp_sit == 1:
#        template_name = 'fwt/content/test1/q9.html'
#    elif exp_sit == 2:
#        template_name = 'fwt/general/test1/q9.html'
#    elif exp_sit == 3:
#        template_name = 'fwt/math/test1/q9.html'

    pass


class activity1_task10(Page):
    template_name = 'fwt/content/test1/q10.html'
    form_model = 'player'
    form_fields = ['test1_q10']
#    exp_sit = switch()
#    if exp_sit == 1:
#        template_name = 'fwt/content/test1/q10.html'
#    elif exp_sit == 2:
#        template_name = 'fwt/general/test1/q10.html'
#    elif exp_sit == 3:
#        template_name = 'fwt/math/test1/q10.html'

    pass







# SECOND TEXT SECTION
class text_2(Page):
    template_name = 'fwt/texts/text_2.html'
    def get_timeout_seconds(self):
        estimate = self.participant.vars['reading_time_estimate'] * 3 # multiplied by 3 because the main text sections have about 3x more words
        minutes = math.ceil(estimate / 60)
        return minutes * 60




# PAGES FOR ACTIVITIES AFTER SECOND SECTION
class activity2_task1(Page):
    template_name = 'fwt/content/test2/q1.html'
    form_model = 'player'
    form_fields = ['test2_q1']
#    exp_sit = switch()
#    if exp_sit == 1:
#        template_name = 'fwt/content/test2/q1.html'
#    elif exp_sit == 2:
#        template_name = 'fwt/general/test2/q1.html'
#    elif exp_sit == 3:
#        template_name = 'fwt/math/test2/q1.html'
#    else:
#        template_name = 'fwt/text_2.html'
          
    pass

class activity2_task2(Page):
    template_name = 'fwt/content/test2/q2.html'
    form_model = 'player'
    form_fields = ['test2_q2']
#    exp_sit = switch()
#    if exp_sit == 1:
#        template_name = 'fwt/content/test2/q2.html'
#    elif exp_sit == 2:
#        template_name = 'fwt/general/test2/q2.html'
#    elif exp_sit == 3:
#        template_name = 'fwt/math/test2/q2.html'

          
    pass


class activity2_task3(Page):
    template_name = 'fwt/content/test2/q3.html'
    form_model = 'player'
    form_fields = ['test2_q3']
#    exp_sit = switch()
#    if exp_sit == 1:
#        template_name = 'fwt/content/test2/q3.html'
#    elif exp_sit == 2:
#        template_name = 'fwt/general/test2/q3.html'
#    elif exp_sit == 3:
#        template_name = 'fwt/math/test2/q3.html'

          
    pass


class activity2_task4(Page):
    template_name = 'fwt/content/test2/q4.html'
    form_model = 'player'
    form_fields = ['test2_q4']
#    exp_sit = switch()
#    if exp_sit == 1:
#        template_name = 'fwt/content/test2/q4.html'
#    elif exp_sit == 2:
#        template_name = 'fwt/general/test2/q4.html'
#    elif exp_sit == 3:
#        template_name = 'fwt/math/test2/q4.html'

          
    pass


class activity2_task5(Page):
    template_name = 'fwt/content/test2/q5.html'
    form_model = 'player'
    form_fields = ['test2_q5']
#    exp_sit = switch()
#    if exp_sit == 1:
#        template_name = 'fwt/content/test2/q5.html'
#    elif exp_sit == 2:
#        template_name = 'fwt/general/test2/q5.html'
#    elif exp_sit == 3:
#        template_name = 'fwt/math/test2/q5.html'

          
    pass


class activity2_task6(Page):
    template_name = 'fwt/content/test2/q6.html'
    form_model = 'player'
    form_fields = ['test2_q6']
#    exp_sit = switch()
#    if exp_sit == 1:
#        template_name = 'fwt/content/test2/q6.html'
#    elif exp_sit == 2:
#        template_name = 'fwt/general/test2/q6.html'
#    elif exp_sit == 3:
#        template_name = 'fwt/math/test2/q6.html'

          
    pass


class activity2_task7(Page):
    template_name = 'fwt/content/test2/q7.html'
    form_model = 'player'
    form_fields = ['test2_q7']
#    exp_sit = switch()
#    if exp_sit == 1:
#        template_name = 'fwt/content/test2/q7.html'
#    elif exp_sit == 2:
#        template_name = 'fwt/general/test2/q7.html'
#    elif exp_sit == 3:
#        template_name = 'fwt/math/test2/q7.html'

          
    pass


class activity2_task8(Page):
    template_name = 'fwt/content/test2/q8.html'
    form_model = 'player'
    form_fields = ['test2_q8']
#    exp_sit = switch()
#    if exp_sit == 1:
#        template_name = 'fwt/content/test2/q8.html'
#    elif exp_sit == 2:
#        template_name = 'fwt/general/test2/q8.html'
#    elif exp_sit == 3:
#        template_name = 'fwt/math/test2/q8.html'

    pass


class activity2_task9(Page):
    template_name = 'fwt/content/test2/q9.html'
    form_model = 'player'
    form_fields = ['test2_q9']
#    exp_sit = switch()
#    if exp_sit == 1:
#        template_name = 'fwt/content/test2/q9.html'
#    elif exp_sit == 2:
#        template_name = 'fwt/general/test2/q9.html'
#    elif exp_sit == 3:
#        template_name = 'fwt/math/test2/q9.html'

    pass


class activity2_task10(Page):
    template_name = 'fwt/content/test2/q10.html'
    form_model = 'player'
    form_fields = ['test2_q10']
#    exp_sit = switch()
#    if exp_sit == 1:
#        template_name = 'fwt/content/test2/q10.html'
#    elif exp_sit == 2:
#        template_name = 'fwt/general/test2/q10.html'
#    elif exp_sit == 3:
#        template_name = 'fwt/math/test2/q10.html'

    pass








# THIRD AND FINAL TEXT SECTION
class text_3(Page):
    template_name = 'fwt/texts/text_3.html'
    def get_timeout_seconds(self):
        estimate = self.participant.vars['reading_time_estimate'] * 3 # multiplied by 3 because the main text sections have about 3x more words
        minutes = math.ceil(estimate / 60)
        return minutes * 60


# PAGES FOR ACTIVITIES AFTER THIRD AND FINAL TEXT SECTION
class content_test3_q1(Page):
    template_name = 'fwt/final/q1.html'
    form_model = 'player'
    form_fields = ['test3_q1']

    pass

class content_test3_q2(Page):
    template_name = 'fwt/final/q2.html'
    form_model = 'player'
    form_fields = ['test3_q2']          
    pass


class content_test3_q3(Page):
    template_name = 'fwt/final/q3.html' 
    form_model = 'player'
    form_fields = ['test3_q3']         

    pass


class content_test3_q4(Page):
    template_name = 'fwt/final/q4.html'
    form_model = 'player'
    form_fields = ['test3_q4']
    pass


class content_test3_q5(Page):
    template_name = 'fwt/final/q5.html'
    form_model = 'player'
    form_fields = ['test3_q5']
    pass


class content_test3_q6(Page): 
    template_name = 'fwt/final/q6.html'
    form_model = 'player'
    form_fields = ['test3_q6']
    pass


class content_test3_q7(Page):
    template_name = 'fwt/final/q7.html'
    form_model = 'player'
    form_fields = ['test3_q7']
    pass


class content_test3_q8(Page):
    template_name = 'fwt/final/q8.html'
    form_model = 'player'
    form_fields = ['test3_q8']
    pass


class content_test3_q9(Page):
    template_name = 'fwt/final/q9.html'
    form_model = 'player'
    form_fields = ['test3_q9']
    pass


class content_test3_q10(Page):
    template_name = 'fwt/final/q10.html'
    form_model = 'player'
    form_fields = ['test3_q10']
    pass



# GOODBYE PAGE
class end_page(Page):
    template_name = 'fwt/auxilliary/end_page.html'
    pass
    


# here define sequences depending on experimental situation

#exp_sit = switch() - if exp_sit 1-3, then choose this sequence
page_sequence = [
    enter_id,
#    instructions,
    timer_start,
    practice_text,
    practice_q1,
    practice_q2,
    practice_q3,
    practice_q4,
    get_ready,
    text_1,
    activity1_task1,
    activity1_task2,
    activity1_task3,
    activity1_task4,
    activity1_task5,
    activity1_task6,
    activity1_task7,
    activity1_task8,
    activity1_task9,
    activity1_task10,
    get_ready,
    text_2,
    activity2_task1,
    activity2_task2,
    activity2_task3,
    activity2_task4,
    activity2_task5,
    activity2_task6,
    activity2_task7,
    activity2_task8,
    activity2_task9,
    activity2_task10,
    get_ready,
    text_3,
    content_test3_q1,
    content_test3_q2,
    content_test3_q3,
    content_test3_q4,
    content_test3_q5,
    content_test3_q6,
    content_test3_q7,
    content_test3_q8,
    content_test3_q9,
    content_test3_q10,
    end_page
    ]


# else choose this sequence

#page_sequence = [
#    enter_id,
#    instructions,
#    timer_start,
#    practice_text,
#    practice_q1,
#    practice_q2,
#    practice_q3,
#    text_1,
#    text_1,
#    text_2,
#    text_2,
#    text_3,
#    content_test3_q1,
#    content_test3_q2,
#    content_test3_q3,
#    content_test3_q4,
#    content_test3_q5,
#    content_test3_q6,
#    content_test3_q7,
#    content_test3_q8,
#    content_test3_q9,
#    content_test3_q10,
#    end_page
#    ]