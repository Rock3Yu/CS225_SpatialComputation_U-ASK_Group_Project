from power import POWER

def batch_POWER(queries, k, points):
    results = {}
    for qid, query in enumerate(queries):
        location, pos, neg = query
        results[qid] = POWER(location, pos, neg, k, points)
    return results