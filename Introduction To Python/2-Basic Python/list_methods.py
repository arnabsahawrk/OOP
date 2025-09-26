numbers = [12, 14, 71, 80]

numbers.append(40)
print(numbers)

numbers.insert(2, 11)
print(numbers)

if 8 in numbers:
    numbers.remove(8)
else:
    numbers.remove(14)
print(numbers)

last = numbers.pop()
print(last, numbers)

index = numbers.index(80)
print(index)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)