from read_data import parse_files
from point import Point
import random
import json


class Query:
    def __init__(self, num_query, path='../data/data_10'):
        self.num_query = num_query
        self.queries = []
        raw_data_points = parse_files(path)
        self.points = []
        self.positions = []
        self.keywords = []
        for raw_point in raw_data_points:
            point = Point(raw_point["id"], raw_point["x"], raw_point["y"], raw_point["keywords"])
            self.points.append(point)
            self.positions.append((point.x, point.y))
            self.keywords.extend(point.keywords)
        random.seed(42)
        random.shuffle(self.points)

        for p in self.points:
            # random 1-5 neg keys, list
            neg_keys = random.sample(self.keywords, random.randint(1, 5))
            q = (p.get_position(), p.get_keywords(), neg_keys)
            self.queries.append(q)
        random.shuffle(self.queries)

    def get_queries_milestone2_version(self):
        queries = [
            ((40.7128, -74.006), ['barbecue', 'cheese'], ['salty']),
            ((34.0522, -118.2437), ['pizza', 'salad'], ['sour']),
            ((41.8781, -87.6298), ['pizza', 'seafood'], ['bitter']),
            ((29.7604, -95.3698), ['barbecue', 'burger'], ['cheap']),
            ((33.4484, -112.074), ['burger', 'burger'], ['greasy']),
            ((39.7392, -104.9903), ['cheese', 'cheesecake'], ['salty']),
            ((29.4241, -98.4936), ['barbecue', 'salad'], ['greasy']),
            ((32.7157, -117.1611), ['sandwich', 'salad'], ['sweet']),
            ((32.7767, -96.797), ['barbecue', 'coffee'], ['expensive']),
            ((37.7749, -122.4194), ['wine', 'coffee'], ['sour']),
            ((40.4406, -79.9959), ['burger', 'chocolate'], ['expensive']),
            ((39.9526, -75.1652), ['pasta', 'salad'], ['mild']),
            ((47.6062, -122.3321), ['coffee', 'barbecue'], ['tough']),
            ((25.7617, -80.1918), ['burger', 'pasta'], ['expensive']),
            ((38.9072, -77.0369), ['cheesecake', 'coffee'], ['mild']),
            ((45.5051, -122.675), ['coffee', 'burger'], ['mild']),
            ((35.2271, -80.8431), ['cheese', 'chocolate'], ['spicy']),
            ((39.7684, -86.1581), ['chocolate', 'pasta'], ['sour']),
            ((36.1627, -86.7816), ['wine', 'taco'], ['mild']),
            ((42.3601, -71.0589), ['cheesecake', 'steak'], ['expensive']),
            ((36.1699, -115.1398), ['chocolate', 'sushi'], ['spicy']),
            ((27.9506, -82.4572), ['pizza', 'burger'], ['salty']),
            ((35.0844, -106.6504), ['burger', 'salad'], ['sweet']),
            ((43.0389, -87.9065), ['burger', 'vegan'], ['expensive']),
            ((44.9778, -93.265), ['steak', 'salad'], ['salty']),
            ((37.3382, -121.8863), ['pasta', 'seafood'], ['sweet']),
            ((35.7796, -78.6382), ['sushi', 'salad'], ['sweet']),
            ((38.2527, -85.7585), ['salad', 'wine'], ['greasy']),
            ((36.7468, -119.7726), ['coffee', 'wine'], ['greasy']),
            ((36.8529, -75.978), ['burger', 'cheese'], ['cheap']),
            ((41.2565, -95.9345), ['salad', 'wine'], ['spicy']),
            ((47.6062, -122.3321), ['coffee', 'barbecue'], ['sour']),
            ((33.748, -84.388), ['barbecue', 'wine'], ['cheap']),
            ((30.2672, -97.7431), ['steak', 'pasta'], ['salty']),
            ((41.4993, -81.6944), ['cheesecake', 'pizza'], ['sour']),
            ((39.1031, -84.512), ['burger', 'sandwich'], ['sour']),
            ((44.468, -73.1944), ['wine', 'barbecue'], ['cheap']),
            ((36.1575, -115.1492), ['chocolate', 'pizza'], ['spicy']),
            ((42.6526, -73.7562), ['wine', 'burger'], ['expensive']),
            ((43.615, -116.2023), ['steak', 'burger'], ['cheap']),
            ((46.8772, -96.7898), ['barbecue', 'wine'], ['sweet']),
            ((42.2808, -83.743), ['sandwich', 'pizza'], ['sour']),
            ((33.5207, -86.8025), ['wine', 'chocolate'], ['sweet']),
            ((32.0809, -81.0912), ['chocolate', 'salad'], ['spicy']),
            ((25.7907, -80.13), ['salad', 'pasta'], ['sweet']),
            ((33.749, -84.388), ['steak', 'taco'], ['salty']),
            ((35.228, -80.8349), ['barbecue', 'seafood'], ['cheap']),
            ((44.9393, -92.2674), ['salad', 'coffee'], ['sweet']),
            ((42.8713, -85.6861), ['sushi', 'seafood'], ['cheap']),
            ((28.5383, -81.3792), ['salad', 'steak'], ['mild']),
            ((40.7608, -111.891), ['sandwich', 'cheesecake'], ['cheap']),
            ((31.9519, -110.9709), ['steak', 'coffee'], ['expensive']),
            ((40.7178, -74.0431), ['burger', 'vegan'], ['bitter']),
            ((40.7357, -74.1724), ['barbecue', 'taco'], ['cheap']),
            ((40.9312, -73.8988), ['wine', 'sandwich'], ['cheap']),
            ((34.1478, -118.1445), ['pasta', 'cheese'], ['expensive']),
            ((33.7701, -118.1937), ['coffee', 'taco'], ['cheap']),
            ((34.0259, -118.4965), ['burger', 'pizza'], ['sweet']),
            ((42.0451, -87.6877), ['steak', 'cheesecake'], ['sweet']),
            ((41.7508, -88.1535), ['pizza', 'cheesecake'], ['sweet']),
            ((41.525, -88.0817), ['chocolate', 'vegan'], ['greasy'])
        ]
        return queries

    def get_queries_by_num_keys(self, num_pos=1, num_neg=1):
        if False:  # use queries2.json
            queries = self.get_queries_by_num_keys_queries2(num_pos, num_neg)
        else:
            queries = [q for q in self.queries if len(q[1]) == num_pos and len(q[2]) == num_neg]
        return queries[:self.num_query]

    def _get_queries_by_num_keys_queries2(self, num_pos=3, num_neg=1):
        path = '../queries2.json'
        with open(path, "r") as f:
            queries = json.load(f)
        for q in queries:
            q[0] = tuple(q[0])
        # filt by num_pos and num_neg
        queries = [q for q in queries if len(q[1]) == num_pos and len(q[2]) == num_neg]
        return queries[:self.num_query]
