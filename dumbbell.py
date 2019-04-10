class Dumbbell:
    def __init__(self, u, c, d):
        self.u = u
        self.c = c
        self.d = d
        self.visited = False

    def __repr__(self):
        return "(%s,%s,%s)" % (self.u, self.c, self.d)
