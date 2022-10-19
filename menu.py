from game import Game
from player1 import Player1
from player2 import Player2

def menu(grid):
    print(f"\n  {grid[0][0]} | {grid[0][1]} | {grid[0][2]} \n "
          f"---+---+---\n"
          f"  {grid[1][0]} | {grid[1][1]} | {grid[1][2]} \n"
          f" ---+---+---\n"
          f"  {grid[2][0]} | {grid[2][1]} | {grid[2][2]}  ")


if __name__ == '__main__':
    game = Game()
    MAX_MOVES = 0
    while game.get_winner() is False and MAX_MOVES != 9: 
        if MAX_MOVES % 2 == 0:
            player = Player1()
        else:
            player = Player2()
        game.play(player)
        grid = game.get_grid()
        menu(grid)
        MAX_MOVES += 1
        
    if MAX_MOVES == 9 and game.get_winner:
        print("\n Tied!")
        

# def help():
#     print("-Please enter column and row you wish to place yourself"
#           "\n separated by a space or a comma."
#           "\n Example: 1,2 or 1 2 \n")