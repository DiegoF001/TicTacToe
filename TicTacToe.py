class TicTacToe:
    def __init__(self):
        pass

    def play(self):
        print("\nPlease enter column and row you wish to place yourself.\n")
        player1 = int(input("X turn: "))
        player2 = int(input("Y turn: "))
        grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
       # if self.validator(player1):
        #    print("d")

        return grid


    # Will validate input is not out of range, and input type
    def validator(self, players):
        print(type(players))
