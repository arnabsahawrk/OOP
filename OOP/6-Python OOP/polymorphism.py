class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        print("animal making some sound")


class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print("dog bark")


class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)


dog = Dog("Dog")
cat = Cat("Cat")

dog.make_sound()
cat.make_sound()
