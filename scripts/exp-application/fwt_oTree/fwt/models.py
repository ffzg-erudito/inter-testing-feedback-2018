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
    practice_q2 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)
    practice_q3 = models.IntegerField(
            choices = [
                    [1, ''],
                    [2, ''],
                    [3, ''],
                    [4, '']],
            widget = widgets.RadioSelect)

    # test1 content questions
    test1_q1 = models.IntegerField(label = 'Koliko se drvenastih i zeljastih biljaka smatra korovima (zaokružite najbližu vrijednost)?'
            choices = [
                    [1, 'više od 2500'],
                    [2, 'više od 3000'],
                    [3, 'više od 3500'],
                    [4, 'više od 4000']],
            widget = widgets.RadioSelect)
    test1_q2 = models.IntegerField(label = 'Na urbanim prostorima se pojavljuju korovima srodne:'
            choices = [
                    [1, 'rudimentarne biljke'],
                    [2, 'runalne biljke'],
                    [3, 'repaste biljke'],
                    [4, 'ruderalne biljke']],
            widget = widgets.RadioSelect)
    test1_q3 = models.IntegerField(label = 'Za korove je karakteristično da imaju:'
            choices = [
                    [1, 'učinkovit korijenski, ali ne i nadzemni sustav'],
                    [2, 'učinkovit nadzemni sustav, ali ne i korijenski'],
                    [3, 'učinkovit korijenski i nadzemni sustav'],
                    [4, 'neučinkovit i korijenski i nadzemni sustav']],
            widget = widgets.RadioSelect)
    test1_q4 = models.IntegerField(label = 'Hoće li se biljka nazvati korovom ili ne, ovisi o:'
            choices = [
                    [1, 'stupnju u kojem crpi resurse od kulturne biljke'],
                    [2, 'njenoj rasprostranjenosti na nekom području'],
                    [3, 'tome je li biljka cilj uzgoja'],
                    [4, 'njenom potencijalu za proliferaciju']],
            widget = widgets.RadioSelect)
    test1_q5 = models.IntegerField(label = 'Korovi uglavnom pripadaju u skupinu:'
            choices = [
                    [1, 'autotrofnih biljaka'],
                    [2, 'semitrofnih biljaka'],
                    [3, 'heterotrofnih biljaka'],
                    [4, 'autosomnih biljaka']],
            widget = widgets.RadioSelect)
    test1_q6 = models.IntegerField(label = 'Dio okoliša koji su ljudi prilagodili za poljoprivrednu proizvodnju naziva se:'
            choices = [
                    [1, 'agrocenoza'],
                    [2, 'agrodom'],
                    [3, 'agrosfera'],
                    [4, 'agrotop']],
            widget = widgets.RadioSelect)
    test1_q7 = models.IntegerField(label = 'Talofite su:'
            choices = [
                    [1, 'parazitske biljke'],
                    [2, 'gljive'],
                    [3, 'alge'],
                    [4, 'drvenaste biljke']],
            widget = widgets.RadioSelect)
    test1_q8 = models.IntegerField(label = 'Korovi mogu biti korisni u:'
            choices = [
                    [1, 'proizvodnji umjetnih gnojiva'],
                    [2, 'proizvo	dnji celuloznih vlakana'],
                    [3, 'proizvodnji antihistaminika'],
                    [4, 'proizvodnji prirodnih boja']],
            widget = widgets.RadioSelect)
    test1_q9 = models.IntegerField(label = 'Agrofitocenoze su:'
            choices = [
                    [1, 'biljne zajednice korova i kulturnih biljaka'],
                    [2, 'zajednice kulturnih biljaka i sisavaca koji nastanjuju poljoprivredne površine'],
                    [3, 'zajednice raznovrsnih kulturnih biljaka'],
                    [4, 'zajednice raznovrsnih korova na poljoprivrednim površinama']],
            widget = widgets.RadioSelect)
    test1_q10 = models.IntegerField(label = 'Koja od navedenih biljaka je istovremeno i korov i kulturna biljka?'
            choices = [
                    [1, 'crna zob'],
                    [2, 'bijela gorušica'],
                    [3, 'cikorija'],
                    [4, 'ječam']],
            widget = widgets.RadioSelect)

    # test2 content questions
    test2_q1 = models.IntegerField(label = 'Dio okoliša koji su ljudi naselili i prilagodili sebi naziva se:'
            choices = [
                    [1, 'antropofitocenoza'],
                    [2, 'antroposfera'],
                    [3, 'agrosfera'],
                    [4, 'antrotop']],
            widget = widgets.RadioSelect)
    test2_q2 = models.IntegerField(label = 'Podzemni dio stabiljke zove se:'
            choices = [
                    [1, 'rudela'],
                    [2, 'gomolj'],
                    [3, 'korijen'],
                    [4, 'rizom']],
            widget = widgets.RadioSelect)
    test2_q3 = models.IntegerField(label = 'U odnosu na mlađe korovske biljke, starije korovske biljke:'
            choices = [
                    [1, 'imaju jači alelopatijski učinak'],
                    [2, 'sadrže više fitotoksina'],
                    [3, 'sadrže manje inhibitornih tvari'],
                    [4, 'pokazuju veću plastičnost']],
            widget = widgets.RadioSelect)
    test2_q4 = models.IntegerField(label = 'Suncokret nepovoljno djeluje na rast:'
            choices = [
                    [1, 'ambrozije'],
                    [2, 'cikorije'],
                    [3, 'koštana'],
                    [4, 'pirike']],
            widget = widgets.RadioSelect)
    test2_q5 = models.IntegerField(label = 'Pojava korova vezana je uz stvaranje:'
            choices = [
                    [1, 'agrosfere i agrofitocenoze'],
                    [2, 'antroposfere i astenosfere'],
                    [3, 'ekosfere i fitocenoze'],
                    [4, 'antroposfere i agrosfere']],
            widget = widgets.RadioSelect)
    test2_q6 = models.IntegerField(label = 'Na poljoprivrednim zemljištima, biljni sastav korova mijenja se:'
            choices = [
                    [1, 'ovisno o sustavu godišnje izmjene usjeva i obradi tla'],
                    [2, 'ovisno o obradi tla i kolebanju ekoloških čimbenika'],
                    [3, 'ovisno o njegovom potencijalu za proliferaciju'],
                    [4, 'neovisno o poljoprivrednim zahvatima']],
            widget = widgets.RadioSelect)
    test2_q7 = models.IntegerField(label = 'Utjecaj koji jedna vrsta ima na rast i razvitak druge vrste naziva se:'
            choices = [
                    [1, 'anuliranje'],
                    [2, 'alelopatija'],
                    [3, 'fitopatija'],
                    [4, 'anualnost']],
            widget = widgets.RadioSelect)
    test2_q8 = models.IntegerField(label = 'Korovi su se na poljoprivrednim površinama pojavili'
            choices = [
                    [1, 'u mlađe kameno doba, pri stvaranju prvih agrofitocenoza'],
                    [2, 'u starije kameno doba, pri stvaranju antroposfere'],
                    [3, 'u mlađe kameno doba, pri stvaranju agrosfere'],
                    [4, 'u starije kameno doba, pri stvaranju prvih fitocenoza']],
            widget = widgets.RadioSelect)
    test2_q9 = models.IntegerField(label = 'Plodored se odnosi na:'
            choices = [
                    [1, 'sustav godišnje izmjene usjeva'],
                    [2, 'način gnojenja kultura u svrhu restrikcije rasta i razvoja korova'],
                    [3, 'uzgoj biljaka pri kojem je karakteristično okopavanje'],
                    [4, 'broj jedinki zasađenih u jednom redu']],
            widget = widgets.RadioSelect)
    test2_q10 = models.IntegerField(label = 'Koji korov može pozitivno djelovati na raž?'
            choices = [
                    [1, 'troskot'],
                    [2, 'trputac'],
                    [3, 'poljska ljubica'],
                    [4, 'slakoperka']],
            widget = widgets.RadioSelect)

    # test3 content questions
    test3_q1 = models.IntegerField(label = 'Veća otpornost prema nepovoljnim biotskim čimbenicima odnosi se prvenstveno na otpornost prema:'
            choices = [
                    [1, 'inhibitornim tvarima'],
                    [2, 'parazitskim biljkama'],
                    [3, 'virusima i bakterijama'],
                    [4, 'bolestima i štetnicima']],
            widget = widgets.RadioSelect)
    test3_q2 = models.IntegerField(label = 'Poljoprivredno stanište u kojem raste neka biljka zove se:'
            choices = [
                    [1, 'agrobiosfera'],
                    [2, 'agrosfera'],
                    [3, 'biotop'],
                    [4, 'agrobiotop']],
            widget = widgets.RadioSelect)
    test3_q3 = models.IntegerField(label = 'Neki korovi biološku reprodukciju u nepovoljnim uvjetima osiguravaju putem:'
            choices = [
                    [1, 'neotenije'],
                    [2, 'alelopatije'],
                    [3, 'diploidije'],
                    [4, 'domestikacije']],
            widget = widgets.RadioSelect)
    test3_q4 = models.IntegerField(label = 'Veći stupanj domestikacije korova dovodi do:'
            choices = [
                    [1, 'smanjenja alelopatijskog djelovanja'],
                    [2, 'bržeg širenja sjemenja'],
                    [3, 'promjene ploidije korova'],
                    [4, 'smanjenja dormantnosti']],
            widget = widgets.RadioSelect)
    test3_q5 = models.IntegerField(label = 'Veći, bujniji i varijabilniji korovi imaju karakteristiku:'
            choices = [
                    [1, 'poliploidije'],
                    [2, 'neotenije'],
                    [3, 'dormantnosti'],
                    [4, 'fertilizacije']],
            widget = widgets.RadioSelect)
    test3_q6 = models.IntegerField(label = 'Neotenija korova za posljedicu ima:'
            choices = [
                    [1, 'povećanu plastičnost'],
                    [2, 'brzo sazrijevanje'],
                    [3, 'prilagodbu kulturnim biljkama'],
                    [4, 'stvaranje velikog broja sjemenki']],
            widget = widgets.RadioSelect)
    test3_q7 = models.IntegerField(label = 'Velika otpornost sjemenki korova na štetne eksterne utjecjaje proizlazi iz:'
            choices = [
                    [1, 'malih dimenzija sjemena'],
                    [2, 'male mase sjemena'],
                    [3, 'čvrste sjemene ljuske'],
                    [4, 'kalijpozitivnosti sjemena']],
            widget = widgets.RadioSelect)
    test3_q8 = models.IntegerField(label = 'Pojam poliploidija se odnosi na:'
            choices = [
                    [1, 'broj setova kromosoma'],
                    [2, 'broj zigotnih stanica'],
                    [3, 'broj alelopatijskih odnosa'],
                    [4, 'broj izdanaka koji tvore stabljiku']],
            widget = widgets.RadioSelect)
    test3_q9 = models.IntegerField(label = 'Veću otpornost prema ekstremnim abiotskim utjecajima korovi mogu zahvaliti:'
            choices = [
                    [1, 'svom florističkom sastavu'],
                    [2, 'pretežnoj diploidnosti i bujnosti'],
                    [3, 'strukturi korijena i razgranatosti stabljike'],
                    [4, 'većoj vitalnosti i većoj heterozigotnosti']],
            widget = widgets.RadioSelect)
    test3_q10 = models.IntegerField(label = 'Dormantnost je karakteristika korova koja se odnosi na:'
            choices = [
                    [1, 'mogućnost odgođenog klijanja'],
                    [2, 'prilagodbu kulturnim biljkama'],
                    [3, 'širenje sjemena isključivo u proljeće'],
                    [4, 'klijanje usko vezano uz rast druge biljke']],
            widget = widgets.RadioSelect)
