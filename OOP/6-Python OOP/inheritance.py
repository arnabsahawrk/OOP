# base class, parent class, common attribute + functionality class
# derived class, child class, uncommon attribute + functionality class


class Gadget:
    def __init__(self, brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin


class Laptop:
    def __init__(self, memory, ssd) -> None:
        self.memory = memory
        self.ssd = ssd


class Phone(Gadget):
    def __init__(self, brand, price, color, origin, dual_sim) -> None:
        super().__init__(brand, price, color, origin)
        self.dual_sim = dual_sim

    def __repr__(self) -> str:
        return f"Brand: {self.brand}, Dual Sim: {self.dual_sim}"


class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel


my_phone = Phone("iphone", 1200000, "black", "india", False)
print(my_phone)
