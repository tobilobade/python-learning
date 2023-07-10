
# write a program that enters a number and prints the factorial of the number
x=int(input("enter number: "))
f=1
for i in range(1, x+1):
        f*=i
        print(f)


x=eval(input("enter number: ")) #evaluate comes in for float or int
n=eval(input("enter power number: "))
p=1
for i in range(0, n):
    p*=x
    print (p)