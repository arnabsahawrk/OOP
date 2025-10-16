class Shopping:
    cart = []  # class attribute # static attribute
    origin = "china"

    def __init__(self, name, location) -> None:
        self.name = name  # instance attribute
        self.location = location

    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f"{item}, {price}, {remaining}")

    @classmethod
    def remove_item(cls, item):  # class method
        print(f"{item} removed.")

    @staticmethod
    def multiply(x, y):  # static method
        return x * y


saka_maka = Shopping("Saka Maka", "Shi Jin Ping")

saka_maka.purchase("PC", 4343343, 3434343)
# Shopping.purchase(26, 2, 6, 7)

Shopping.remove_item("TV")

print(Shopping.multiply(4, 5))
