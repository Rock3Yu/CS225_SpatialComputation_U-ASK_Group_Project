class QuadTreeNode:
    def __init__(self, x0, y0, x1, y1, capacity=4, max_depth=10, depth=0):
        self.bounds = (x0, y0, x1, y1)
        self.capacity = capacity
        self.points = []
        self.divided = False
        self.children = []
        self.max_depth = max_depth
        self.depth = depth

    def insert(self, point):
        stack = [(self, point)]  # Stack of (node, point) pairs
        while stack:
            node, current_point = stack.pop()
            if not node.in_bounds(current_point):
                continue

            if len(node.points) < node.capacity or node.depth >= node.max_depth:
                node.points.append(current_point)
                continue

            if not node.divided:
                node.subdivide()

            for child in node.children:
                stack.append((child, current_point))

    def subdivide(self):
        x0, y0, x1, y1 = self.bounds
        mid_x = (x0 + x1) / 2
        mid_y = (y0 + y1) / 2

        self.children = [
            QuadTreeNode(x0, y0, mid_x, mid_y, self.capacity, self.max_depth, self.depth + 1),
            QuadTreeNode(mid_x, y0, x1, mid_y, self.capacity, self.max_depth, self.depth + 1),
            QuadTreeNode(x0, mid_y, mid_x, y1, self.capacity, self.max_depth, self.depth + 1),
            QuadTreeNode(mid_x, mid_y, x1, y1, self.capacity, self.max_depth, self.depth + 1),
        ]
        self.divided = True

    def in_bounds(self, point):
        x0, y0, x1, y1 = self.bounds
        return x0 <= point.x <= x1 and y0 <= point.y <= y1

    def query_range(self, x0, y0, x1, y1):
        points_in_range = []
        if not self.intersects(x0, y0, x1, y1):
            return points_in_range

        for point in self.points:
            if x0 <= point.x <= x1 and y0 <= point.y <= y1:
                points_in_range.append(point)

        if self.divided:
            for child in self.children:
                points_in_range.extend(child.query_range(x0, y0, x1, y1))

        return points_in_range

    def intersects(self, x0, y0, x1, y1):
        qx0, qy0, qx1, qy1 = self.bounds
        return not (x1 < qx0 or x0 > qx1 or y1 < qy0 or y0 > qy1)
