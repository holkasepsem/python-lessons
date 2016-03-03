"""
Implementace základních geometrických objektů.
"""

import abc
from math import sqrt


# -----------------------------------------------------------------------------
class Point:  # Immutable

    """
    Třída reprezentující bod v n-rozměrném euklidovském prostoru
    (prozatím jen kartézské souřadnice).
    """

    def __init__(self, *coordinates):
        """
        Vytvoří bod s požadovanými souřadnicemi.
        :coordinates: Kartézké souřadnice.
        """
        try:
            self._coordinates = list((float(value) for value in coordinates))
            if not len((self._coordinates)):
                raise ValueError("Musíte zadat alespoň jednu souřadnici!")
        except:
            raise ValueError("Souřadnice musí být sekvence čísel!")

        self._dimension = len(self._coordinates)

        for index in range(self._dimension):
            setattr(Point, "x" + str(index + 1),
                property(lambda self,
                    index=index: self._coordinates[index]))

    @property
    def _coordinates(self):
        return self.__coordinates

    @_coordinates.setter
    def _coordinates(self, values):
        # TODO Ošetři podobně jako v `__init__`!
        if not hasattr(self, "_dimension"):
            self.__coordinates = values
        else:
            self.__coordinates = values[0:self.dimension]
        self._dimension = len(self.__coordinates)

    @property
    def dimension(self):
        return self._dimension

    def __getitem__(self, i):
        return self._coordinates[i]

    def __setitem__(self, i, v):
        try:
            value = float(v)
        except:
            raise TypeError
        self._coordinates[i] = value


# -----------------------------------------------------------------------------
class Line2D:
    def __init__(self, p1, p2):
        if len(p1) < 2 or len(p2) < 2:
            raise ValueError
        self.p1 = p1[0:2]
        self.p2 = p2[0:2]


# -----------------------------------------------------------------------------
class Canvas:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def draw(self, point, *points):
        x = point.x1 - 1
        y = point.x2 - 1

        for i in range(self.height - 1):
            row = ""
            for j in range(self.width):
                if i == x and j == y:
                    row += "#"
                else:
                    row += "."
            print(row)

        # print( "+" + "".join([self.width * "━ ━"]))



if __name__ == "__main__":
    print(__file__)
    canvas = Canvas(10, 10)
    canvas.draw(Point(5, 5))
