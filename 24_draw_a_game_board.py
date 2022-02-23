
board_size = int(input("Enter the size of game board you like to play: "))


def print_horizontal_line():
    print(" ___ " * board_size)


def print_vertical_line():
    print("|    " * (board_size + 1))


for i in range(board_size):
    print_horizontal_line()
    print_vertical_line()

print_horizontal_line()
