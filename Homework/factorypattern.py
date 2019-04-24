# Make a Factory that will return either a ComplexNumber class that we made earlier or a new Number class that is a parent of ComlpexNumber. 
# The input to the factory will be a string that is either a regular number or a complex number. 
# It returns a Number if the input was a regular number, but a ComplexNumber if the input was a complex number.

class ComlpexNumber:
    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary

    def Add(self, real, imaginary=None):
        if type(real) == ComlpexNumber:
            a = real.r
            b = real.i
            self.r += a
            self.i += b
        elif real and not imaginary:
            self.r += real
        return self

    # def __str__(self):
    #     if self.i < 0:
    #         return f'{self.r} - {self.i}i'
    #     return f'{self.r} + {self.i}i'


class Number:
    def __init__(self, val):
        self.val = val

    def Add(self, number):
        self.val += number
        return self


class Factory:
    @classmethod
    def ComplexNumberAdd(cls, cn, real, imaginary=None):
        return cn.Add(real, imaginary)

    @classmethod
    def NumberAdd(cls, number, numberToAdd):
        return number.Add(numberToAdd)

if __name__ == "__main__":
    cn = ComlpexNumber(1, 2)
    num = Number(2)

    newCn = Factory.ComplexNumberAdd(cn, 3, 2)
    newNum = Factory.NumberAdd(num, 5)
    print("Complex Number Mem Location:", cn)
    print("Num Mem Location:", num)
    print("NewComplexNum Mem Location:", newCn)
    print("NewNum Mem Location:", newNum)