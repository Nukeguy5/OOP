
import time as t

class Clock:
    def __init__(self, clock_type):
        self.time = t.localtime()
        self.clock_type = clock_type

    def print_time(self):
        for _ in range(3):
            self.time = t.ctime()
            print("Time:", self.time)
            t.sleep(1)
    
    def show_time(self):
        print("Type:", self.clock_type)
        self.print_time()
        print()


class Sundial(Clock):
    def __init__(self):
        Clock.__init__(self, "Sundial")
    

class Mechanical(Clock):
    def __init__(self, sub_type=None, sound='tick...tock...'):
        Clock.__init__(self, "Mechanical")
        self.sub_type = sub_type
        self.sound = sound

    def show_time(self):
        print(self.clock_type)
        if self.sub_type is not None:
            print("Type:", self.sub_type)
        self.print_time()
        print(self.sound)
        print()


class Cuckoo(Mechanical):
    def __init__(self):
        Mechanical.__init__(self, "Cukoo", "Cukoo! Cukoo!")


class Grandfather(Mechanical):
    def __init__(self):
        Mechanical.__init__(self, "Grandfather", "DONG... DONG... DONG...")


class Digital(Clock):
    def __init__(self):
        Clock.__init__(self, "Digital")


class Atomic(Clock):
    def __init__(self):
        Clock.__init__(self, "Atomic")


if __name__ == "__main__":
    s = Sundial()
    m = Mechanical()
    c = Cuckoo()
    g = Grandfather()
    d = Digital()
    a = Atomic()

    s.show_time()
    m.show_time()
    c.show_time()
    g.show_time()
    d.show_time()
    a.show_time()
