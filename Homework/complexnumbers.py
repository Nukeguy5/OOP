
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
        self.r = self.r*c - self.i*d
        self.i = self.r*d + self.i*c

    def divide(self, c, d):
        self.r = self.r*c + self.i*d 
        self.i = -self.r*d + self.i*c  

        c = c**2 - d**2

        self.r = self.r/c
        self.i = self.i/c