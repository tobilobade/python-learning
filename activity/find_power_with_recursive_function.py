def factorial(x,y):
    """This is a recursive function
    to find the power of an integer with the second input"""

    if y == 0:
        return 1
    else:
        return  x * factorial(x,y-1)


x = int(input("enter number: "))
y = int(input("enter number: "))
print("The power of", x, "is", factorial(x,y))