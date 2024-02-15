import json
import yaml


def parsed(path):
    with open(path, 'r') as file:
        if path.endswith('.json'):
            return json.load(file)

        elif path.endswith(('.yaml', '.yml')):
            return yaml.load(file, yaml.Loader)