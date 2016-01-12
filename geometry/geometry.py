"""
Implementace základních geometrických objektů.
"""

import abc
from math import sqrt


# -----------------------------------------------------------------------------
class Point:


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
            self._coordinates = tuple((float(value) for value in coordinates))
            if not len((self._coordinates)):
                raise ValueError("Musíte zadat alespoň jednu souřadnici!")
        except: 
            raise ValueError("Souřadnice musí být sekvence čísel!")
        
        self._dimension = len(self.coordinates)

        for index in range(len(coordinates)):
            setattr(Point, "x" + str(index + 1), 
                property(lambda self, 
                    index=index: str(self.coordinates[index])))
            
    @property # getter
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, value):
        # TODO Ošetři podobně jako v `__init__`!
        self._coordinates = value
        self._dimension = len(self.coordinates)
        
    @property
    def dimension(self):
        return self._dimension

    
# -----------------------------------------------------------------------------
class Line():
    def __init__():
        pass


# =============================================================================
# SIMPLE TESTS
# =============================================================================
if __name__ == "__main__":

    p = Point(1, 2, 3, 4, 8.0, 9.0)
    print(p.coordinates)
    print(p.dimension)
    print(p.x1, p.x2, p.x3, p.x4, p.x5, p.x6)
    print(type(p.x1))
    print(type(p.coordinates)) 
    
    p1 = (1, 2)
    p2 = (3, 4)
    

    import collections
    Point2 = collections.namedtuple("Point2", "x y")

     
    p3 = Point2(1, 2)
    p4 = Point2(3, 4)

    print(p1[0])
    print(p1[1])

    print(p3.x)
    print(p3.y)
