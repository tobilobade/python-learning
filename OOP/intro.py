#Creating objects in python
#An object is an instance of a class. By using objects we can access class members, store data etc

#Example 1
class Employee:
    def display(self):
        print ("Hello my name is SG")

emp_obj= Employee()
emp_obj.display()


# Example 2 (Creaing multiple objects)
class Employee:
    def display(self):
        print ("Hello my name is SG")

emp_obj= Employee()
emp_obj.display()

emp_obj= Employee()
emp_obj.display()