import random

from grid import Grid
from game import Game
from player1 import Player1

if __name__ == '__main__':
    grid = Grid()
    grid_board = grid.get_grid()
    moves_history = grid.get_moves_history()
    game = Game(grid_board, moves_history)
    randomizer = random.randrange(1, 3)  # 1 or 2

    while game.get_winner() is None and game.moves_left > 0:
        if randomizer == 1:
            game.play()
            randomizer += 1
        else:
            game.make_move_ai()
            randomizer -= 1
        grid.display_grid()

    if game.get_winner() is None and game.moves_left == 0:
        print("\nTIED")
