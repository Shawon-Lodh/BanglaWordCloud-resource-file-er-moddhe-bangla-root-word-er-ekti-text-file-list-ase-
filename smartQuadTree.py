from smartquadtree import Quadtree

q = Quadtree(0, 0, 10, 10)
class Point(object):

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self):
        return "(%.2f, %.2f) %s" % (self.x, self.y, self.color)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

q.insert(Point(2, -7, "red"))

q