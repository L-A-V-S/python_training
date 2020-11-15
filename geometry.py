from math import sqrt

class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def distance(self,p2):
        dx = p2.x - self.x
        dy = p2.y - self.y
        return sqrt(dx*dx +dy*dy)

a = Point(0,0)
b = Point(3,4)
print(a.distance(b))
