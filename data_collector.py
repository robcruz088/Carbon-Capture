import json
from os import path

class data_collection():
    def __init__(self, filename):
        self.filename = filename
        if not path.exists(filename):
            with open(self.filename,'r') as f:
                empty_dict
