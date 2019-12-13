from eightcards.environment.board import Board

def run():
    bd = Board()
    bd.init_board()
    while not bd.is_end():
        bd.attack_action()
        bd.defend_action()
    bd.end_game()


if __name__ == "__main__":
    run()