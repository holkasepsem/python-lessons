"""
Implementace základních geometrických objektů.
"""

import abc


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

"""
Napište funkci, která jako vstupní parametr vezme dva body, které představují 
koncové body úhlopříčky čtyřúhelníku a vrací další dva body, které představují
koncové body druhé úhlopříčky.

Pomocí těchto bodů budeme poté konstruovat čtyřúhelník, podobně jako při 
táhnutí myši na ploše počítače.
"""

def calculate_rectangle_points(p1, p2):
    """
    Vypočítá souřadnice dalších dvou bodů úhlopříčky čtyřúhelníku.

    +----------------------+ 
    |  u2              p2  |
    |    +------------+    |
    |    |            |    |
    |    |            |    |
    |    |            |    |
    |    +------------+    |
    |  p1              u1  |
    +----------------------+
    0,0

    :param: Bod v ploše `p1` reprezentovaný n-ticí `(x, y)`.
    :param: Bod v ploše `p2` reprezentovaný n-ticí `(x, y)`.
    :return: Dva body `u1` a `u2` reprezentované n-ticemi `(x, y)`
    """
    dx = abs(p2.x - p1.x)
    dy = abs(p2.y - p1.y)

    u1 = (p1.x + dx, p1.y)
    u2 = (p1.x, )

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