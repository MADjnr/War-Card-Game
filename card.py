'''
The second step is to create the Card class. Which is an important aprt of the game.
the constructor of the class shall have two instance attributes: suit and value.
These attributes are non-public so that they can be protected from direct access outside the class.

The Card Class also has a class attribute that maps the values of the special cards to their written description
The class also has two methods: show and is_special

The show method shall display the value, suit and symbol of the suit of the card

While the is_special description shall return True if the value of the card is greater than or equal to 11 and
false otherwise.

'''

class Card:

    SPECIAL_CARDS = {11: 'jack', 12: 'Queen', 13: 'King', 14: 'Ace'}

    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value

    ## The method here presents the value of the card to the user
    def show(self):
        card_value = self._value
        card_suit = self._suit.description.capitalize() ## i need to get the suit of the card but the description of the suit
                                                        ### since the suit is a defined object, i can access its attributes which is the .description
        suit_symbol = self._suit.symbol ## the access was granted outside of the class because of the Suit class i had defined earlier \
                                        ## Which has a property called symbol which ofcourse can be accessed outside of the class
                                        ## 'description' and 'symbol' are properties that we defined in our suit class

        if self.is_special():##this returns true as defined in the method below
            card_description = Card.SPECIAL_CARDS[card_value] ## example, the card description of 11 is 'Jack'.
                                                              ## Therefore, the card value is used to access its description
            print(f'{card_description} of {card_suit} {suit_symbol}')

        else:                                                 ## else the card is not a special card 
            print(f'{card_value} of {card_suit} {suit_symbol}')

    ## implementing the first method: is_special which will check if our card is special or not
    def is_special(self):
        return self._value >= 11 ## this line returns true if the value of the card is greater than or equal to 11
                                 ## the value of 11 is 'Jack', so if any card is greater than or equal to 11, then the card is a special card
