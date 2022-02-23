
import random

start_game = input(f"Type Y to start game or type N to exit the game: ").upper()
random_number = random.randint(1, 9)
guess_count = 0

if start_game == "Y":

    while True:
        guess = int(input(f"Enter the number between 1 to 9: "))

        if guess == random_number:
            print(f"Congratulations!")
            guess_count += 1
            break
        elif guess > random_number:
            print(f"number too high")
            guess_count += 1
        else:
            print(f"number too low")
            guess_count += 1

print(f"Total guess count is: {guess_count}")
print(f"exit the game")
