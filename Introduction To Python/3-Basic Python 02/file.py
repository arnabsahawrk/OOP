# .csv comma separated value
# .txt text file

# with open("message.txt", "w") as file:
#     file.write("Python is a awesome language\n")


# with open("message.txt", "a") as file:
#     file.write("Python has simple structure and syntax\n")

with open("message.txt", "r") as file:
    text = file.read()
    print(text)
