# power_batch.py

from collections import defaultdict
from geopy.distance import geodesic
import copy

def coordinate_hash(lat, lon, grid_size=100):
    return (round(lat / grid_size), round(lon / grid_size))

def cluster_queries(queries, radius_miles=100):
    # Create clusters of queries based on proximity.
    pending = copy.deepcopy(queries)
    grid = defaultdict(list)
    for query in pending:
        cell = coordinate_hash(*query[0], grid_size=radius_miles)
        grid[cell].append(query)
    
    clusters = []
    processed = set()
    for cell, qlist in grid.items():
        if cell in processed:
            continue
        processed.add(cell)
        group = []
        queue = qlist[:]
        while queue:
            current = queue.pop(0)
            group.append(current)
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    neighbor = (cell[0] + dx, cell[1] + dy)
                    if neighbor in grid:
                        for neighbor_query in grid[neighbor][:]:
                            if geodesic(current[0], neighbor_query[0]).miles <= radius_miles and neighbor_query not in group:
                                queue.append(neighbor_query)
                                grid[neighbor].remove(neighbor_query)
        clusters.append(group)
    return clusters

def compute_spatial_candidates(tree, queries, num_results):
    candidates = {}
    radii = {}
    init_radius = 0.1
    for idx, (loc, _, _) in enumerate(queries):
        tx, ty = loc
        r = init_radius
        candidate_set = set()
        while True:
            candidate_set.update(tree.query_range(tx - r, ty - r, tx + r, ty + r))
            if len(candidate_set) >= num_results:
                radii[idx] = r
                break
            r *= 2
        candidates[idx] = candidate_set
    return candidates, radii

def apply_keyword_filter(candidates_dict, queries, index):
    filtered = {}
    for idx, (_, pos_tags, neg_tags) in enumerate(queries):
        valid_ids = index.query(pos_tags, neg_tags)
        filtered[idx] = [pt for pt in candidates_dict[idx] if pt.pid in valid_ids]
    return filtered

def process_batch(tree, index, queries, num_results):
    spatial_dict, _ = compute_spatial_candidates(tree, queries, num_results)
    filtered_dict = apply_keyword_filter(spatial_dict, queries, index)

    results = {}
    for idx, (loc, _, _) in enumerate(queries):
        tx, ty = loc
        sorted_points = sorted(filtered_dict[idx], key=lambda pt: (pt.lat - tx) ** 2 + (pt.lon - ty) ** 2)
        results[idx] = sorted_points[:num_results]
    return results

def run_POWER_batch(tree, index, queries, num_results):
    return process_batch(tree, index, queries, num_results)
