# abc -> abstract base class
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def eat(self):  # enforce all derived class to have a eat method
        pass

    def move(self):
        pass


class Monkey(Animal):
    name = "Monkey"

    def __init__(self, category) -> None:
        self.category = category
        super().__init__()

    def eat(self):
        print("Eat: Banana")


big_monkey = Monkey("Big Monkey")
print(big_monkey.category)
big_monkey.eat()
