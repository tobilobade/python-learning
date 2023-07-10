
#write a program which enters start number and end number, pass the numbers to a function(display) the 

value1= int(input("Enter first value: "))
value2= int(input("Enter second value: "))

def fac(x):
    f=1
    for i in range(1, x+1):
        f*=i
    return f

def display(a,b):
    for x in range (a,b+1):
        print(fac(x))

display(value1, value2)

# write the function which enters a number and prints the factorial of the number

x=int(input("enter number: "))
def fac(x):
    f=1
    for i in range(1, x+1):
        f*=i
    return f
print(fac(x))



