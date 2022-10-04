from TicTacToe import TicTacToe


def menu(grid):
    print(f" {grid[0][0]}  |{grid[0][1]}  | {grid[0][2]} \n "
          f"---|---|---\n"
          f"  {grid[1][0]} | {grid[1][1]} | {grid[1][2]} \n"
          f" ---|---|---\n"
          f"  {grid[2][0]} | {grid[2][2]} | {grid[2][2]}")

if __name__ == '__main__':
    game = TicTacToe()
    menu(game.play())
