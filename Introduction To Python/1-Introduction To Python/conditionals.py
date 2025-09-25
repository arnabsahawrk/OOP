
num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

boss = False
if boss is True:
    print("You are the boss.")
else:
    print("You are not the boss.")

if boss is not True:
    print("You are not the boss.")
else:
    print("You are the boss.")

# nested conditionals
boss = True
coin = 'heads'
if boss:
    if coin == 'heads':
        print("You win!")
    else:
        print("You lose!")
else:
    print("You are not the boss.")