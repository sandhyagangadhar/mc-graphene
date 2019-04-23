class Point:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z
        self.visited = False

    def __repr__(self):
        return "(%s,%s,%s)" % (self.x, self.y, self.z)
