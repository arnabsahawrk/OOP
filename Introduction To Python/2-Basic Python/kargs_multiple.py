# def function_name(num1, num2, *args, **kargs)
def full_name(first, middle, last):
    return f"{first} {middle} {last}"


name = full_name(last="Emu", first="Arnab", middle="Saha")
print(name)  # Output: Arnab Saha Emu


# key value : kargs
def full_name_kargs(**kargs):
    print(kargs)  # Output: {'first': 'Arnab', 'middle': 'Saha', 'last': 'Emu'}
    for key, value in kargs.items():
        print(f"{key}: {value}")
    return f"{kargs['first']} {kargs['middle']} {kargs['last']}"


print(full_name_kargs(first="Arnab", middle="Saha", last="Emu"))


def multiple_return(num1, num2):
    sum = num1+num2
    multi = num1*num2
    sub = num1 - num2
    return sum, multi, sub


print(multiple_return(33, 4))