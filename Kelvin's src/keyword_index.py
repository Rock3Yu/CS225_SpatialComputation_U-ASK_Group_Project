# keyword_index.py

class KeywordIndex:
    def __init__(self):
        self._index = {}

    def add(self, point):
        # 'point' is expected to have attributes: pid and tags (list of keywords)
        for tag in point.tags:
            self._index.setdefault(tag, set()).add(point.pid)

    def query(self, include=None, exclude=None):
        include = include or []
        exclude = exclude or []
        result = set()
        for tag in include:
            if tag in self._index:
                result |= self._index[tag]
        for tag in exclude:
            if tag in self._index:
                result -= self._index[tag]
        return result
