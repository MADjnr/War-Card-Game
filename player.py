'''
At this fourth step of the game, i implemented the player class which contains three instance attributes: name, deck and is_computer

The deck is the instance of the Deck class while the is_computer is boolean

The name is public attribute while the deck and is_computer shall be non-public attributes.

However, the cards have four methods: has_empty_deck, draw_card and add_card
'''

class Player:


    def __init__(self, name, deck, is_computer=False): ##name: is the player's name so that we can customize the nam of the player
                                                      ## Also the deck object that is associated with the player
                                                       ## Also to know if the Player is the computer player which will be faulse by default, so by default the player will be human
        self.name = name
        self._deck = deck
        self._is_computer = is_computer


    @property
    def is_computer(self):
        return self._is_computer

    ## this is a method that returns true or false if the size of the deck associated with the player is empty or not
    def has_empty_deck(self):
        return self._deck.size == 0  ##there is a size property in the deck class
                                     ## So if the player's deck is empty, it returns true

    def draw_card(self):
        if not self.has_empty_deck():
            return self._deck.draw()  ##this draws a card from the deck associated with the player
        else:
            return None

    def add_card(self, card):
        self._deck.add(card) ##there is a add method in the deck class



