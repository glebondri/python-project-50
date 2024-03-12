from gendiff.shared import get_key, get_value
from gendiff.shared import get_children, get_status, is_leaf
from gendiff.titles import PROPERTY, ADDED, REMOVED, UPDATED
from typing import Any


def filter_line(line):
    return (get_status(line) != 'unchanged'
            or not is_leaf(line))


def format_value(value) -> str:
    if value is None:
        return 'null'

    types = {
        bool: str(value).lower(),
        str: f'\'{value}\'',
        dict: '[complex value]'
    }

    value_type = type(value)

    if value_type in types:
        return types.get(value_type)

    return value


def format_string(key: str, value: Any, path: list, status=None) -> str:
    string_path = '.'.join(path + [key])

    if status != 'changed':
        value = format_value(value)

        plains = {
            'added': [PROPERTY.format(string_path),
                      ADDED.format(value)],
            'removed': [PROPERTY.format(string_path),
                        REMOVED]
        }

        if status in plains:
            return ' '.join(plains[status])

    else:
        old_value = format_value(value['old'])
        new_value = format_value(value['new'])

        return ' '.join((PROPERTY.format(string_path),
                         UPDATED.format(old_value,
                                        new_value)
                         ))


def format_line(line: dict, path: list) -> str:
    key = get_key(line)
    status = get_status(line)

    if is_leaf(line):
        return format_string(key, get_value(line), path, status)

    children = filter(filter_line, get_children(line))
    return '\n'.join(map(lambda x: format_line(x, path + [key]), children))


def format(diff: list) -> str:
    """Formats the difference to be \"plain\""""

    filtered_diff = filter(filter_line, diff)
    result = map(lambda x: format_line(x, []), filtered_diff)
    return '\n'.join(result)
