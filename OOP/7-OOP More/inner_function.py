# In python, function is a first class object


def func():
    print("Function Printed.")

    def inner_func():
        print("Inner Function Printed.")
        return "Inner Function Returned."

    return inner_func


print(func())
print(func()())
