import json


def format(diff: list) -> str:
    """Formats the difference to be JSON"""

    return json.dumps(diff, indent=4)
