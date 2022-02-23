
import json
from collections import Counter


with open("birthdays.json", "r") as file:
    birthdays = json.load(file)
    print(birthdays)

name = birthdays.keys()

num_to_string = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December",

}

months = []

for name, birthday in birthdays.items():
    print(name, birthday)
    month = birthday.split("/")[1]  # ['20', '05', '1992']
    months.append(num_to_string[month])


print(Counter(months))
