class InvertedIndex:
    def __init__(self):
        self.index = {}

    def insert(self, point):
        for keyword in point.keywords:
            if keyword not in self.index:
                self.index[keyword] = set()
            self.index[keyword].add(point.id)

    def filter(self, keywords, negative_keywords):
        candidates = set()
        for keyword in keywords:
            if keyword in self.index:
                candidates.update(self.index[keyword])
        for neg_keyword in negative_keywords:
            if neg_keyword in self.index:
                candidates.difference_update(self.index[neg_keyword])
        return candidates
