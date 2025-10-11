# list --> []
# tuple --> ()
# set --> {}
# set: unique items collection. No duplicate and unordered.

numbers = [33, 5, 1, 44, 7, 8, 99, 10, 2, 4, 44, 2, 22, 33, 1, 99]
print(numbers)

numbers_set = set(numbers)
print(numbers_set)

numbers_set.add(100)
print(numbers_set)

# in set can not index-based access

A = {2, 3, 6, 88, 9, 0, 22}
B = {33, 5, 6, 99, 1, 2, 22}

print(A & B)
print(A | B)
