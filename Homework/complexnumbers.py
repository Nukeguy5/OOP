
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
    print(f"Starting Complex Number: {c.r} + {c.i}i\n")
    real = 5
    imaginary = 1
    print(f"Adding: {real} + {imaginary}i")
    c.add(5, 1)
    print(f"New Complex Number: {c.r} + {c.i}i\n")
    print(f"Subtracting: {real} + {imaginary}i")
    c.subtract(5, 1)
    print(f"New Complex Number: {c.r} + {c.i}i\n")
    print(f"Multiplying: {real} + {imaginary}i")
    c.multiply(5, 1)
    print(f"New Complex Number: {c.r} + {c.i}i\n")
    print(f"Dividing: {real} + {imaginary}i")
    c.divide(5, 1)
    print(f"New Complex Number: {c.r} + {c.i}i")
