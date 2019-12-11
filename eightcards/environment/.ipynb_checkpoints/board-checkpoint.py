import random

from eightcards.environment.card import Card
from eightcards.environment.player import Player

class Board:

    def __init__(self):
        self.cards = []
        self.players = []
        self.pile = []
        self.turns = 1
        self.trump = None
        self.defender = None
        self.attacker = None
        self.winner = None

    @property
    def pile_number(self):
        print(len(self.pile))

    def init_board(self):

        self._init_pile()
        self._init_players()

        for player in self.players:
            for _ in range(8):
                self.deal(player)

        self.trump = random.choice(['Heart', 'Spade', 'Club', 'Diamond'])

        return

    def _init_pile(self):
        for suit in ['Heart', 'Spade', 'Club', 'Diamond']:
            for number in range(1, 14):
                self.pile.append((suit, number))
        self.pile.extend([('Joker', -2), ('Joker', -1)])
        random.shuffle(self.pile)
        return

    def _init_players(self, num_player=2):
        for _ in range(num_player):
            self.players.append(Player())
        flag = random.randint(0, num_player-1)
        self.defender = self.players[flag]
        self.attacker = self.players[flag-1]
        # for player in self.players:
        #     if not player.identity:
        #         player.identity = 'Assist'
        return

    def deal(self, player):

        if player.hand_number < 8:
            card = self.pile.pop()
            player.hand.append(card)
            return
        
        raise ValueError("Cannot deal to a player with 8 or more cards!")

    def attack_action(self):
        print("You are now attacker. Your hand is:")
        print(" ".join(str(card) for card in self.attacker.hand))
        title = "Please use a card to attack"
        card = input(title)
        

    def defend_action(self):
        pass

    def discard_cards(self):
        pass

    def is_end(self):
        pass




