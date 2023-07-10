#THIS METHOD IS USE TO SPLIT CONTENTS IN A WORD TO AN ARRAY / LIST
# BY USING THE .split()

course = "Python Programming language"
n= course.split() #it  turns it into an array because no parameter is inputed with a whole index[0]
print ("Before splitting: ", course)
print ("After splitting: ", n)
print (type(n))
for x in n:
    print(x)

b=course.split(",") #divides it into different indexes of array e.g [0],[1],[2]
print(b)
