class Point:
    def __init__(self, id, x, y, keywords):
        self.id = id
        self.location = (x, y)
        self.keywords = set(keywords)

    def __repr__(self):
        return f"Point(id={self.id}, location={self.location}, keywords={self.keywords})"