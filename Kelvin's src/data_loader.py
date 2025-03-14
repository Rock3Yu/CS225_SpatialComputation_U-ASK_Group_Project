# data_loader.py

import os
import glob

def parse_line_data(line):
    tokens = line.strip().split()
    pid = int(tokens[0])
    lat = float(tokens[1])
    lon = float(tokens[2])
    count = int(tokens[3])
    keywords = [tokens[4 + i * 2] for i in range(count)]
    return {"id": pid, "x": lat, "y": lon, "keywords": keywords}

def load_data(directory):
    all_data = []
    file_pattern = os.path.join(directory, '*.txt')
    for filepath in glob.glob(file_pattern):
        with open(filepath, 'r') as f:
            for entry in f:
                all_data.append(parse_line_data(entry))
    return all_data
