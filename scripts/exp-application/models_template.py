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


# Pitanja dodajemo tako da unesemo "label" kao prvi argument models.IntegerField-u!

class Player(BasePlayer):
    identity = models.StringField(label = 'prva dva slova imena oca, zadnja dva slova imena majke, i zadnja dva broja mobitela:')

    def feedback(self, form_fields):
        if form_fields == 2:
            print('Točno')
        else:
            print('Netočno')

    # practice questions
    practice_q1 = models.IntegerField(label = 'Tlak kisika uvijek iznosi manje od:',
            choices = [
                    [1, '10% ukupnog atmosferskog tlaka'],
                    [2, '21% ukupnog atmosferskog tlaka'],
                    [3, '73% ukupnog atmosferskog tlaka'],
                    [4, '87% ukupnog atmosferskog tlaka']],
            widget = widgets.RadioSelect)
    practice_q2 = models.IntegerField(label = """Ovisno o promjeni nadmorske visine,
 odnos veličine parcijalnog tlaka kisika u atmosferi i veličine parcijalnog tlaka
 kisika u alveolama pluća je:""",
            choices = [
                    [1, 'proporcionalan'],
                    [2, 'eksponencijalan'],
                    [3, 'konstantan'],
                    [4, 'neproporcionalan']],
            widget = widgets.RadioSelect)
    practice_q3 = models.IntegerField(label = """Smanjenje parcijalnog tlaka kisika
 u zraku može biti posljedica:""",
            choices = [
                    [1, 'povećanja proporcije vodene pare'],
                    [2, 'povećanja nadmorske visine'],
                    [3, 'pojačane respiracijske aktivnosti'],
                    [4, 'smanjenja proporcije vodene pare']],
            widget = widgets.RadioSelect)
    practice_q4 = models.IntegerField(label = """S porastom nadmorske visine, izmjena
 ugljikovog dioksida između alveola i plućnih kapilara je:""",
            choices = [
                    [1, 'povećana'],
                    [2, 'smanjena'],
                    [3, 'konstantna'],
                    [4, 'razmjerna količini vodene pare u alveolama']],
            widget = widgets.RadioSelect)

    # test1 content questions
    test1_q1 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test1_q2 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test1_q3 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test1_q4 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test1_q5 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test1_q6 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test1_q7 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test1_q8 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test1_q9 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test1_q10 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)

    # test2 content questions
    test2_q1 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test2_q2 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test2_q3 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test2_q4 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test2_q5 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test2_q6 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test2_q7 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test2_q8 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test2_q9 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test2_q10 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)

    # test3 content questions
    test3_q1 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test3_q2 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test3_q3 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test3_q4 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test3_q5 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test3_q6 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test3_q7 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test3_q8 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test3_q9 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    test3_q10 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
