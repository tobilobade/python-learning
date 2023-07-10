


#Multilevel

class One:

    def m1(self):

        print("Parent class method")

class Two(One):

    def m2(self):

        print("Child class method")

class Three(Two):

    def m2(self):

        print("child class 3 inheriting from child class")

       

c=Three()

c.m1()

c.m2()