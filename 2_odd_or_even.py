
num1 = int(input(f"Enter a number: "))
if num1 % 2 == 0:
    print(f"number {num1} is a even number")
    if num1 % 4 == 0:
        print(f"and number {num1} is a multiple of 4")
    else:
        print(f"and number {num1} is not a multiple of 4")
else:
    print(f"number {num1} is a odd number")
    print(f"and number {num1} is not a multiple of 4")


num = int(input(f"Enter the first number: "))
check = int(input(f"Enter the second number: "))
if num % check == 0:
    print(f"{num} is evenly divisible by {check}")
else:
    print(f"{num} is not evenly divisible by {check}")


