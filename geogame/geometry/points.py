
# coding: utf-8

import abc


class Point(metaclass=abc.ABCMeta):
    
    """Abstraktní třída reprezentující bod v euklidovském prostoru.
    """
    
    __slots__ = ("_coords")
        
    def __init__(self, coord, *coords, point=None):
        """
        Vytvoří novou instanci bodu a to buď ze zadaných souřadnic nebo, pokud 
        byl zadán pojmenovaný parametr `point`, tak ze souřadnic zadaného bodu.
        """
        if point is not None:
            _coords = tuple([c for c in point.coords])
        else:
            _coords = tuple([coord,]) + tuple([c for c in coords])
            
        self._coords = tuple((float(c) for c in _coords))
    
    @property
    def coords(self):
        return self._coords
    
    def __add__(self, other):
        return Point(*[sc + oc for sc, oc in zip(self.coords, other.coords)]) \
            if isinstance(other, Point) else  NotImplemented
    
    def __sub__(self, other):
        return Point(*[sc - oc for sc, oc in zip(self.coords, other.coords)]) \
            if isinstance(other, Point) else NotImplemented
        
    def __eq__(self, other):
        return all([sc == oc for sc, oc in zip(self.coords, other.coords)]) \
            if isinstance(other, Point) else NotImplemented 
    
    def __getitem__(self, index):
        return self.coords[index]
    
    def __str__(self):
        return "(" + ",".join((str(c) for c in self.coords)) + ")"
    
    def __repr__(self):
        return "Point" + self.__str__()


class Point1(Point):
    
    """
    Reprezentuje bod v 1-dimenzionální euklidovském prostoru.
    """
    
    __slots__ = ("_coords")
    
    def __init__(self, x):
        super().__init__(x)
    
    @property
    def x(self):
        return self._coords[-1]
    

class Point2(Point1):
    
    """Reprezentuje bod v 2-dimenzionálním euklidovském prostoru.
    """
    
    __slots__ = ("_coords")
    
    
    def __init__(self, x, y):
        super().__init__(x)
        self._coords += (y,)
   
    @property
    def y(self): 
        return self._coords[-1]


class Point3(Point2):
    
    """Reprezentuje bod v 3-dimenzionálním euklidovském prostoru.
    """
    
    __slots__ = ("_coords")
    
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self._coords += (z,)
    
    @property
    def z(self):
        return self._coords[-1]
