import os
import glob

def parse_line(line):
    parts = line.strip().split()

    # Extract data
    object_id = int(parts[0])
    latitude = float(parts[1])
    longitude = float(parts[2])
    num_keywords = int(parts[3])

    keywords = []
    for i in range(num_keywords):
        keyword = parts[4 + i * 2]
        # weight = float(parts[5 + i * 2])
        keywords.append(keyword)

    return {
        "id": object_id,
        "x": latitude,
        "y": longitude,
        "keywords": keywords
    }


def parse_files(folder_path):
    data_points = []
    # Use glob to match all txt files
    file_list = glob.glob(os.path.join(folder_path, '*.txt'))

    for file_path in file_list:
        with open(file_path, 'r') as file:
            for line in file:
                # Parse each line and append to the data_points list
                data_point = parse_line(line)
                data_points.append(data_point)

    return data_points
