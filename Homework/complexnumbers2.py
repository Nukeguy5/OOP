
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary

    def _num_check(self, lst):
        if (type(lst[0]) == int or type(lst[0]) == float) and (type(lst[1]) == int or type(lst[1]) == float):
            return True
        return False

    def _is_list(self, obj):
        if (type(obj) == list or type(obj) == tuple) and (len(obj) == 2) and self._num_check :
            return True
        return False

    def _get_nums(self, complex_num):
        if self._is_list(complex_num):
            real = complex_num[0]
            imaginary = complex_num[1]
            return real, imaginary
        elif isinstance(complex_num, ComplexNumber):
            real = complex_num.r
            imaginary = complex_num.i
            return real, imaginary
        else:
            return NotImplemented

    def __add__(self, complex_num):
        return self.__radd__(complex_num)

    def __radd__(self, complex_num):
        try:
            real, imaginary = self._get_nums(complex_num)
            r = self.r + real
            i = self.i + imaginary
            return ComplexNumber(r, i)
        except TypeError:
            return "Error: Operation used on object that is not list or ComplexNumber"

    def __sub__(self, complex_num):
        return self.__rsub__(complex_num)

    def __rsub__(self, complex_num):
        try:
            real, imaginary = self._get_nums(complex_num)
            r = self.r - real
            i = self.i - imaginary
            return ComplexNumber(r, i)
        except TypeError:
            return "Error: Operation used on object that is not list or ComplexNumber"

    def __mul__(self, complex_num):
        try:
            real, imaginary = self._get_nums(complex_num)
            a = self.r*real - self.i*imaginary
            b = self.r*imaginary + self.i*real
            r = a
            i = b
            return ComplexNumber(r, i)
        except TypeError:
            return "Error: Operation used on object that is not list or ComplexNumber"

    def __floordiv__(self, complex_num):
        cnum = self.__truediv__(complex_num)
        cnum.r = int(cnum.r)
        cnum.i = int(cnum.i)
        return cnum

    def __truediv__(self, complex_num):
        try:
            real, imaginary = self._get_nums(complex_num)
            cnum = self.__mul__([real, -imaginary]) 
            c = real**2 + imaginary**2
            r = cnum.r/c
            i = cnum.i/c
            return ComplexNumber(r, i)
        except TypeError:
            return "Error: Operation used on object that is not list or ComplexNumber"

    def __str__(self):
        if self.i > 0:
            return f'{self.r} + {self.i}i'
        elif self.i < 0:
            return f'{self.r} - {-self.i}i'
        else:
            return f'{self.r}'


if __name__ == "__main__":
    c1 = ComplexNumber(1,2)
    c2 = ComplexNumber(3,4)
    c3 = [3,5]
    c4 = c1 * c2
    c5 = [1,2,3]
 
    print(c1)
    print(c1 + c3)
    print(c3 + c1)
    print(c1 - c3)
    print(c3 - c1)
    print(c4)
    print(c4/c2)
    print(c4//c2)
    print(c5 + c1)
    print(c1 - c5)
    print(c1 * c5)
    print(c1/c5)
