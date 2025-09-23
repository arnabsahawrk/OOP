# print("Now I need money")
# input()
# input("Give me money: ")

money = input("Give me money: ")
print(f"You gave me {money} taka")
print(type(money))  
""" input() always returns a string
so if input a number it will be treated as a string
if want to treat it as a number, need to convert it """
money = int(money)
print(type(money))

moreMoney = int(input("Give me more money: "))
print(f"You gave me total {money + moreMoney} taka")
