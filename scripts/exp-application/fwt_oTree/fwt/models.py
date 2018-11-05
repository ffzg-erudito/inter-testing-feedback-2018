from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Matej Pavlić'

doc = """
This app is designed to investigate the forward testing effect
"""


class Constants(BaseConstants):
    name_in_url = 'fwt'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    id = models.StringField(label="prva dva slova imena oca, zadnja dva slova imena majke, i zadnja dva broja mobitela:")
    practice_q1 = models.IntegerField(
            choices = [
                    [1, '']
                    [2, '']
                    [3, '']
                    [4, '']], 
            widget = widgets.RadioSelect)
    practice_q2 = models.IntegerField(
            choices = [
                    [1, '']
                    [2, '']
                    [3, '']
                    [4, '']], 
            widget = widgets.RadioSelect)
    practice_q3 = models.IntegerField(
            choices = [
                    [1, '']
                    [2, '']
                    [3, '']
                    [4, '']], 
            widget = widgets.RadioSelect)
    
    