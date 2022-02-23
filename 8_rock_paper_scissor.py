
import random

play_count = 0
play_limit = 3
out_of_choices = play_count > play_limit
player_win = 0
computer_win = 0


while play_count < play_limit and not out_of_choices:
    player = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissor:\n").lower()
    opponent = random.choice(['r', 'p', 's'])
    print(f"opponent choice is: {opponent}")

    if player == opponent:
        print("Match Tie")
    elif (player == "r" and opponent == "s") \
            or (player == "s" and opponent == "p") \
            or (player == "p" and opponent == "r"):
        print("Congratulations! You Won!")
        player_win += 1
    else:
        print(f"You Lost! try again.")
        computer_win += 1

    play_limit -= 1

print(f"You won {player_win} game/s out of 3 games")
print(f"Exit the game")
