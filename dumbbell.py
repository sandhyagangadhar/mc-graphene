from point import Point


class Dumbbell:
    def __init__(self, u: Point, c: Point, d: Point):
        self.u = u
        self.c = c
        self.d = d
        self.visited = False

    def __repr__(self):
        return "(%s,%s,%s)" % (self.u, self.c, self.d)
