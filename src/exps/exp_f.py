import time

from point import Point
from quadTreeNode import QuadTreeNode
from invertedIndex import InvertedIndex
from power import POWER
from power_batch import POWER_batch, group_queries_by_proximity
from query import Query
from read_data import parse_files

X_MIN, X_MAX = -180, 180
Y_MIN, Y_MAX = -90, 90


def exp_f(path, query_num):
    print("Running exp_f() function...")
    x_labels = [2, 4, 6, 8, 10]
    line_POWER, line_POWER_batch = [], []
    x_name = "Dataset Size (Millions)"
    for size in x_labels:
        path = f"../data/data_{size}"
        folder_path = path
        data_points = parse_files(folder_path)
        print(f"Total number of data points: {len(data_points)}")

        # Initialize the quadtree and inverted index
        print("Initializing Quadtree and Inverted Index...")
        quadtree = QuadTreeNode(X_MIN, Y_MIN, X_MAX, Y_MAX, capacity=4, max_depth=15, depth=0)
        inverted_index = InvertedIndex()
        for point in data_points:
            point_obj = Point(point["id"], point["x"], point["y"], point["keywords"])
            quadtree.insert(point_obj)
            inverted_index.insert(point_obj)
        print("Quadtree and Inverted Index initialized successfully!")

        # Begin the experiment
        q = Query(query_num, path=folder_path)
        
        # Get the queries
        queries = q.get_queries_by_num_keys(num_pos=3, num_neg=1)
        queries_groups_20 = group_queries_by_proximity(queries, 20)
        
        print(f"Running POWER and POWER_batch...")

        # Run original POWER
        # print("Running original POWER...")
        start = time.time()
        res = []
        for query in queries:
            res += [POWER(quadtree, inverted_index, *query, k=5)]
        original_latency = (time.time() - start) / query_num * 100
        # print(f"Original POWER took {original_latency} seconds")

        # Run batch POWER
        # print("Running batch POWER...")
        start = time.time()
        res = []
        for group in queries_groups_20:
            res += POWER_batch(quadtree, inverted_index, group, k=5)
        batched_latency = (time.time() - start) / query_num * 100
        # print(f"Batched POWER took {batched_latency} seconds")

        line_POWER.append(original_latency)
        line_POWER_batch.append(batched_latency)

    return line_POWER, line_POWER_batch, x_labels, x_name