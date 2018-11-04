from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Matej Pavlić & Denis Vlašiček'

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
    pass
