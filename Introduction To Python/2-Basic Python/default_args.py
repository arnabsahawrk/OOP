# default parameters
def sum(num, num2, num3=0):
    return num + num2 + num3


print(sum(1, 2))
print(sum(1, 2, 3))


# numbers of arguments
def all_sum(num, num2, *args):
    print(args)
    total = 0
    for n in args:
        total += n
    return total


print(all_sum(1, 2))
print(all_sum(1, 2, 3, 4, 5))