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
        if not card.defendable:
            return False
        
        self.hand.remove(card)
        return True
