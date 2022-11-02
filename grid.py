class Grid:
    def __init__(self):
        self.__grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.__moves_history = {'1': ['1', '2', '3'], '2': ['1', '2', '3'], '3': ['1', '2', '3']}

    def display_grid(self):
        print(f"\n  {self.__grid[0][0]} | {self.__grid[0][1]} | {self.__grid[0][2]} \n "
              f"---+---+---\n"
              f"  {self.__grid[1][0]} | {self.__grid[1][1]} | {self.__grid[1][2]} \n"
              f" ---+---+---\n"
              f"  {self.__grid[2][0]} | {self.__grid[2][1]} | {self.__grid[2][2]}  ")

    def clear_grid(self):
        for row in self.__grid:
            for i in range(row):
                row[i] = " "

    def build_moves_history(self):
        for i in range(1, 4):
            self.__moves_history[i] = ["1", "2", "3"]

    def get_grid(self):
        return self.__grid

    def get_moves_history(self):
        return self.__moves_history
