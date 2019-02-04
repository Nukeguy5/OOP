
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary

    def _num_check(self, lst):
        if (type(lst[0]) == int or type(lst[0]) == float) and (type(lst[1]) == int or type(lst[1]) == float):
            return True
        return False

    def _list_check(self, obj):
        if (type(obj) == list or type(obj) == tuple) and (len(obj) == 2) and self._num_check :
            return True
        return False

    def __add__(self, complex_num):
        self.r += real
        self.i += imaginary

    def __radd__(self, complex_num):
        pass

    def __sub__(self, complex_num):
        if self._list_check(complex_num):
            real = complex_num[0]
            imaginary = complex_num[1]

        
        self.r -= real
        self.i -= imaginary
        
    def __mul__(self, complex_num):
        a = self.r*real - self.i*imaginary
        b = self.r*imaginary + self.i*real
        self.r = a
        self.i = b

    def __floordiv__(self, complex_num):
        pass

    def __truediv__(self, complex_num):
        self.multiply(real, -imaginary) 
        c = real**2 + imaginary**2
        self.r = self.r/c
        self.i = self.i/c

    def __str__(self):
        print(f'<{self.x},{self,y}>')


if __name__ == "__main__":
    pass
