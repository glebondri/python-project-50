from gendiff.shared import get_key, get_value
from gendiff.shared import get_children, get_status, is_leaf
from typing import Any


def get_sign(status):
    return ('+' if status == 'added' else
            '-' if status == 'removed' else
            ' ')


def brace(string: str, depth=0) -> str:
    return '{\n' + string + '  ' * depth + '}'


def format_complex(value: dict, depth: int) -> str:
    new_value = []

    for line in value.items():
        sub_key, sub_value = line

        new_value.append(format_string(sub_key, sub_value,
                                       depth + 2))

    return brace(''.join(new_value), depth + 1)


def format_value(value: Any, depth: int):
    if value is None:
        return 'null'

    elif isinstance(value, dict):
        return format_complex(value, depth)

    elif isinstance(value, bool):
        return str(value).lower()

    return value


def format_string(key: str, value: Any, depth: int, status=None) -> str:
    string = '  ' * depth + '{sign} {key}: {value}\n'

    if status != 'changed':
        sign = get_sign(status)
        return string.format(sign=sign,
                             key=key,
                             value=format_value(value, depth))

    old_value = format_value(value['old'], depth)
    new_value = format_value(value['new'], depth)

    old_string = string.format(sign='-', key=key,
                               value=old_value)
    new_string = string.format(sign='+', key=key,
                               value=new_value)

    return old_string + new_string


def format_line(line: dict, depth: int) -> str:
    key = get_key(line)
    status = get_status(line)

    if is_leaf(line):
        return format_string(key, get_value(line), depth, status)

    children = get_children(line)
    value = map(lambda x: format_line(x, depth + 2), children)

    return format_string(key, brace(''.join(value), depth + 1),
                         depth)


def format(diff: list) -> str:
    """Formats the difference to be \"stylish\""""

    result = map(lambda x: format_line(x, 1), diff)
    return brace(''.join(result))
