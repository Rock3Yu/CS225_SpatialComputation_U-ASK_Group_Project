# POWER Algorithm (TKQN)**
def POWER(quadtree, inverted_index, query_coords, keywords, negative_keywords, k):
    # Spatial filtering (kNN using quadtree)
    x, y = query_coords
    radius = 0.1  # Initial search radius (adjust as needed)
    while True:
        spatial_candidates = quadtree.query_range(x - radius, y - radius, x + radius, y + radius)
        if len(spatial_candidates) >= k:
            break
        radius *= 2  # Expand search radius

    # Keyword filtering
    keyword_candidates = inverted_index.filter(keywords, negative_keywords)

    # Intersection and ranking
    final_candidates = [point for point in spatial_candidates if point.id in keyword_candidates]
    final_candidates.sort(key=lambda p: (p.x - x) ** 2 + (p.y - y) ** 2)  # Sort by distance

    # Return top-k results
    return final_candidates[:k]
