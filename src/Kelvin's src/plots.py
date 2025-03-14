import matplotlib.pyplot as plt

def plot_points(points, results=None, query_location=None):
    x, y = zip(*[p.location for p in points])
    plt.scatter(x, y, color='blue', label='Points')

    if results:
        res_x, res_y = zip(*[p.location for _, p in results])
        plt.scatter(res_x, res_y, color='red', label='Query Results')

    if query_location:
        plt.scatter(*query_location, color='green', marker='*', s=200, label='Query Location')

    plt.legend()
    plt.show()