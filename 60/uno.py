from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()

UnoCard = namedtuple('UnoCard', 'suit name')


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""

    names = [i for i in range(1, 10)] + \
            ("Draw Two,Skip,Reverse").split(',')

    zeros = [UnoCard(suit, 0) for suit in SUITS]

    wilds = [UnoCard(None, name) for name
             in ['Wild']*4 + ['Wild Draw Four']*4]

    others = [UnoCard(suit, name) for suit in SUITS for name in names * 2]

    return zeros + wilds + others

print(create_uno_deck())