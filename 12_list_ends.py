
import random


def random_list():
    my_list = list(random.sample(range(1, 20), 5))
    print(my_list)
    a = [my_list[0], my_list[-1]]
    print(a)


random_list()
