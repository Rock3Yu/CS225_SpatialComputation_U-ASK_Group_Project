# power.py

def run_POWER(quadtree, index, target_coords, pos_tags, neg_tags, num_results):
    tx, ty = target_coords
    radius = 0.1  # Start with an initial radius
    while True:
        nearby = quadtree.query_range(tx - radius, ty - radius, tx + radius, ty + radius)
        if len(nearby) >= num_results:
            break
        radius *= 2  # Increase search area
    valid_ids = index.query(pos_tags, neg_tags)
    filtered = [pt for pt in nearby if pt.pid in valid_ids]
    filtered.sort(key=lambda pt: (pt.lat - tx) ** 2 + (pt.lon - ty) ** 2)
    return filtered[:num_results]
