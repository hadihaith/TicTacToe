from random import choice


def println():
    print("-" * 3, end="")
    print("+", end="")
    print("-" * 5, end="")
    print("+", end="")
    print("-" * 3, end="")
    print()

class Computer:
    def __init__(self):
        self.name = "Friendly Neighbourhood Fake AI"
        self.choices = []
    def __repr__(self):
        return self.name
    def check_grid(self, grid):
        count = 0
        for row in grid:
            for cell in row:
                if str(cell).isdigit():
                    self.choices.append(cell)
                    count += 1

        return count
    def make_choice(self):
        if self.choices:
            x = choice(self.choices)
            self.choices = []
            return x



