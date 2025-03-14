class QuadTreeNode:
    def __init__(self, bounds, points):
        self.bounds = bounds  # (xmin, ymin, xmax, ymax)
        self.points = points
        self.children = []

    def is_leaf(self):
        return len(self.children) == 0

    def subdivide(self):
        pass  