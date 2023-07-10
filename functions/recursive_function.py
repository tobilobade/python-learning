#RECURSIVE FUNCTION
#A recursive function code is a conditional statement 
#The if condition specifies the stopping condition
#The function operation is done on the else part which contains the recall
#During the recall, some of the arguments may be changed.



# def first_ten(n):
#     if n==6:
#         return
#     else:
#          print(n)
#          print(n-1)

# first_ten(5)

# def factorial(x):
#     """This is a recursive function
#     to find the factorial of an integer"""

#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))


# num = int(input("enter number: "))
# print("The factorial of", num, "is", factorial(num))


# recursive function to get the product of a string of numbers '1234'

def product(string):

    if len(string) == 0:

        return 1

    else:

        return int(string[0]) * product(string[1:])

print(product("1234"))