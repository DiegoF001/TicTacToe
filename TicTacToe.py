class TicTacToe:
    def __init__(self):
        self.grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        pass

    def play(self, player_position):
        self.validator(player_position)
        return self.grid

    # Will validate input is not out of range, and input type
    def validator(self, player_position):
        c = "Hello My Name is Diego Flores and I come from El Salvador"
        x = c.split()
        print(x)
        x = list(map(str.lower, x))
        print(x)
        c = " ".join(x)
        print(c)

        for chars in player_position:
            if chars == " ":
                continue
            if chars.isdigit():
                print(chars)
            else:
                print("Please enter a valid position")
                break



