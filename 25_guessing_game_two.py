
import random


def guess_number(num):
    guess_count = 0

    while True:
        guess = random.randint(0, 100)
        print(f"computer guess number is: {guess}")
        if number_to_guess == guess:
            print(f"Congratulations! your guess is correct.")
            guess_count += 1
            break
        elif number_to_guess > guess:
            print(f"Try again, your guess is too low.")
            guess_count += 1
        else:
            print(f"Try again, your guess is too high.")
            guess_count += 1
    print(f"Total guess count is: {guess_count}")
    print(f"Exit the game.")


number_to_guess = int(input(f"Please enter the number you need to be guessed: "))

guess_number(number_to_guess)
