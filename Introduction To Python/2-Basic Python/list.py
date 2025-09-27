# list, array, collection are same in simple terms

# index =  0    1  2   3   4   5   6   7   8   9   10  11
numbers = [45, 65, 37, 22, 29, 10, 77, 43, 23, 32, 56, 80]
# index = -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1

print(numbers[3], numbers[-3])

# list(start : end)
print(numbers[3:7])
print(numbers[-5:-1])

# list(start : end : step)
print(numbers[2:10:3])
print(numbers[8:1:-2])


print(numbers[:])  # shortcut to copy a list
print(numbers[2:])
print(numbers[:7])
print(numbers[::-1])  # shortcut to reverse a list