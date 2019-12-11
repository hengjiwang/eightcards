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
        pass

    def defend(self, card):
        pass
    
    # def surrend(self):
    #     pass

    # def stop_attack(self):
    #     pass
