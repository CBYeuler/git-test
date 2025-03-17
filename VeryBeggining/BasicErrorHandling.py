print("enter two numbers for division")
a = int(input(":"))
b = int(input(":"))
if b == 0:
    raise ZeroDivisionError("Can't divide to zero")
else:
    print(a / b)


