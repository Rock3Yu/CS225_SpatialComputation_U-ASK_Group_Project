from read_data import load_data
from query import Query
from power import POWER
from plots import plot_points

def main():
    points = load_data('data.txt')

    query = Query(location=(10, 20), positive_keywords={'cafe'}, negative_keywords={'bakery'})
    results = POWER(query.location, query.positive, query.negative, k=3, points=points)

    print("Query Results:")
    for dist, point in results:
        print(f"Point ID: {point.id}, Distance: {dist:.2f}, Keywords: {point.keywords}")

    plot_points(points, results, query.location)

if __name__ == '__main__':
    main()