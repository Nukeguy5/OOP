
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary

    def add(self, real, imaginary):
        self.r += real
        self.i += imaginary

    def subtract(self, real, imaginary):
        self.r -= real
        self.i -= imaginary
        
    def multiply(self, real, imaginary):
        a = self.r*real - self.i*imaginary
        b = self.r*imaginary + self.i*real
        self.r = a
        self.i = b

    def divide(self, real, imaginary):
        self.multiply(real, -imaginary) 
        c = real**2 + imaginary**2
        self.r = self.r/c
        self.i = self.i/c


if __name__ == "__main__":
    c = ComplexNumber(2, 1)
    print(c.r, c.i)
    c.add(5, 1)
    print(c.r, c.i)
    c.subtract(5, 1)
    print(c.r, c.i)
    c.multiply(5, 1)
    print(c.r, c.i)
    c.divide(5, 1)
    print(c.r, c.i)
