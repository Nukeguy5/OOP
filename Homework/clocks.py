
import time as t

class Clock:
    TYPE = "Clock"

    def __init__(self):
        self.time = t.localtime()

    def show_time(self):
        for _ in range(len(1)):
            self.time = t.localtime()
            print(self.time)
            t.sleep(1)

class Sundial(Clock):

    def print_type(self):
        print("Sundial")
        self.show_time()

class Mechanical(Clock):
    TYPE = "Mechanical"

    def print_type(self):
        print("Mechanical")
        self.show_time()

class Cuckoo(Mechanical):
    TYPE = "Cuckoo"


class Grandfather(Mechanical):
    TYPE = "Grandfather"


class Digital(Clock):
    TYPE = "Digital"


class Atomic(Clock):
    TYPE = "Atomic"


if __name__ == "__main__":
    Sundial.print_type()
    Mechanical.print_type()

