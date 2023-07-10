#Abstract method

from abc import *

class Demo1(ABC):

    @abstractmethod

    def m1(self):

        pass

    def m2(self):

        pass

    def m3(self):

        print("implemented method")

d = Demo1()

d.m1()

d.m2()

d.m3()