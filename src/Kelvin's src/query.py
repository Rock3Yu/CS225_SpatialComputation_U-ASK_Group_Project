class Query:
    def __init__(self, location, positive_keywords, negative_keywords):
        self.location = location
        self.positive = positive_keywords
        self.negative = negative_keywords