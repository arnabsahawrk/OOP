num = 1
while num <= 10:
    print(num)
    num += 1

print("------------")

# Uses of break and continue
num = 1
while num <= 1000:
    num += 1
    if num & 1:  # if num is odd
        continue
    print(num)
    if num == 100:
        break
# Output 1 to 100 even numbers