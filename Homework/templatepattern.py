
import datetime as dt


class DateFormat:
    TIME = dt.datetime.now()

    def formatTime(self):
        pass

    def printTime(self):
        print(self.formatTime())


class TwentyFourHour(DateFormat):
    def formatTime(self):
        time = self.TIME.strftime('%H:%M:%S %m/%d/%Y')
        string = f"Twenty-four hour format: {time}"
        return string


class MacTime(DateFormat):
    def formatTime(self):
        time = self.TIME.strftime('%a %b %d  %I:%M:%S %p')
        string = f"Mac time format: {time}"
        return string


class VerboseDate(DateFormat):
    def formatTime(self):
        time = self.TIME.strftime('%I:%M:%S %p  %A %B %d, %Y')
        string = f"Verbose date and time: {time}"
        return string


if __name__ == "__main__":
    tfh = TwentyFourHour()
    tfh.printTime()

    mt = MacTime()
    mt.printTime()

    vd = VerboseDate()
    vd.printTime()
