# decorator is a nested function
import math
import time


def timer(func):
    def inner():
        print("Time Stated.")
        func()
        print("Time Ended.")

    return inner


# t = timer()
# t()


@timer
def get_factorial():
    print("Factorial Started.")


# print(get_factorial)
# timer(get_factorial)()
# timer(get_factorial())
get_factorial()


def timers(func):
    def inners(n):
        start = time.time()
        func(n)
        end = time.time()
        print(f"Total Time Taken: {end - start}")

    return inners


@timers
def factorial(n):
    print(f"Factorial of {n} is: {math.factorial(n)}")


factorial(1500)
