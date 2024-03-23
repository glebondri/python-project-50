from typing import Any


def get_key(line: dict) -> str:
    return line['name']


def get_value(line: dict) -> Any:
    return line['value']


def get_status(line: dict) -> str:
    return line['status']


def get_children(line: dict) -> list:
    return line['children']


def is_leaf(line: dict) -> bool:
    return 'value' in line
