from math import pi as PI
from math import sqrt


class Shape(object):

    def __init__(self):
        """
        Metoda `__init__` je zděděna z nadtřídy -- naše třída `Shape` dědí od
        vestavěného typu `object`, který implementuje metodu `__init__` stejně
        jako tuto, proto není tak úplně potřeba implementovat ji znovu.
        """

        pass

    def area(self):
        raise NotImplementedError


class Circle(Shape):

    def __init__(self, r=0):
        self.r = r

    def area(self):
        return self.r * self.r * PI


class Rectangle(Shape):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Triangle(Shape):

    def __init__(self, side_a, side_b, angle):
        self.side_a = side_a
        self.side_b = side_b
        self.angle = angle

    def area(self):
        """
        FIXME
        """
        pass


if __name__ == "__main__":

    # TODO

    c = Circle(1)
    print(type(c))
    print(dir(c))
    print(c.area())

    r = Rectangle(1,1)
    r_area = r.area()
    print(r_area)

    t = Triangle(9, 15, 16)
    print(t.area())
