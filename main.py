import random

from grid import Grid
from game import Game
from player1 import Player1
from ai import AI
if __name__ == '__main__':
    grid = Grid()
    ai = AI(grid)
    player = Player1()
    grid_board = grid.get_grid()
    moves_history = grid.get_moves_history()
    game = Game(grid_board, moves_history)
    max_moves = 0
    randomizer = random.randrange(1, 3)

    while game.get_winner() is False and max_moves != 9:
        if randomizer == 1:
            game.play(player.make_move(), player.get_symbol())
            randomizer += 1
        else:
            ai.make_move()
            randomizer -= 1
        grid.display_grid()
        max_moves += 1
    if max_moves == 9 and game.get_winner:
        print("\n Tied!")
        

# def help():
#     print("-Please enter column and row you wish to place yourself"
#           "\n separated by a space or a comma."
#           "\n Example: 1,2 or 1 2 \n")