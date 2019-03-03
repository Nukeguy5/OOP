
class Angle:
    def __init__(self, angle=0):
        self.num = self.is_valid_range(angle)

    def is_valid_range(self, angle):
        if angle > 360:
            angle -= 360
            return self.is_valid_range(angle)
        elif angle < 0:
            angle += 360
            return self.is_valid_range(angle)
        return angle

    def __add__(self, angle):
        return self.__radd__(angle)

    def __radd__(self, angle):
        if isinstance(angle, Angle):
            angle = angle.num
        elif type(angle) is not int and type(angle) is not float:
            return NotImplemented
        raw_angle = self.num + angle
        new_angle = self.is_valid_range(raw_angle)
        return new_angle

    def __sub__(self, angle):
        if isinstance(angle, Angle):
            angle = angle.num
        elif type(angle) is not int and type(angle) is not float:
            return NotImplemented
        raw_angle = self.num - angle
        new_angle = self.is_valid_range(raw_angle)
        return new_angle

    def __rsub__(self, angle):
        if isinstance(angle, Angle):
            angle = angle.num
        elif type(angle) is not int and type(angle) is not float:
            return NotImplemented
        raw_angle = angle - self.num
        new_angle = self.is_valid_range(raw_angle)
        return new_angle

    def __mul__(self, angle):
        return self.__rmul__(angle)

    def __rmul__(self, angle):
        if isinstance(angle, Angle):
            angle = angle.num
        elif type(angle) is not int and type(angle) is not float:
            return NotImplemented
        raw_angle = self.num * angle
        new_angle = self.is_valid_range(raw_angle)
        return new_angle

    def __truediv__(self, angle):
        if isinstance(angle, Angle):
            angle = angle.num
        elif type(angle) is not int and type(angle) is not float:
            return NotImplemented
        raw_angle = self.num/angle
        new_angle = self.is_valid_range(raw_angle)
        return new_angle

    def __floordiv__(self, angle):
        if isinstance(angle, Angle):
            angle = angle.num
        elif type(angle) is not int and type(angle) is not float:
            return NotImplemented

        raw_angle = self.num//angle
        new_angle = self.is_valid_range(raw_angle)
        return new_angle

    def __rtruediv__(self, angle):
        if isinstance(angle, Angle):
            angle = angle.num
        elif type(angle) is not int and type(angle) is not float:
            return NotImplemented
        raw_angle = angle/self.num
        new_angle = self.is_valid_range(raw_angle)
        return new_angle

    def __rfloordiv__(self, angle):
        if isinstance(angle, Angle):
            angle = angle.num
        elif type(angle) is not int and type(angle) is not float:
            return NotImplemented
        raw_angle = angle//self.num
        new_angle = self.is_valid_range(raw_angle)
        return new_angle

    def __eq__(self, angle):
        if isinstance(angle, Angle):
            angle = angle.num
        elif type(angle) is not int and type(angle) is not float:
            return NotImplemented

        if angle != self.num:
            return False
        return True

    def __ne__(self, angle):
        if isinstance(angle, Angle):
            angle = angle.num
        elif type(angle) is not int and type(angle) is not float:
            return NotImplemented

        if angle == self.num:
            return False
        return True

    def __le__(self, angle):
        if isinstance(angle, Angle):
            angle = angle.num
        elif type(angle) is not int and type(angle) is not float:
            return NotImplemented

        if angle > self.num:
            return False
        return True

    def __ge__(self, angle):
        if isinstance(angle, Angle):
            angle = angle.num
        elif type(angle) is not int and type(angle) is not float:
            return NotImplemented

        if angle < self.num:
            return False
        return True
    
    def __lt__(self, angle):
        if isinstance(angle, Angle):
            angle = angle.num
        elif type(angle) is not int and type(angle) is not float:
            return NotImplemented

        if angle >= self.num:
            return False
        return True

    def __gt__(self, angle):
        if isinstance(angle, Angle):
            angle = angle.num
        elif type(angle) is not int and type(angle) is not float:
            return NotImplemented

        if angle <= self.num:
            return False
        return True

    def __str__(self):
        return str(self.num)

