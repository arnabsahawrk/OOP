"""
This script demonstrates the use of variables in Python. (name = value)
It includes examples of different data types and basic operations.

Ctrl + / to comment/uncomment multiple lines of code.
Alt + Shift + A to comment/uncomment a block of code.
"""

# Variables in Python
name = "Arnab Saha"
age = 26
is_single = True
is_sleeping = False
salary = 25000
tax = 1000.50

# Printing the variables
print(name)
print(age)
print(salary - tax)

# Checking the data types
print(type(name))
print(type(age))
print(type(is_single))
print(type(tax))

print("Arnab Saha" + " is " + str(age) + " years old.")

text = f"{name} is {age} years old."
print(text)
