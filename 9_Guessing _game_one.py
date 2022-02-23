
import random

start_game = input(f"Type Y to start game or type N to exit the game: ").upper()
guess_count = 0

if start_game == "Y":
    random_number = random.randint(1, 9)
    guess_number = 0

    while guess_number != random_number:
        guess_number = int(input(f"Enter a number between 1 to 9: "))

        if guess_number < random_number:
            print(f"Guess is too low, guess again.")
            guess_count += 1

        elif guess_number > random_number:
            print(f"Guess is too high, guess again. ")
            guess_count += 1

    else:
        print(f"Congratulations! You have guessed the number correctly.")
        guess_count += 1

print(f"You took, {guess_count} try/tries to guess the number.")
print(f"Exit the game")
