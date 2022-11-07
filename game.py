import sys


class Game:

    def __init__(self, grid, moves_history):
        self.__grid = grid
        self.__moves_history = moves_history
        self.__winner = None
        self.__winner_ai = None
        self.__scores = {"X": -1, "O": 1, "tie": 0}
        self.moves_left = 9
        self.moves_left_ai = 9

    def play(self, move, symbol):
        move = self.input_validation(move)
        self.__grid[move[0]][move[1]] = symbol
        self.moves_left -= 1
        self.__check_winner(symbol)

    # Will validate input is not out of range, and input type
    def input_validation(self, move):
        move = filter(str.isdigit, move)
        move = list(filter(lambda x: 0 <= int(x) <= 2, move))
        move = list(map(int, move))
        if not len(move) == 2:
            move = input("Please enter a row and a column to place yourself into in range 0-2: ")
            return self.input_validation(move)
        if not self.__move_validation(move):
            move = input("Position has previously been taken, please choose another row and column: ")
            return self.input_validation(move)
        return move

    # 1 2, if 2 in dict(1), del
    def __move_validation(self, move):
        if move[1] in self.__moves_history[move[0]]:
            self.__moves_history[move[0]].remove(move[1])
            return True
        return False

    def __check_winner(self, symbol):
        self.__winner = self.equals(symbol)

    def equals(self, symbol):
        # vertical
        for i in range(3):
            if self.__grid[0][i] == symbol and self.__grid[1][i] == symbol and self.__grid[2][i] == symbol:

                return True
        # horizontal
        for i in range(3):
            if self.__grid[i][0] == symbol and self.__grid[i][1] == symbol and self.__grid[i][2] == symbol:

                return True
        # diagonal
        if self.__grid[0][0] == symbol and self.__grid[1][1] == symbol and self.__grid[2][2] == symbol:

            return True
        if self.__grid[0][2] == symbol and self.__grid[1][1] == symbol and self.__grid[2][0] == symbol:

            return True
        return None

    def get_winner(self):
        return self.__winner

    # ------------------AI------------------------------ #

    def best_move(self):
        best_score = -sys.maxsize
        move = [0, 0]
        for i in range(3):
            for j in range(3):
                if self.__grid[i][j] == " ":
                    self.__grid[i][j] = "O"
                    score = self.minimax(self.__grid, 0, False, "O")
                    self.__grid[i][j] = " "
                    self.__winner_ai = None
                    self.moves_left_ai = self.moves_left
                    if score > best_score:
                        best_score = score
                        move[0] = i
                        move[1] = j
        self.__moves_history[move[0]].remove(move[1])
        self.__grid[move[0]][move[1]] = "O"

    def __check_winner_ai(self, symbol):
        self.__winner_ai = self.equals(symbol)
        # tie
        if self.__winner_ai is None and self.moves_left_ai == 0:
            return "tie"
        # X won, or O won
        elif self.__winner_ai:
            return "X" if symbol == "X" else "O"
        # game is still in process, and no winners yet
        return None

    def minimax(self, grid, depth, is_maximizing, symbol):
        self.moves_left_ai -= 1
        result = self.__check_winner_ai(symbol)
        if result is not None:
            score = self.__scores[result]
            return score

        if is_maximizing:
            best_score = -sys.maxsize
            for i in range(3):
                for j in range(3):
                    if grid[i][j] == " ":
                        grid[i][j] = "O"
                        score = self.minimax(grid, depth + 1, False, "O")
                        grid[i][j] = " "
                        self.moves_left_ai = self.moves_left
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = sys.maxsize
            for i in range(3):
                for j in range(3):
                    if grid[i][j] == " ":
                        grid[i][j] = "X"
                        score = self.minimax(grid, depth + 1, True, "X")
                        grid[i][j] = " "
                        self.moves_left_ai = self.moves_left
                        best_score = min(score, best_score)
            return best_score

    def make_move_ai(self):
        self.moves_left_ai = self.moves_left
        self.best_move()
        self.moves_left -= 1
        self.__check_winner("O")
