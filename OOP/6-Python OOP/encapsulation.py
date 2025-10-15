# encapsulation -> hide details
# access modifier: public, private, protected


class Bank:
    def __init__(self, holder_name, branch, initial_deposit) -> None:
        self.name = holder_name  # public attribute
        self._branch = branch  # protected attribute
        self.__balance = initial_deposit  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


arnab = Bank("Arnab", "Feni", 10000)
arnab.deposit(50000)
print(arnab.get_balance())

print(arnab._branch)

# print(arnab.__balance)
# print(dir(arnab))
# print(arnab._Bank__balance)
