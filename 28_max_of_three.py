
import random

numbers = random.sample(range(50, 100), 3)
print(numbers)

max_value = max(numbers)
print(f"Maximum number is: {max_value}")

###

a = random.randint(1, 20)
b = random.randint(1, 20)
c = random.randint(1, 20)

print(a, b, c)

if a > b and a > c:
    print(f"Maximum is: {a}")
if b > a and b > c:
    print(f"Maximum is: {b}")
elif c > a and c > b:
    print(f"Maximum is: {c}")
