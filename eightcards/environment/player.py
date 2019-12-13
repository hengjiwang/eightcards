import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from eightcards.environment.card import Card

class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        # self.identity = None

    @property
    def no_hand(self):
        return len(self.hand) == 0

    @property
    def hand_number(self):
        return len(self.hand)

    def attack(self, card):
        if not card.attackable:
            return False

        self.hand.remove(card)
        return True


    def defend(self, card):
        if not card.defensible:
            return False
        
        self.hand.remove(card)
        return True

    def get_card_by_str(self, string):
        elements = string.strip("(").strip(")")
        elements = string.split()

        if len(elements)!=2:
            return None

        if elements[0][-1] == ',':
            elements[0] = elements[0][:-1]
        elements[1] = int(elements[1])
        for card in self.hand:
            if card.suit == elements[0] and card.number == elements[1]:
                return card
        
        return None
