
user_num = int(input(f"Enter your number: "))
a = range(1, user_num+1)

print(list(filter(lambda x: (user_num % x == 0), a)))

# same as

n_list = [x for x in a if(user_num % x == 0)]
print(n_list)

# same as

print(list(x for x in a if(user_num % x == 0)))
