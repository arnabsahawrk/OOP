class Vehicle:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class Bus(Vehicle):
    def __init__(self, name, price, seats) -> None:
        super().__init__(name, price)
        self.seats = seats


class Truck(Vehicle):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price)
        self.weight = weight


class PickUpTruck(Truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)


class AcBus(Bus):
    def __init__(self, name, price, seats, temperature) -> None:
        super().__init__(name, price, seats)
        self.temperature = temperature

    def __repr__(self) -> str:
        return (
            f"Name: {self.name}, Price: {self.price} "
            f"Seats: {self.seats}, Temperature: {self.temperature}"
        )


green_line = AcBus("Green Line", 50000000, 35, 18)
print(green_line)
