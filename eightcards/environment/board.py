import sys, random

from eightcards.environment.card import Card
from eightcards.environment.player import Player

class Board:

    def __init__(self):
        self.cards = []
        self.players = []
        self.pile = []
        self.trump = None
        self.defender = None
        self.attacker = None
        self.turns = 1
        self.winner = None
        

    @property
    def pile_number(self):
        print(len(self.pile))

    def init_board(self):

        self._init_pile()
        self._init_players()

        for player in self.players:
            self._deal(player)

        self.trump = random.choice(['Heart', 'Spade', 'Club', 'Diamond'])

        print("Turn 1 -- Number of left cards: " + str(self.pile_number))

        return

    def _init_pile(self):
        for suit in ['Heart', 'Spade', 'Club', 'Diamond']:
            for number in range(1, 14):
                self.pile.append((suit, number))
        self.pile.extend([('Joker', -2), ('Joker', -1)])
        random.shuffle(self.pile)
        return

    def _init_players(self, num_player=2):
        for j in range(num_player):
            self.players.append(Player("Player " + str(j+1)))
        flag = random.randint(0, num_player-1)
        self.defender = self.players[flag]
        self.attacker = self.players[flag-1]
        # for player in self.players:
        #     if not player.identity:
        #         player.identity = 'Assist'
        return

    def _deal(self, player):

        while player.hand_number < 8:
            card = self.pile.pop()
            player.hand.append(card)
            if self.pile_number == 0:
                break
        
        return

    def attack_action(self):

        if self.attacker.no_hand:
            self._end_turn('stop')
            return


        print("You are now attacker. Your hand is:  \n")
        print(" ".join(str(card) for card in self.attacker.hand))

        title = "\n Please use a card to attack (input 'stop' to stop attacking):"
        while True:

            card = input(title)

            if card == 'stop':
                self._end_turn(card)
                break

            if self.attacker.attack(card):
                self.cards.append(card)

                if self.attacker.no_hand and self.pile_number == 0:
                    self.winner = self.attacker
                    self.end_game()

                break

            else:
                title = "The card you chose is not valid. Please choose another one: "

        return
        

    def defend_action(self):
        print("You are now a defender. Your hand is: \n")
        print(" ".join(str(card) for card in self.defender.hand))
        title = "\nPlease use a card to defend (input 'surrender' to surrender this turn):"
        while True:

            card = input(title)

            if card == 'surrender':
                self._end_turn(card)
                break

            if self.defender.defend(card):
                self.cards.append(card)

                if self.defender.no_hand:
                    if self.pile_number == 0:
                        self.winner = self.defender
                        self.end_game()
                    else:
                        self._end_turn()

                break

            else:
                title = "The card you chose is not valid. Please choose another one: "

        return

    def _end_turn(self, last_card=None):

        if last_card == 'surrender':
            while self.cards:
                card = self.cards.pop()
                self.defender.hand.append(card)
        
        else:
            self.cards = []
            self.attacker, self.defender = self.defender, self.attacker

        self._deal(self.attacker)
        self._deal(self.defender)
        self.turns += 1

        print("Turn " + str(self.turns) + " -- Number of left cards: " + str(self.pile_number)) 
        

    def is_end(self):
        return self.winner is not None

    def end_game(self):
        print("WINNER IS " + self.winner.name + "!!!")
        sys.exit(0)



