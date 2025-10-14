class Phone:
    def __init__(self, owner, model, price):
        self.owner = owner
        self.model = model
        self.price = price

    def call(self):
        pass


my_phone = Phone("Arnab Saha", "iPhone-7", 16000)

print(my_phone.owner, my_phone.model, my_phone.price)
