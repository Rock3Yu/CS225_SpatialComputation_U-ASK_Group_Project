# geopoint.py

class GeoPoint:
    def __init__(self, pid, lat, lon, tags):
        self.pid = pid      # Unique identifier
        self.lat = lat      # Latitude
        self.lon = lon      # Longitude
        self.tags = tags    # List of associated keywords
