import json

def read_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)