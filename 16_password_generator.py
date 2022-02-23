
import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",            # import string
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]  # lower = string.ascii_lower
capital_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                   "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]  # upper = string.ascii_upper
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]                              # numbers = string.digits
characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
              "+", "-", "_", ".", ",", "/", "?", ":", ";", "[", "]", "{", "}", "="]   # characters = string.punctuation


print(f"Welcome to the password generator!\nThis will generate a "
      "random password including letters, numbers and characters.")

min_size = int(input(f"Please enter the minimum number of variables you want to have in your password: "))
max_size = int(input(f"Please enter the maximum number of variables you want to have in your password: "))

password_length = (random.choice(range(min_size, max_size + 1)))

password = []

for i in range(1, password_length):
    if len(password) < password_length:
        password.append(random.choice(letters + capital_letters + numbers + characters))

random.shuffle(password)

print(f"Your password is: {''.join(password)}")
print(f"your password length is:  {len(password)}")
