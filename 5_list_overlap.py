
import random

a = [random.randint(1, 20) for i in range(10)]
b = [random.randint(10, 30) for u in range(10)]
print(a)
print(b)

common_list = list(set(a).intersection(b))
print(common_list)

