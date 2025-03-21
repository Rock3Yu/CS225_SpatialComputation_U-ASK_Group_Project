from collections import defaultdict
from geopy.distance import geodesic
import copy


# def group_queries_by_proximity(q, radius_miles=100):
#     groups = []
#     queries = copy.deepcopy(q)
#     while queries:
#         first_query = queries.pop(0)
#         current_group = [first_query]
#         current_group_coords = first_query[0]

#         for other_query in queries[:]:
#             other_query_coords = other_query[0]
#             distance = geodesic(current_group_coords, other_query_coords).miles
#             if distance <= radius_miles:
#                 current_group.append(other_query)
#                 queries.remove(other_query)

#         groups.append(current_group)
#     return groups

def hash_coordinates(lat, lon, grid_size_miles=100):
    return (round(lat / grid_size_miles), round(lon / grid_size_miles))


def group_queries_by_proximity(q, radius_miles=100):
    queries = copy.deepcopy(q)
    grid = defaultdict(list)

    # Step 1: Assign queries to grid cells
    for query in queries:
        cell = hash_coordinates(*query[0], radius_miles)
        grid[cell].append(query)

    # Step 2: Group queries using only nearby cells
    visited = set()
    groups = []
    for cell, cell_queries in grid.items():
        if cell in visited:
            continue
        visited.add(cell)
        current_group = []
        queue = cell_queries[:]
        while queue:
            first_query = queue.pop(0)
            current_group.append(first_query)
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    neighbor_cell = (cell[0] + dx, cell[1] + dy)
                    if neighbor_cell in grid:
                        for neighbor_query in grid[neighbor_cell]:
                            distance = geodesic(first_query[0], neighbor_query[0]).miles
                            if distance <= radius_miles and neighbor_query not in current_group:
                                queue.append(neighbor_query)
                                grid[neighbor_cell].remove(neighbor_query)
        groups.append(current_group)

    return groups


def generate_spatial_candidates(quadtree, queries, k):
    """
    The function uses an expanding search radius to ensure that each query has at least k spatial candidates.
    """
    query_radii = {}
    spatial_candidates = defaultdict(set)

    # Start with initial search radius
    initial_radius = 0.1  # adjust based on context
    for i, (query_coords, _, _) in enumerate(queries):
        x, y = query_coords
        radius = initial_radius
        while True:
            curr_candidates = set(quadtree.query_range(x - radius, y - radius, x + radius, y + radius))
            spatial_candidates[i].update(curr_candidates)
            if len(spatial_candidates[i]) >= k:
                query_radii[i] = radius
                break
            radius *= 2

    return spatial_candidates, query_radii


def filter_candidates_by_keywords(spatial_candidates, queries, inverted_index):
    """
    performs an intersection between the spatial candidates and the keyword-based candidates.
    """
    final_candidates = {}

    for i, (_, keywords, negative_keywords) in enumerate(queries):
        keyword_candidates = inverted_index.filter(keywords, negative_keywords)
        # Intersect with spatial candidates
        intersected = [point for point in spatial_candidates[i] if point.id in keyword_candidates]
        final_candidates[i] = intersected

    return final_candidates


def process_queries_optimized(quadtree, inverted_index, queries, k):
    # Get spatial candidates for each query
    spatial_candidates, _ = generate_spatial_candidates(quadtree, queries, k)

    # Filter based on keywords
    all_candidates = filter_candidates_by_keywords(spatial_candidates, queries, inverted_index)

    # Sort by distance and retrieve top-k for each query
    results = {}
    for i, (query_coords, _, _) in enumerate(queries):
        x, y = query_coords
        sorted_by_distance = sorted(all_candidates[i], key=lambda p: (p.x - x) ** 2 + (p.y - y) ** 2)
        results[i] = sorted_by_distance[:k]

    return results


# POWER_batch Algorithm (TKQN)**
def POWER_batch(quadtree, inverted_index, queries, k):
    return process_queries_optimized(quadtree, inverted_index, queries, k)
