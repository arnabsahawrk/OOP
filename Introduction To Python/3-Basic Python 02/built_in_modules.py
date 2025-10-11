from math import ceil, floor
import random
from time import sleep

number = 24.65

c = ceil(number)
f = floor(number)
print(c, f)

sleep(4)
print(random.random())
print(random.randint(1, 20))
print(random.choice(["Arnab", "Emu", "Arna", "Maitry", "Arup"]))
