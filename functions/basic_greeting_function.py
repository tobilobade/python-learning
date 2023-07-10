#BASIC FUNCTION
def greeting(name):
    print (f"hello {name}")
#greeting ("Dami")


#BASIC CALCULATOR FUNCTION

def calculateDiv(a,b):
    if (a>b):
        return a/b
    return b/a

def calculateProduct(a,b):
    return a*b

def calculateDiff(a,b):
    if (a>b):
        return a-b
    return b-a