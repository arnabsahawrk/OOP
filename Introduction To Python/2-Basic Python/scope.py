# global variable and local variable
# Access a global variable without using global keyword but for modifying use global keyword

balance = 3000  # global variable


def buy_things(items, price):
    phone = False  # local variable
    global balance
    balance = balance - price
    if (phone):
        print(f'Previous Balance {balance}')
    print(f'Balance After Buying {items}', balance)


buy_things("Sunglass", 300)       

