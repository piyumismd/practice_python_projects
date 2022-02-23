
import random


def random_list():
    r_list = [random.randint(1, 30) for i in range(10)]
    print(r_list)
    no_dup_list = []
    for i in r_list:
        if i not in no_dup_list:
            no_dup_list.append(i)
    print(no_dup_list)


random_list()

###

my_list = [1, 2, 4, 3, 9, 3, 5, 6, 2]
print(my_list)
print(type(my_list))
my_list = set(my_list)
print(my_list)
print(type(my_list))
my_list = list(my_list)
print(my_list)
print(type(my_list))
