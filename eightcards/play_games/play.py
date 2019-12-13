import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from eightcards.environment.board import Board

def run():
    bd = Board()
    bd.init_board()
    while not bd.is_end():
        bd.turn_end = False
        bd.attack_action()
        if not bd.turn_end: bd.defend_action()
    bd.end_game()


if __name__ == "__main__":
    run()