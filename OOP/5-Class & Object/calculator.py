class Calculator:
    name = "Simple Calculator"

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        return x / y


calc = Calculator()

print(calc.add(45, 6))
print(calc.subtract(45, 6))
print(calc.multiplication(45, 6))
print(calc.division(45, 6))
