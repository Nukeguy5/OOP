
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary

    def add(self, c, d):
        self.r += c
        self.i += d

    def subtract(self, c, d):
        self.r -= c
        self.i -= d
        
    def multiply(self, c, d):
        a = self.r*c - self.i*d
        b = self.r*d + self.i*c
        self.r = a
        self.i = b

    def divide(self, c, d):
        self.multiply(c, -d) 
        c = c**2 + d**2
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
