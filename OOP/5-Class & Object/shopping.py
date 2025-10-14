class Shopping:
    shop_name = "Swapno"

    def __init__(self, name):
        self.name = name
        self.cart = []
        self.total = 0

    def add_to_cart(self, item, price, quantity):
        product = {"item": item, "price": price, "quantity": quantity}
        self.total += price * quantity
        self.cart.append(product)

    def remove_item(self, item):
        for product in self.cart:
            if product["item"] == item:
                self.total -= product["price"] * product["quantity"]
                self.cart.remove(product)
                print(f"{item} removed from cart.")
                return

        print("Item not found.")

    def get_total(self):
        print(f"Purchased {self.total} tk's products.")

    def checkout(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount < self.total:
            print(f"Pay more {self.total - amount} tk.")
        else:
            if amount - self.total:
                print(f"Thanks for shopping. Return {amount - self.total} tk.")
            else:
                print("Tanks for shopping.")


arnab = Shopping("Arnab")

arnab.add_to_cart("Potato", 50, 33)
arnab.add_to_cart("Onion", 80, 20)
arnab.add_to_cart("Fish", 500, 5)
arnab.add_to_cart("Mutton", 1200, 10)

arnab.get_total()

arnab.remove_item("Mutton")
arnab.remove_item("Mutton")

arnab.get_total()

arnab.checkout(0)
arnab.checkout(3000)
arnab.checkout(5750)
