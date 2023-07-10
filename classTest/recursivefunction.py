#RECURSIVE FUNCTION TO CALCULATE NUMBERS FROM 0 -1O

def recurSum(n):
    if n <= 0:
        return n
    return n + recurSum(n - 1)
  

n = 10
print("The sum for all numbers 0-10 is: ", recurSum(n))