
class Player1:
    def __init__(self):
        self.symbol = "X"

    def make_move(self):

        return input(f"\n{self.symbol} turn: ")

    def get_symbol(self):
        return self.symbol
