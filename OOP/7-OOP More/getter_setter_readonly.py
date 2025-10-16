class User:
    def __init__(self, name, age, money) -> None:
        self.name = name
        self._age = age
        self.__money = money

    @property  # getter without setter means readonly
    def age(self):
        return self._age

    @property
    def salary(self):
        return self.__money

    @salary.setter  # setter
    def salary(self, value):
        if value < 0:
            return "Invalid."
        self.__money += value


arnab = User("Arnab Saha", 26, 50000)

print(arnab.age)
print(arnab.salary)

arnab.salary = 4500
print(arnab.salary)
