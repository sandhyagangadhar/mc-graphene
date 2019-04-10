class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.visited = False

    def __repr__(self):
        return "(%s,%s)" % (self.x, self.y)
