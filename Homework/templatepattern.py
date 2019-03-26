
import datetime as dt


class DateFormat:
    def __init__(self):
        self.time = dt.datetime.now()

    def printTime(self):
        pass


class TwentyFourHour(DateFormat):
    def printTime(self):
        time = self.time.strftime('%H:%M:%S %m/%d/%Y')
        print("Twenty-four hour format:", time)


class MacTime(DateFormat):
    def printTime(self):
        time = self.time.strftime('%a %b %d  %I:%M:%S %p')
        print("Mac time format:", time)


class VerboseDate(DateFormat):
    def printTime(self):
        time = self.time.strftime('%I:%M:%S %p  %A %B %d, %Y')
        print("Verbose date and time:", time)


if __name__ == "__main__":
    tfh = TwentyFourHour()
    tfh.printTime()

    mt = MacTime()
    mt.printTime()

    vd = VerboseDate()
    vd.printTime()
