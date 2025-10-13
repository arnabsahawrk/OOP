class Shop:
    cart = []  # cart is a class attribute

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)


arna = Shop("Arna")
arna.add_to_cart("shoes")
arna.add_to_cart("sunglass")
print(arna.cart)

maitry = Shop("Maitry")
maitry.add_to_cart("sari")
print(maitry.cart)
