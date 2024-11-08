from importlib.metadata import pass_none

from PlaySol import Computer, println

def main():
    grid, choice = initialize_game()
    show_grid(grid)
    comp_p = Computer()
    print("Player 1 gets to play first as X,", "Then the computer" if choice == 2 else "Then the player", "plays as O!")
    turn = 0
    while not grid_done(grid):
        while True:
            try:
                x = int(input(f"Player {(turn + 1)} Make a choice(1 - 9) for the location you want to play: "))
                if x in range(1, 10):
                    break
            except ValueError:
                pass
            print("Enter a number from 1 to 9.")
        grid = adjust_grid(grid, x, turn)
        if choice == 1:
            turn = ((turn + 1) % 2)
            show_grid(grid)
            continue
        elif choice == 2:
            if comp_p.check_grid(grid):
                grid = adjust_grid(grid, comp_p.make_choice(),1)
                show_grid(grid)
                print("The computer has made a choice!")
                print()

















def initialize_game():
    input("Before we begin, Maximize your terminal for best experience. press enter to start... ")
    with open("static/resource.txt") as t:
        l = t.read()
    print(l)
    print("Welcome to Tic Tac Toe Game created by Hadihaith!")
    grid = [list(range(1, 4)),list(range(4, 7)),list(range(7, 10))]
    print("Would you rather play against another player in the console?(1) Or play against the computer?(2)")
    while True:
            try:
                x = int(input("Choice: ").strip())
                if x in [1, 2]:
                    break
            except ValueError:
                pass
            print("Please enter 1 or 2.")
    return grid, x

def show_grid(grid):
    key = 0
    for row in grid:
        print(row[0], "  |  ", row[1], "  |  ", row[2], sep="")
        if key < 2:
            println()
        key += 1

def grid_done(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] in list(range(1, 10)):
                return False
    return True

def adjust_grid(grid, x, turn):
    op = "X" if turn == 0 else "O"
    # I guess i don't need a validation for player 2 entering a spot player 1 entered
    for j in range(len(grid)):
        for i in range(len(grid)):
            if grid[j][i] == x:
                 grid[j][i] = op
    return grid


if __name__ == "__main__":
    main()