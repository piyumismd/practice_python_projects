# 0 1 1 2 3 5 8 13 21
# 0 1 2 3 4 5 6 7 8
# [3] = [2] + [1]
# [2] = [1] + [0]
# [1] = [1]
# [0] = [0]

limit = int(input(f"How many fibonacci numbers do you want: "))


def fibonacci(x):

    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(limit)
for i in fib:
    print(i)

