import random
lines = []


def pick_word():
    with open("sowpods", "r") as f:
        line = f.readline().strip()
        while line:
            line = f.readline().strip()
            lines.append(line)
            random_word = random.choice(lines)

    print(f"The entire file has been read!")
    print(f"The selected random word is: {random_word}")


pick_word()
