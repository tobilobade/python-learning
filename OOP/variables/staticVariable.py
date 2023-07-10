#if the value of a variable is NOT CHANGING from object to object it is a static variable
# can be accessed in two ways , either by class name or by object name

#Example
class Student:
    college_name="GITAM" #This is the static variable
    def __init__(self,name,id):
        self.name=name
        self.id=id

s1= Student("Naya", 1)
s2= Student("Dami",2)
print("Name: ", s1.name )
print("id: ", s1.id )
print("College name n: ", Student.college_name)
