
import random


def game(num_digits):
    listnum = [random.randint(0, 9) for i in range(num_digits)]
    # listnum = random.sample(range(0, 10), num_digits)
    print(f"random_number is: {listnum}")
    guess_count = 0

    while True:
        guess_count += 1
        print(f"Please enter a {num_digits} digit number as a guess: ")
        guess = [int(i) for i in str(input())]

        if guess == listnum:
            print(f"You Won! your guess is correct.")
            break
        else:
            cow = 0
            bull = 0
            for x in range(0, num_digits):
                if guess[x] == listnum[x]:
                    cow += 1
                elif guess[x] in listnum:
                    bull += 1

        print(f"Cows: {cow}, Bulls: {bull}")

    print(f"You took {guess_count} try/tries to guess the correct number.")


game(4)
