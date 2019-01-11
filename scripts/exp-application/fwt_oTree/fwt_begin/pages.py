from ._builtin import Page


# participant has to enter ID - to be implemented: check whether ID conforms to required format
class enter_id(Page):
    form_model = 'player'
    form_fields = ['identity']
    def before_next_page(self):
        self.participant.vars['identity'] = self.player.identity
        print(self.session.config['app_sequence'],'Give feedback? ' + str(self.session.config['feedback']))
        
# initial instructions        
class init_instructions(Page):
    pass


page_sequence = [
    enter_id,
    init_instructions
]
