from otree.api import Currency as c, currency_range
from ._builtin import Page
from .models import Constants
import time
import math

# this function outputs an integer in the range from 1 to 4 which
# represents a particular 
def switch(x):
    return {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }[x]

class enter_id(Page):
    form_model = 'player'
    form_fields = ['id']


class instructions(Page):
    pass


class timer_start(Page):

    def before_next_page(self):
        # user has 5 minutes to complete as many pages as possible
        self.participant.vars['timer_start'] = time.time()

    
class practice_text(Page):
    def before_next_page(self):
        # user has 5 minutes to complete as many pages as possible
        self.participant.vars['reading_time_estimate'] = time.time() - self.participant.vars['timer_start']



class practice_test(Page):
    pass



# SECTION DEFINING TEXT PAGES AND ACTIVITIES
class text_1(Page):
    def get_timeout_seconds(self):
        estimate = self.participant.vars['reading_time_estimate'] * 3 # multiplied by 3 because the main text sections have about 3x more words
        minutes = math.ceil(estimate / 60)
        return minutes * 60
    
    

class activity_1(Page):
    template_name = 'fwt/content_test_1.html'
#    exp_sit = switch()
#    if exp_sit == 1:
#        template_name = 'fwt/content_test_1.html'
#    elif exp_sit == 2:
#        template_name = 'fwt/general_test_1.html'
#    elif exp_sit == 3:
#        template_name = 'fwt/math_test_1.html'
#    else:
#        template_name = 'fwt/text_1.html'
          
    pass


class text_2(Page):
    def get_timeout_seconds(self):
        estimate = self.participant.vars['reading_time_estimate'] * 3 # multiplied by 3 because the main text sections have about 3x more words
        minutes = math.ceil(estimate / 60)
        return minutes * 60


class activity_2(Page):
    template_name = 'fwt/content_test_2.html'
#    exp_sit = switch()
#    if exp_sit == 1:
#        template_name = 'fwt/content_test_2.html'
#    elif exp_sit == 2:
#        template_name = 'fwt/general_test_2.html'
#    elif exp_sit == 3:
#        template_name = 'fwt/math_test_2.html'
#    else:
#        template_name = 'fwt/text_2.html'
    
    pass


class text_3(Page):
    def get_timeout_seconds(self):
        estimate = self.participant.vars['reading_time_estimate'] * 3 # multiplied by 3 because the main text sections have about 3x more words
        minutes = math.ceil(estimate / 60)
        return minutes * 60


class activity_3(Page):
    template_name = 'fwt/content_test_3.html'
    pass


class end_page(Page):
    pass


# here define sequences depending on experimental situation

#exp_sit = switch()
page_sequence = [
    enter_id,
    instructions,
    timer_start,
    practice_text,
    practice_test,
    text_1,
    activity_1,
    text_2,
    activity_2,
    text_3,
    activity_3,
    end_page
    ]
