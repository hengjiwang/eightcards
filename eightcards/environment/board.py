import sys, os, random

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

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
        self.__turn_end = False
        self.winner = None
        
    @property
    def turn_end(self):
        return self.__turn_end

    @turn_end.setter
    def turn_end(self, value):
        self.__turn_end = value


    @property
    def pile_number(self):
        return len(self.pile)

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
                self.pile.append(Card(suit, number, self))
        self.pile.extend([Card('Joker', -2, self), Card('Joker', -1, self)])
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

        while player.hand_number < 8 and self.pile_number > 0:
            card = self.pile.pop()
            player.hand.append(card)
            if self.pile_number == 0:
                break
        
        return

    def attack_action(self):

        if self.attacker.no_hand:
            self._end_turn('abandon')
            return


        print("\n" + self.attacker.name + ": You are now attacker. " + " (Trump is " + str(self.trump) +") Your hand is:  \n")
        # print(self.attacker.hand)
        print(" ".join(str(card.show()) for card in self.attacker.hand))
        print("\nThe cards on the board are: \n")
        print(" ".join(str(card.show()) for card in self.cards))
        title = "\n Please use a card to attack (input 'abandon' to abandon attacking):"
        while True:

            input_str = input(title)

            if input_str == 'abandon':
                self._end_turn(input_str)
                break
            
            card = self.attacker.get_card_by_str(input_str)

            if not card:
                
                title = "\nThe card you chose is not valid. Please choose another one: "

            elif self.attacker.attack(card):
                self.cards.append(card)

                if self.attacker.no_hand and self.pile_number == 0:
                    self.winner = self.attacker
                    self.end_game()

                break

            else:
                title = "\nThe card you chose is not valid. Please choose another one: "

        return
        

    def defend_action(self):
        print("\n" + self.defender.name + ": You are now a defender. " + " (Trump is " + str(self.trump) + ") Your hand is: \n")
        print(" ".join(str(card.show()) for card in self.defender.hand))
        # print(self.defender.hand)
        print("\nThe cards on the board are: \n")
        print(" ".join(str(card.show()) for card in self.cards))
        title = "\nPlease use a card to defend (input 'surrender' to surrender this turn):"
        while True:

            input_str = input(title)

            if input_str == 'surrender':
                self._end_turn(input_str)
                break
            
            card = self.defender.get_card_by_str(input_str)

            if not card:
                
                title = "\nThe card you chose is not valid. Please choose another one: "


            elif self.defender.defend(card):
                self.cards.append(card)

                if self.defender.no_hand:
                    if self.pile_number == 0:
                        self.winner = self.defender
                        self.end_game()
                    else:
                        self._end_turn()

                break

            else:
                title = "\nThe card you chose is not valid. Please choose another one: "

        return

    def _end_turn(self, input_str=None):

        if input_str == 'surrender':
            while self.cards:
                card = self.cards.pop()
                self.defender.hand.append(card)
        
        else:
            self.cards = []
            self.attacker, self.defender = self.defender, self.attacker

        self._deal(self.attacker)
        self._deal(self.defender)
        self.turns += 1
        self.turn_end = True

        print("\nTurn " + str(self.turns) + " -- Number of left cards: " + str(self.pile_number)) 
        

    def is_end(self):
        return self.winner is not None

    def end_game(self):
        print("\nWINNER IS " + self.winner.name + "!!!")
        sys.exit(0)



