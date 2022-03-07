'''
This is where i defined the main functionality of the game
'''

class WarCardGame:


    def __init__(self, player, computer, deck):
        self._player = player
        self._computer = computer
        self._deck = deck

        self.make_initial_decks() ## the intention is for it to run automatically, given that it is the first step below

    ##The first step is to make the initial decks
    def make_initial_decks(self):
        self._deck.shuffle()
        self.make_deck(self._player) ##these were created first before the method was built below
        self.make_deck(self._computer)

    def make_deck(self, character): #the character could be human player or computer
        for i in range(26):
            card = self._deck.draw()
            character.add_card(card)