
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

new_list = list(x for x in a if x % 2 == 0)
print(new_list)

new_list = list(filter(lambda x: x % 2 == 0, a))
print(new_list)
