#The variable which we declare inside of a method is called a local variable

#Example 1

# class Demo:
#     def m1(self):
#         a=10 #local variable
#         print(a)
# d=Demo()
# d.m1()


# class One:
#     def m1(self):
#         print("parent class m1 Method")

# class Two(One):
#     def m2(self):
#         print("Child class m2 method")
# c= Two()
# c.m1()
# c.m2()


# class P1:
#     def m1(self):
#         print("parent class m1 Method")

# class P2(P1):
#     def m1(self):
#         print("Child class m2 method")

# class C(P1,P2):
#     def m3(self):
#         print("Child class m3 method")
# c= C()
# c.m3()


#it is not required to define a default constructor for a derived class if base class has a default constructor{only}
#If we have argumented constructors in the base class, then it is the responsibility to pass the respective arguments 
#explicitly using the base class constructor.
