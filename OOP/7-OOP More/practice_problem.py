class Product:
    def __init__(self, name, price, quantity) -> None:
        self.product_name = name
        self.product_price = price
        self.product_quantity = quantity

    def __repr__(self) -> str:
        return (
            f"{self.product_name} - {self.product_price}"
            f" ({self.product_quantity} is stock.)"
        )


class Shop:
    def __init__(self, name) -> None:
        self.shop_name = name
        self.products = []

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.products.append(product)
        print("New Product Added.")

    def buy_product(self, item, quantity):
        for product in self.products:
            if product.product_name.lower() == item.lower():
                if quantity > 0 and quantity <= product.product_quantity:
                    print(
                        f"Product Name: {product.product_name},"
                        f" Price: {product.product_price}"
                    )
                    total = product.product_price * quantity
                    print(f"Total Price: {total}")
                    price = int(input())
                    if price >= total:
                        if price - total:
                            print(f"Congress. Return {price - total} tk.")
                        else:
                            print("Congress.")
                    else:
                        print("Invalid.")
                elif quantity > product.product_quantity:
                    print("Stock Out.")
                else:
                    print("Invalid Quantity.")

                return
        print("Product is not available.")


my_shop = Shop("Wallmart")

my_shop.add_product("Coffee", 40, 60)
my_shop.add_product("Oil", 50, 10)
my_shop.add_product("Milk", 40, 100)

my_shop.buy_product("Mouse", 50)
my_shop.buy_product("Coffee", 100)
my_shop.buy_product("Milk", 10)
