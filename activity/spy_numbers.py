#write a program which displays all spy numbers between 1-1000
#A spy number is a number whose product and sum of digits are the same



def product(a):
   countP= 1
   for i in str(a):
        countP*=int(i)
   return countP


def sum(a):
    countS = 0
    for i in str(a):
        countS+=int(i)
    return countS


def process():
    for i in range(1,1001):
        if product(i)==sum(i):
            print(i)

process()