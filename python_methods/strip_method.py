# TO REMOVE SPACES FROM EITHER THE LEFT OR RIGHT 
# BY USING EITHER .lstrip() for the left spaces or .rstrip()for right spaces

a= "cags  "
b="a"
c=a+b
d= a.strip() + b 
print(c)
print (a.rstrip())
print(d)
