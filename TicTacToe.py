
def main():
    initialize_game()












def initialize_game():
    input("Before we begin, Maximize your terminal for best experience. press enter to start...")
    with open("static/resource.txt") as t:
        l = t.read()
    print(l)
    print("Welcome to Tic Tac Toe Game created by Hadihaith!")




if __name__ == "__main__":
    main()