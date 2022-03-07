'''
The third step is to great the deck class
it has just one instance attribute which is non-public and it contains a list of instances of the card class

the deck also has a property called size which corresponds to the list of cards in the deck

The class shall have four methods: build, show, shuffle, draw and add


'''
import random
from card import Card
from suit import Suit

class Deck:

    SUITS = ('clubs', 'diamonds', 'hearts', 'spades')

    def __init__(self, is_empty=False): ##by default, the deck will not be empty
        self._cards = []

        if not is_empty: ## in this line if the deck is not empty, the deck should be built automatically
            self.build()  ## The code will run automatically when we create an instance of the deck because it is writtene in the init method

    @property
    def size(self):
        return len(self._cards)

    def build(self):
        for suit in Deck.SUITS:
            for value in range(2, 15): ##there is a value from 1 to 14 for each one of the suit created in the conditional above
                self._cards.append(Card(Suit(suit), value)) ## for these two conditions above, we creat a card
                                                            ## and appended it to a list of cards in the instance attribut
                                                            ## A Card object is created for a particular suit and for a particular value obtained from the loop variables

        ### to show the deck using the show method in the card class
    def show(self):
        for card in self._cards:
            card.show()

    ### to implement the shuffle
    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if self._cards: ##if the list of card is not empty
            return self._cards.pop()
        else:
            return None

    def add(self, card): ##this is used when a winner has to add the card that he or she won to the bottom of the deck
        self._cards.insert(0, card)
                                    ## Note: the bottom of the deck is the first element in the list and the top is the last element.
                                    ## So a winner's card is added to the first bottom which is the first element




