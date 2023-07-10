#single

class One:

    def m1(self):

        print("Parent class method")

class Two(One):

    def m2(self):

        print("Child class method")

c=Two()

c.m1()

c.m2()


