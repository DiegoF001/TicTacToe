class Game:

    def __init__(self):
        self.__grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.__moves_history = { '1': ['1','2','3'], '2': ['1','2','3'], '3': ['1','2','3']}
        self.__winner = False

    def play(self, player):
        move = self.input_validation(player.make_move())
        self.__grid[move[0]][move[1]] = player.get_symbol()
        self.__winner_found(player.get_symbol())

    # Will validate input is not out of range, and input type
    def input_validation(self, move):
        move = filter(str.isdigit, move)
        move = list(filter(lambda x: 1 <= int(x) <= 3, move))
        if not len(move) == 2:
            move = input("Please enter a row and a column to place yourself into in range 1-3: ")
            return self.input_validation(move)
        if not self.__move_validation(move):
            move = input("Position has previously been taken, please choose another row and column: ")
            return self.input_validation(move)
        return [int(i) - 1 for i in move]

# 1 2, if 2 in dict(1), del 
    def __move_validation(self, move):
        if move[1] in self.__moves_history[move[0]]:
            self.__moves_history[move[0]].remove(move[1])
            return True
        return False

    def __winner_found(self, symbol):
        self.__horizontal_check(symbol)
        self.__vertical_check(symbol)
        self.__diagonal_check(symbol)
        if self.__winner:
            print(f"!!!Winner Found!!: {symbol}")

    def __diagonal_check(self, symbol):
        if self.__grid[0][2] == symbol and \
                self.__grid[1][1] == symbol and \
                self.__grid[2][0] == symbol:
            self.__winner = True
            return
        if self.__grid[0][0] == symbol and self.__grid[1][1] == symbol and \
                self.__grid[2][2] == symbol:
            self.__winner = True

    def __vertical_check(self, symbol):
        row = 0
        column = 0
        while row <=2 and column <=2:
            if self.__grid[row][column] != symbol:
                row = 0
                column += 1
                continue
            row += 1
        if row == 3 or row ==3 and column == 3:
            self.__winner = True
        
            
            
        
            
    
    def __horizontal_check(self, symbol):
        for row in range(len(self.__grid)):
            for column in range(len(self.__grid)):
                if self.__grid[row][column] != symbol:
                    break
                if column == 2:
                    self.__winner = True

    def get_winner(self):
        return self.__winner

    def get_grid(self):
        return self.__grid
