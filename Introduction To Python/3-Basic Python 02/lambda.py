# def doubled(x):
#     return x * 2

doubled = lambda num: num * 2
squared = lambda num: num * num

print(doubled(5))
print(squared(10))

add = lambda x, y: x + y


print(add(3, 50))

numbers = [33, 5, 1, 44, 7, 8, 99, 10, 2, 4, 44, 2, 22, 33, 1, 99]
doubled_nums = map(doubled, numbers)
squared_nums = map(lambda x: x * x, numbers)

print(list(doubled_nums))
print(list(squared_nums))


actresses = [
    {"name": "Deepika Padokone", "age": 38},
    {"name": "Kreeti Suresh", "age": 33},
    {"name": "Samantha Ruth Prabhu", "age": 32},
]

juniors = filter(lambda actress: actress["age"] < 33, actresses)
print(list(juniors))
