
import random

a = [random.randint(1, 20) for i in range(10)]
b = [random.randint(1, 20) for x in range(15)]
print(a)
print(b)

new_list = list(set(a).intersection(b))
print(new_list)

c = random.sample(range(1, 10), 5)
print(c)
