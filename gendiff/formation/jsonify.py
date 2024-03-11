import json


def format(diff):
    """Formats the difference to be JSON"""

    return json.dumps(diff, indent=4)
