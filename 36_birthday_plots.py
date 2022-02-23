import bokeh.plotting
from collections import Counter
import json

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


def run():

    with open("birthdays.json", "r") as f:
        birthdays = json.load(f)

    months = []
    for name, birthday in birthdays.items():
        print(name, birthday)
        month = birthday.split("/")[1]
        months.append(num_to_string[month])

    months = (Counter(months))
    print(months)

    months_name = list(months.keys())
    months_quantity = list(months.values())

    bokeh.plotting.output_file("plot.html")
    plot = bokeh.plotting.figure(x_range=list(num_to_string.values()))
    plot.vbar(x=months_name, top=months_quantity, width=0.7)
    bokeh.plotting.show(plot)


run()
