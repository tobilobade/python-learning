#multiple

class Two:

    def m2(self):

        print("class 2")

class Three:

    def m3(self):

        print("class 3")

class Four(Two,Three):

    def m4(self):

        print("Child method")

d=Four()

d.m2()

d.m3()

d.m4()




#Parent classes having the same method name

#class C(p1,p2)-->p1's method will be considered first

#class C(p2,p1)-->p2's method will be considered first

class Two:

    def m2(self):

        print("class 2")

class Three:

    def m2(self):

        print("class 3")

class Four(Three,Two):

    def m4(self):

        print("Child method")

d=Four()

d.m2()

d.m4()

