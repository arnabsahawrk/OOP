class Bank:
    bank_name = "IFIC"

    def __init__(self, amount):
        self.balance = amount
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        print(f"Current balance is {self.balance} taka.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.get_balance()
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient amount.")
        elif amount < self.min_withdraw:
            print(f"Can't withdraw less than {self.min_withdraw} taka.")
        elif amount > self.max_withdraw:
            print(f"Can't withdraw more than {self.max_withdraw} taka.")
        else:
            self.balance -= amount
            print(f"Withdraw {amount} taka.")
            self.get_balance()


my_account = Bank(500000)
my_account.deposit(-3)
my_account.deposit(1500)
my_account.withdraw(99)
my_account.withdraw(300000)
my_account.withdraw(33333333333)
my_account.withdraw(4000)
