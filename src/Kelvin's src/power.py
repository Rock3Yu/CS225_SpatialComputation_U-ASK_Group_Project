import heapq
from math import sqrt

def distance(p1, p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def satisfies_keywords(point, positive, negative):
    return positive.issubset(point.keywords) and negative.isdisjoint(point.keywords)

def POWER(query_location, positive, negative, k, points):
    heap = []
    for point in points:
        if satisfies_keywords(point, positive, negative):
            dist = distance(query_location, point.location)
            heapq.heappush(heap, (dist, point))
    return heapq.nsmallest(k, heap)