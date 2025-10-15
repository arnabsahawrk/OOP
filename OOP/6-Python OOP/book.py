class Book:
    def __init__(self, name) -> None:
        self.name = name

    def watch(self):
        raise NotImplementedError


class OOP(Book):
    def __init__(self, name, practice) -> None:
        self.practice = practice
        super().__init__(name)

    def watch(self):
        print("Watching...")


arnab = OOP("Object Oriented Programming", True)

print(issubclass(Book, OOP))
print(issubclass(OOP, Book))
print(isinstance(arnab, Book))
print(isinstance(arnab, OOP))

arnab.watch()
