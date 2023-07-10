#Constructor is a method used for initial initializations that are required during the object creation
#In python, The constructor is a method with the name '__init__' .The methods first parameter should be self(referring to current object)

#Example 1
# class Employee:
#     def __init__(self):
#         print("message from constructor")

# emp= Employee()
# print(emp)


# #Example 2
# class Employee:
#     def __init__(self):
#         print("message from constructor")

# emp= Employee()
# emp.__init__()

#Example 3 (parameterised constructor in python)

# class Employee:
#     def __init__(self,id):
#         print("Employeen id is: ", self.id)

# emp1= Employee(1)
# emp2= Employee(1)


#Example 4 (parameterised)

class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def display(self):
            print("Employeen id is: ", self.id)
            print("my name is: ", self.name)

emp1= Employee(1,"Nina")
emp1.display()
emp2= Employee(2, "Dami")
emp2.display()