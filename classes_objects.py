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
