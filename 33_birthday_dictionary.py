
birthdays = {"Max": "20/05/1992", "David": "03/07/1995", "Wendy": "24/11/1993", "Benjamin": "15/03/1992"}


def find_birthday():
    print(f"Welcome to the birthday dictionary. We know the birthdays of: ")
    for name in birthdays:
        print(name)

    name = input(f"Whose birthday do you want to look up? ").capitalize()

    if name in birthdays:
        print(f"{name}'s birthday is on {birthdays[name]}")

    else:
        print(f"Sorry, we don't have {name}'s birthday.")


find_birthday()
