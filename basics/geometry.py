"""
Implementace základních geometrických objektů.
"""


class Point():
	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z

class Line():
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2	= p2


if __name__ == "__main__":

	# Vytvářím objekt reprezentující bod s výchozími hodnotami
	p1 = Point()
	print(p1.x, p1.y, p1.z)

	p2 = Point(0, 0, 0)
	print(p2.x, p2.y, p2.z)
	
	p3 = Point(0, 0, 1)
	print(p3.x, p3.y, p3.z)
	
	p4 = Point(z=1)
	print(p4.x, p4.y, p4.z)
	
	p5 = Point(z=3, y=2, x=1)
	print(p5.x, p5.y, p5.z)
	
	p6 = Point(1, 2, 3)
	print(p6.x, p6.y, p6.z)


	l1 = Line(p1=Point(), p2=Point(1,1))

	print(l1.p1, l1.p2)
	print(l1.p1.x, l1.p2.y)


