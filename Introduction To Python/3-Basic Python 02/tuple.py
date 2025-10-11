def multiple():
    return 3, 4


print(multiple())

things = "Monitor", "Mouse", "Keyboard", "Web Cam", "iPhone", "Charger"
print(type(things))
print(things)
print(things[2])
print(things[-2])
print(things[1:3])


if "iPhone" in things:
    print("exits")

# things[0] = "Display" tuple is immutable

print(len(things))

mega = ([1, 2, 3], [1, 2, 5, 4])

print(type(mega))
print(type(mega[0]))

print(mega)
mega[1][2] = 3  # here, tuple is immutable but list is mutable
print(mega)
