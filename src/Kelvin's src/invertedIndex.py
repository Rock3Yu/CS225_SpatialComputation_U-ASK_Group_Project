from collections import defaultdict

class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(set)

    def build(self, points):
        for point in points:
            for keyword in point.keywords:
                self.index[keyword].add(point.id)

    def query(self, keywords):
        result_sets = [self.index[kw] for kw in keywords if kw in self.index]
        if not result_sets:
            return set()
        return set.intersection(*result_sets)