








###################################-- Polymorphism --#####################################

#Overloading - The same having methods with same name but diff parameters

#magic methods/operator overloading

class Book:

    def __init__(self,pages):

        self.pages = pages

    def __add__(self,others):

        return self.pages + others.pages

b1 = Book(100)

b2 = Book(200)

print(b1+b2)




#method overloading

class Demo:

    def m1(self):

        print("no args mthd")

    def m1(self,a):

        print("one-arg mthd")

    def m1(self,a,b):

        print("two-args mthd")

#the last method will be considered. Hence, python does not support overloading

d=Demo()

d.m1()

d.m1(10)

d.m1(10,20)




class Demo:

    def sum(self,a=None,b=None,c=None):

        if a!=None and b!=None and c!=None:

            print('The sum of the 3 numbers: ',a+b+c)

        elif a!=None and b!=None:

            print('The sum of the 2 numbers: ',a+b)

        else:

            print('Pls provide 2 or 3 args')

d=Demo()

d.sum(10,20,30)

d.sum(10,20)

d.sum(10)




#Constructor overloading

class Demo:

    def __init__(self):

        print('No-Arg Constructor')

    def __init__(self,a):

        print('One-Arg Constructor')

    def __init__(self,a,b):

        print('Two-Arg Constructor')        

d1=Demo()

d1=Demo(10)

d1=Demo(10,20)

#the last method will be considered. Hence, python does not support constructor overloading




#Method Overriding

class P:

    def status(self):

        print('Eligible')

    def student(self):

        print('classP Student')

class Q(P):

    def study(self):

        print('Pharmacy')

    def student(self):

        print('classQ Student')

q = Q()

q.status()

q.student()

q.study()




#Constructors Overriding

class Person:

    def __init__(self,name,age):

        self.name=name

        self.age=age

class Employee(Person):

    def __init__(self,name,age,e_no,e_sal):

        super().__init__(name,age)

        self.e_no = e_no

        self.e_sal = e_sal

    def display(self):

        print("Employee's name: ", self.name)

        print("Employee's age: ", self.age)

        print("Employee's number: ",self.e_no)

        print("Employee's Salary: ",self.e_sal)

e1 = Employee('Johnson',24,1234,2400)

e1.display()

e2 = Employee('Charity',29,1235,24200)

e2.display()




