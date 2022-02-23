
def reverse_string():
    word = str(input(f"Enter a sentence: "))
    split_word = word.split()
    reverse_word = " ".join(split_word[::-1])
    print(reverse_word)

    #  print(" ".join(word.split()[::-1]))


reverse_string()
