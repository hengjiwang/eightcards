class Card:

    def __init__(self, suit, number, board):

        self.__suit = suit
        self.__number = number
        self.__board = board

    @property
    def suit(self):
        return self.__suit

    @property
    def number(self):
        return self.__number

    @property
    def board(self):
        return self.__board

    @property
    def is_trump(self):
        return self.suit == self.board.trump

    @property
    def attackable(self):
        if self.suit == 'Joker':
            return False

        if self.board.defender.no_hand:
            return False

        if not self.__matched(self.board):
            return False

        return True

    def __matched(self, board):
        cards = board.cards
        for card in cards:
            if self.number == card.number:
                return True
        return False

    @property
    def defensible(self):
        if self.suit == 'Joker':
            return True

        card_to_defend = self.board.cards[-1]

        if self.is_trump:
            if card_to_defend.is_trump:
                return self.number > card_to_defend.number
            else:
                return True

        else:
            if self.suit != card_to_defend.suit:
                return False
            else:
                return self.number > card_to_defend.number
            

    
