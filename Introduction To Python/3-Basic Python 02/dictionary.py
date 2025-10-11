# Dictionary --> {} key value pair

person = {
    "Name": "Arnab Saha",
    "Age": 26,
    "Occupation": "Software Engineer",
    "Address": "Dhaka, Bangladesh",
}
print(person)
print(person["Occupation"])
print(person.keys())
print(person.values())

person["Language"] = "Python"
print(person)

person["Name"] = "Arnab Emu"
print(person)

del person["Age"]
print(person)

print(list(person))
print(sorted(person))

for key in person:
    print(key)

for key, value in person.items():
    print(key, ":", value)
