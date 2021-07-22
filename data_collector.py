import json
from os import path

class data_collection():
    """
    Class for Collecting the JSON Data from the Arduino
    """
    def __init__(self, filename):
        self.filename = filename
        if not path.exists(filename):
            with open(self.filename,'r') as f:
                data = json.load(f)

    def search(self, key):
        "Search for the specific key"
        with open(self.filename, 'r') as f:
            data = json.load(f)

        if key not in data.keys():
            return None

        return data[key]



