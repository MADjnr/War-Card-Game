'''
The first step to building the War card game is to creat a suit Class
I copied the suit symbols from the wiki link----   https://en.wikipedia.org/wiki/Standard_52-card_deck
The suit is one of the categories into which the cards of a deck are divided.

Kindly go over to the suit.py file to follow up with the second step.
'''

#### Algorithm:

### The Suit Class has two instance attributes called description and symbols
### The descriptions can be either: 'club', 'diamonds', 'hearts' or 'spades'
### The symbols can be either: ♣ ♦ ♥ ♠
### Tha instance attribute shall be read-only( ie getter)
### There is a class attribute that maps the description to the corresponding symbol...(Hint: a dictionary)

### The constructor takes only one attribute which is the description

class Suit:


    SYMBOLS = {'club': '♣', 'diamonds': '♦', 'hearts': '♥', 'spades': '♠'}

    def __init__(self, description):
        self._description = description  ## The instance attributes are non_public because i do not want them to accessible \
        self._symbol = Suit.SYMBOLS[description.lower()]                        ####### outside the class

## At this stage i will build their property decorator in a pythonic way
    ### This method provides an indirect access into the non_public instance attributes above

    @property
    def description(self):
        return self._description

    @property
    def symbol(self):
        return self._symbol