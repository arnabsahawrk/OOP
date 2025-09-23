numbers = [5, 10, 15, 20, 25]
sum = 0
for num in numbers:
    sum += num
print("The sum is:", sum)

print("------------")

name = "Arnab Saha"
for char in name:
    print(char)

print("------------")

for i in range(1, 5):
    print(i)

print("------------")

for i in range(1, 10, 2):
    print(i)

print("------------")

fruits = ["apple", "banana", "cherry"]
for index, value in enumerate(fruits):
    print(index, value)          # 0 apple, 1 banana, 2 cherry  
