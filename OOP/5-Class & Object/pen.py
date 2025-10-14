class Pen:
    def __init__(self, company, type, color, price):
        self.company = company
        self.type = type
        self.color = color
        self.price = price

    def output(self):
        print(
            f"Pen Name: {self.company}, "
            f"Type: {self.type}, Color: {self.color}, Price: {self.price}"
        )


pen1 = Pen("Matador", "Regular", "Black", 6)
pen2 = Pen("Economic", "Old", "Light Black", 5)
pen3 = Pen("Hi-School", "New", "Blue", 10)

pen1.output()
pen3.output()
