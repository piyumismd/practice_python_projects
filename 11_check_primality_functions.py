
def is_prime(num):

    a = range(1, num+1)
    b = [i for i in a if (num % i == 0)]  # entered num is divided by elements in range "a"

    if num > 1:
        if len(b) == 2:  # prime numbers are divided by only 2 elements: 1 and "the number".
            print(f"Your number is a prime number")
        else:
            print(f"Your number is not a prime number")  # if len(b) > 2
    else:
        print(f"Your number is not a prime number.")


is_prime(int(input(f"Enter a number: ")))
