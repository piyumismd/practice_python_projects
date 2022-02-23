
from datetime import date

name = input(f"Enter your name: ")
age = int(input(f"Enter your age: "))
current_year = date.today().year
user_birth_year = current_year - age
turn_hundred_year = user_birth_year + 100


print(f"Hello {name}! You will turn 100 years old in {turn_hundred_year}")
