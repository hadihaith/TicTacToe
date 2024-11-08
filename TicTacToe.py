from importlib.metadata import pass_none

from PlaySol import Computer, println

def main():
    grid, choice = initialize_game()
    show_grid(grid)
    comp_p = Computer()
    print("Player 1 gets to play first as X,", "Then the computer" if choice == 2 else "Then Player 2", "plays as O!")
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
        elif choice == 2:
            if comp_p.check_grid(grid):
                grid = adjust_grid(grid, comp_p.make_choice(),1)
                show_grid(grid)
                print("The computer has made a choice!")
                print()
        who = check_winner(grid)
        if who == 1:
            print("Player 1 wins!")
            break
        elif who == 2:
            print(f"{'Player 2' if choice == 1 else 'Computer'} wins!")
            break
    if ask_again() == 'y':
        main()
    else:
        print("Thanks for playing!")

















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

def check_winner(grid):
    ls1 = grid[0]
    ls2 = grid[1]
    ls3 = grid[2]
    for i in range(3):
        if ls1[i] == ls2[i] and ls1[i] == ls3[i]:
            return 1 if ls1[i] == 'X' else 2
    if ls1[0] == ls1[1] and ls1[2] == ls1[0]:
        return 1 if ls1[1] == 'X' else 2
    if ls2[0] == ls2[1] and ls2[2] == ls2[0]:
        return 1 if ls2[1] == 'X' else 2
    if ls3[0] == ls3[1] and ls3[2] == ls3[0]:
        return 1 if ls3[1] == 'X' else 2
    if ls1[0] == ls2[1] and ls2[1] == ls3[2]:
        return 1 if ls1[0]== 'X' else 2
    if ls1[2] == ls2[1] and ls2[1] == ls3[0]:
        return 1 if ls2[1] == 'X' else 2
    return 0

def ask_again():
    while True:
        x = input("Would you like to play this game again(y/n)? ")
        if x == 'y' or x == 'n':
            break
        else:
            print("Please enter y or n.")
    return x


if __name__ == "__main__":
    main()