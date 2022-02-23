
user_string = (input(f"Enter a word: ")).lower()
sub_string = user_string[::-1]
if user_string == sub_string:
    print(f"Wow!your word is a palindrome.")
else:
    print(f"Your word is not a palindrome.")

