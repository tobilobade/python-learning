#if the value of a variable is changing from object to object then such variable are called as instance variables


#Example 1
class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name



emp1= Employee(1,"Nina") #Nina and 1 are the instance variables
emp2= Employee(2, "Dami") #Dami and 2 are the instance variable

print("student info")
print("name: ",emp1.name)
print("id: ",emp1.id)

print("student info 2")
print("name: ",emp2.name)
print("id: ",emp2.id)
