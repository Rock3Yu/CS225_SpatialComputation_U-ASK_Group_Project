# quadtree.py

class QuadTree:
    def __init__(self, min_lat, min_lon, max_lat, max_lon, capacity=4, max_depth=10, depth=0):
        self.bounds = (min_lat, min_lon, max_lat, max_lon)
        self.capacity = capacity
        self.points = []
        self.children = []
        self.divided = False
        self.max_depth = max_depth
        self.depth = depth

    def add_point(self, pt):
        # Uses a stack-based insertion to avoid recursion.
        stack = [(self, pt)]
        while stack:
            node, point = stack.pop()
            if not node.contains(point):
                continue
            if len(node.points) < node.capacity or node.depth >= node.max_depth:
                node.points.append(point)
                continue
            if not node.divided:
                node.split()
            for child in node.children:
                stack.append((child, point))

    def split(self):
        min_lat, min_lon, max_lat, max_lon = self.bounds
        mid_lat = (min_lat + max_lat) / 2
        mid_lon = (min_lon + max_lon) / 2
        self.children = [
            QuadTree(min_lat, min_lon, mid_lat, mid_lon, self.capacity, self.max_depth, self.depth + 1),
            QuadTree(min_lat, mid_lon, mid_lat, max_lon, self.capacity, self.max_depth, self.depth + 1),
            QuadTree(mid_lat, min_lon, max_lat, mid_lon, self.capacity, self.max_depth, self.depth + 1),
            QuadTree(mid_lat, mid_lon, max_lat, max_lon, self.capacity, self.max_depth, self.depth + 1)
        ]
        self.divided = True

    def contains(self, pt):
        min_lat, min_lon, max_lat, max_lon = self.bounds
        return min_lat <= pt.lat <= max_lat and min_lon <= pt.lon <= max_lon

    def search_range(self, min_lat, min_lon, max_lat, max_lon):
        found = []
        if not self.overlaps(min_lat, min_lon, max_lat, max_lon):
            return found
        for pt in self.points:
            if min_lat <= pt.lat <= max_lat and min_lon <= pt.lon <= max_lon:
                found.append(pt)
        if self.divided:
            for child in self.children:
                found.extend(child.search_range(min_lat, min_lon, max_lat, max_lon))
        return found

    def overlaps(self, min_lat, min_lon, max_lat, max_lon):
        qmin_lat, qmin_lon, qmax_lat, qmax_lon = self.bounds
        return not (max_lat < qmin_lat or min_lat > qmax_lat or max_lon < qmin_lon or min_lon > qmax_lon)

    # Compatibility alias for the original method name.
    def query_range(self, min_lat, min_lon, max_lat, max_lon):
        return self.search_range(min_lat, min_lon, max_lat, max_lon)
