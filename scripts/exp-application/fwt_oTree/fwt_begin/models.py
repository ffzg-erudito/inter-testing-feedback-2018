from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
    )

author = 'Matej Pavlić'

doc = """
This app asks the participant to make a personal ID, and to submit basic personal information
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
    participant_code = models.StringField(label = 'Šifra: unesite prva dva slova imena oca, zadnja dva slova imena majke, i zadnje dvije znamenke u broju mobitela:')
    dob = models.IntegerField()
    spol = models.StringField(widget = widgets.RadioSelect)
