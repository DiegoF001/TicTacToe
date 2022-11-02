import sys



class AI:

    def __init__(self, grid):
        self.__grid = grid

    def minimax(self, grid_board, depth, is_maximizing):
        pass

    def best_move(self):
        grid_board = self.__grid.get_grid().copy()
        bestScore = -sys.maxsize-1
        move = []
        for i in range(3):
            for j in range(3):
                if grid_board[i][j] == " ":
                    score = self.minimax(grid_board, 0, True)
                    if score > bestScore:
                        bestScore = score
                        move.append(i)
                        move.append(j)
        self.__grid.get_grid()[move[0]][move[1]] = "0"



    def make_move(self):
        return input("\n0 turn: ")

    def get_symbol(self):
        return "0"


