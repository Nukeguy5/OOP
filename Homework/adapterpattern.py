
'''
Write adapters for math.sin(), math.cos() that take degrees instead of radians. 
Write adapters for math.asin(), math.acos() that return degrees instead of radians.
'''

import math

class Math:
    @staticmethod
    def Sin(rads):
        return math.sin(rads)

    @staticmethod
    def Cos(rads):
        return math.cos(rads)

    @staticmethod
    def ASin(rads):
        return math.asin(rads)

    @staticmethod
    def ACos(rads):
        return math.acos(rads)


class Adapter(Math):
    @staticmethod
    def Sin(degrees):
        return Math.Sin(degrees*math.pi/180)

    @staticmethod
    def Cos(degrees):
        return Math.Cos(degrees*math.pi/180)

    @staticmethod
    def ASin(degrees):
        rads = degrees*math.pi/180
        rads = rads - math.floor(rads)
        return Math.ASin(rads)

    @staticmethod
    def ACos(degrees):
        rads = degrees*math.pi/180
        rads = rads - math.floor(rads)
        return Math.ACos(rads)


class AdaptedMath:
    def __init__(self, adapterClass):
        self.adapterClass = adapterClass

    def Sin(self, degrees):
        print(self.adapterClass.Sin(degrees))

    def Cos(self, degrees):
        print(self.adapterClass.Cos(degrees))

    def ASin(self, degrees):
        print(self.adapterClass.ASin(degrees))

    def ACos(self, degrees):
        print(self.adapterClass.ACos(degrees))


if __name__ == "__main__":
    a = AdaptedMath(Adapter)
    a.Sin(90)
    a.Cos(0)
    a.ACos(90)
    a.ASin(90)
