
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Q1

new_list = [x for x in a if x <= 5]
print(new_list)


# Q2

print(list(filter(lambda x: x <= 5, a)))

# Q3

num = int(input(f"Enter your number: "))
print(list(filter(lambda x: (x < num), a)))


