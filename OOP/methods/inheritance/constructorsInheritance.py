
#Constructors in inheritance

class Num:

    def __init__(self,num):

        self.num=num

    def display(self):

        print(self.num)

class Power(Num):

    def __init__(self,num,n):

        super().__init__(num)

        self.n=n

    def display(self):

        super().display()

        print(self.n)

p=Power(2,3)

p.display()

