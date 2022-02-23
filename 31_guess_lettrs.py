
import random

start_game = str(input(f"Type Y to start game or type N to exit the game: ")).upper()

if start_game == "Y":
    print(f"Welcome to Hangman!")

    with open("sowpods", "r") as f:
        line = f.read().split('\n')
        random_word = random.choice(line)
        # print(f"random word is: {random_word}")

    def play(word):
        word_completion = "_" * len(random_word)
        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = 6
        print(word_completion)
        print("\n")
        while not guessed and tries > 0:
            guess = input(f"Please guess a letter or word: ").upper()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print(f"You have already guessed the letter {guess}")
                elif guess not in random_word:
                    print(f"{guess} is not in the word.")
                    tries -= 1
                    print(f"You have {tries} tries left.")
                    guessed_letters.append(guess)
                else:
                    print(f"Good job, {guess} is in the word.")
                    guessed_letters.append(guess)
                    random_word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(random_word)if letter == guess]
                    for index in indices:
                        random_word_as_list[index] = guess
                    word_completion = "".join(random_word_as_list)
                    if "_" not in word_completion:
                        guessed = True
            elif len(guess) == len(random_word) and guess.isalpha():
                if guess in guessed_words:
                    print(f"You already guessed the word {guess}.")
                elif guess != random_word:
                    print(f"{guess} is not in the word.")
                    tries -= 1
                    print(f"You have {tries} tries left.")
                    guessed_words.append(guess)
                else:
                    guessed = True
                    word_completion = random_word
            else:
                print(f"Not a valid guess.")
            print(word_completion)
            print("\n")
        if guessed:
            print(f"Congrats! You guessed the word {random_word}.")
        else:
            print(f"Sorry, you ran out of tries. The word is {random_word}.")

    play(random_word)

elif start_game == "N":
    print(f"Exit the game.")
else:
    print(f"Invalid input.Try again.")
