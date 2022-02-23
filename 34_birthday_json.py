
import json

# convert to a json file
birthdays = {"Max": "20/05/1992", "David": "03/07/1995", "Wendy": "24/11/1993", "Benjamin": "15/03/1992"}
with open("birthdays.json", "w") as file:
    json.dump(birthdays, file, indent=4)

# load from json

with open("birthdays.json", "r") as f:
    birthdays = json.load(f)
    print(birthdays)

# Add a new entry


def add_new_entry():
    name = input(f"Please enter the name that you want to add to the dictionary: ").capitalize()
    date = str(input(f"Please add the {name}'s birthday as DD/MM/YYYY: "))
    birthdays[name] = date

    with open("birthdays.json", "w") as f:
        json.dump(birthdays, f)
    print(f"{name} was added to the birthday list")


def find_date():
    name = input(f"whose birthday do you want to know? ").capitalize()
    try:
        if birthdays[name]:
            print(f"{name} is born on {birthdays[name]}")
    except KeyError:
        print(f"{name} is not in the list")


def current_entries():
    print(f"The entries in my birthday list are: ")
    for key, value in birthdays.items():
        print(key, value)


add_new_entry()
find_date()
current_entries()
