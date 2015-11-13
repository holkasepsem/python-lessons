<<<<<<< HEAD
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

=======
"""
Třídy a objekty
"""


class Cube(object):

    def __init__(self, side=1):
        self.side = side

    def volume(self):
        return self.side * self.side * self.side

    def surface(self):
        return 6 * self.side * self.side


if __name__ == "__main__":
    print("---OK---")

    # vytvořím objekt (instanci) typu (třídy) krychle.
    c1 = Cube()
    c2 = Cube(2)
    c3 = Cube(side=3)

    print(c1.side, c1.volume(), c1.surface())
    print(c2.side, c2.volume(), c2.surface())
    print(c3.side, c3.volume(), c3.surface())
>>>>>>> af0424488bde0e27ec7efe12f2a939cda23c7fca
