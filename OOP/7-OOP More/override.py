class Person:
    def __init__(self, name, age, weight, height) -> None:
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def eat(self):
        print("Vat, Mangso, Polao")

    def __len__(self):  # len overload
        return self.height

    def exercise(self):
        raise NotImplementedError(
            "A Person Usually Don't Exercise, But A Cricketer Does."
        )


class Cricketer(Person):
    def __init__(self, name, age, weight, height, team) -> None:
        super().__init__(name, age, weight, height)
        self.team = team

    # overload
    def __add__(self, other):  # dunder method
        return self.name + " & " + other.name

    def __gt__(self, other):  # > operator overload
        return self.age > other.age

    # override
    def eat(self):
        print("Vegetables, Energy Drink")

    def exercise(self):
        print("Always Do.")


sakib = Cricketer("Sakib Al Hasan", 42, 80, 72, "BD")
sakib.eat()
sakib.exercise()

arnab = Person("Arnab Saha", 26, 60, 64)
arnab.eat()
# arnab.exercise()

# overload
print(45 + 67)
print("Arnab" + " Saha")
print([4, 5, 6, 2] + [4, 3, 1])

print(sakib + arnab)
print(len(sakib))  # len overload
print(sakib > arnab)
