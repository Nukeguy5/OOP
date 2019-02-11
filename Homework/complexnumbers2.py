
import math

class ComplexNumIter:
    """Iterator class for ComplexNumber implementation."""
    def __init__(self, complex_num, forward=True):
        self.complex_num = complex_num
        self.forward = forward
        if self.forward:
            self.index = 0
            self.dir = 1
        else:
            self.index = 1
            self.dir = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 1 or self.index < 0:
            raise StopIteration
        result = self.complex_num[self.index]
        self.index += self.dir
        return result


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary

    def _num_check(self, lst):
        if (type(lst[0]) == int or type(lst[0]) == float) and (type(lst[1]) == int or type(lst[1]) == float):
            return True
        return False

    def _is_list(self, obj):
        if (type(obj) == list or type(obj) == tuple) and (len(obj) == 2) and self._num_check:
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
        raise TypeError

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

    def __eq__(self, complex_num):
        real, imaginary = self._is_list(complex_num)
        if real == self.r and imaginary == self.i:
            return True
        return False

    def __str__(self):
        if self.i > 0:
            return f'{self.r} + {self.i}i'
        elif self.i < 0:
            return f'{self.r} - {-self.i}i'
        else:
            return f'{self.r}'

    def __getitem__(self, key):
        if type(key) == int or type(key) == float:
            if key < -2 or key > 1 or key != math.floor(key):
                raise IndexError
            elif key == 0 or key == -2:
                return self.r
            return self.i
        elif type(key) == str:
            key = key.lower()
            if key == 'r' or key == 'real':
                return self.r
            elif key == 'i' or key == 'imaginary':
                return self.i
            raise KeyError
        raise TypeError
    
    def __setitem__(self, key, value):
        if type(key) == int or type(key) == float:
            if key < -2 or key > 1 or key != math.floor(key):
                raise IndexError
            elif key == 0:
                self.r = value
            elif key == 1:
                self.i == value
            return
        elif type(key) == str:
            key = key.lower()
            if key == 'r' or key == 'real':
                self.r = value
            elif key == 'i' or key == 'imaginary':
                self.i = value
            else:
                raise KeyError
            return
        raise TypeError

    def __contains__(self, key):
        if type(key) == int or type(key) == float:
            if key == self.r or key == self.i:
                return True
            return False
        elif type(key) == str:
            key = key.lower()
            if key == 'r' or key == 'i':
                return True
            return False
        return TypeError

    def __len__(self):
        return 2

    def __iter__(self):
        return ComplexNumIter(self)

    def __reversed__(self):
        return ComplexNumIter(self, False)


if __name__ == "__main__":
    pass
