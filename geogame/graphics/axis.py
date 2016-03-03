import abc

class Axis(metaclass=abc.ABCMeta):
    def __init__(self, points, title, orientation):
        self.title = title
        self.points = points
        self.orientation = orientation
    
    def draw(self):
        pass
    
class VerticalAxis(Axis):
    def __init__(self, points, title=""):
        super().__init__(points, title, 1)
    
    def draw(self):
        print("y\n ^\n" + "|\n".join([str(p) for p in self.points]))
        
class HorizontalAxis(Axis):
    def __init__(self, points, title=""):
        super().__init__(points, title, 0)
    
    def draw(self):
        print("--".join([str(p) for p in self.points]) + "->" + self.title)
    

if __name__ == "__main__":
    y_axis = VerticalAxis([0, 1, 2, 3, 4], "y")
    x_axis = HorizontalAxis([0, 1, 2, 3, 4], "x")

    y_axis.draw()
    x_axis.draw()
