from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Matej Pavlić'

doc = """
This app asks the participant to make a personal ID.
"""



class Constants(BaseConstants):
    name_in_url = 'start'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    identity = models.StringField(label = 'prva dva slova imena oca, zadnja dva slova imena majke, i zadnja dva broja mobitela:')
