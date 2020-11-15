from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1,p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    return sqrt(dx*dx +dy*dy)

print(distance(Point(0,0), Point(3,4)))
