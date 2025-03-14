import pandas as pd
from point import Point

def load_data(filepath):
    df = pd.read_csv(filepath)
    points = []
    for _, row in df.iterrows():
        keywords = row['keywords'].split()
        points.append(Point(row['id'], row['x'], row['y'], keywords))
    return points