import json


def format(diff):
    """Formats the difference to be as json"""

    return json.dumps(diff, indent=4)
