import random

# 1st method


def game(random_list, num):

    for i in random_list:
        if i == num:
            return True
    return False


random_list = sorted(random.sample(range(1, 20), 10))
print(random_list)
num = random.randint(1, 20)
print(num)
print(game(random_list, num))

# 2nd method


def find(sorted_list, element_find):
    min_ind = 1
    max_ind = len(sorted_list)-1

    while True:
        mid_ind = (max_ind - min_ind) / 2
        mid_ele = sorted_list[mid_ind]

        for i in sorted_list:
            if i != element_find:
                return False
        if mid_ind < min_ind or mid_ind > max_ind or mid_ind < 0:
            return False
        if mid_ele == element_find:
            return True
        elif element_find > mid_ele:
            mid_ind = max_ind
        else:
            mid_ind = min_ind


sorted_list = sorted(random.sample(range(1, 30), 15))
print(sorted_list)
element_find = random.randint(1, 30)
print(element_find)
print(game(sorted_list, element_find))
