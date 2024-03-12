# # stylish_rules = {
# #     type(None): 'null',
# #     bool: lambda x: str(x).lower()
# # }
#
# def format_string(key, value, sign=' ', depth=0) -> str:
#     return '  ' * depth + f'{sign} {key}: {value}\n'
#
#
# def formatted(arg):
#     alias = {
#         type(None): 'null',
#         bool: str(arg).lower(),
#     }
#     return alias[type(arg)] if type(arg) in alias else arg
#
#
# def format_value(arg, depth) -> str:
#     if not isinstance(arg, dict):
#         return formatted(arg)
#
#     def walk(path, depth):
#         result = []
#
#         for key, value in path.items():
#             if isinstance(value, dict):
#                 value = walk(value, depth + 2)
#
#             result.append('  ' * (depth + 2) + f'{key}: {value}\n')
#
#         formatted_result = ''.join(result) + '  ' * depth
#         return f'{{\n{formatted_result}}}'
#
#     return walk(arg, depth + 1)
#
#
# def format(diff: list):
#     """Formats the difference to be "stylish\""""
#
#     if not diff:
#         return '{}'
#
#     def walk(value, depth=0):
#         result = []
#
#         for line in value:
#             data, state = line.values()
#             key, value = data.values()
#
#             match state:
#                 case 'changed':
#                     result.append(
#                         format_string(key,
#                                       format_value(value['old'], depth),
#                                       sign='-', depth=depth))
#                     result.append(
#                         format_string(key,
#                                       format_value(value['new'], depth),
#                                       sign='+', depth=depth))
#
#                 case 'unchanged':
#                     if isinstance(value, list):
#                         result.append(format_string(key,
#                                                     walk(value, depth + 2),
#                                                     depth=depth))
#                     else:
#                         result.append(format_string(key, format_value(value,
#                                                                       depth),
#                                                     depth=depth))
#
#                 case _:
#                     alias = {
#                         'added': '+',
#                         'removed': '-'
#                     }
#
#                     if state in alias:
#                         result.append(format_string(key, format_value(value,
#                                                                       depth),
#                                                     sign=alias[state],
#                                                     depth=depth))
#
#         formatted_result = ''.join(result) + '  ' * (depth - 1)
#         return f'{{\n{formatted_result}}}'
#
#     return walk(diff, 1)
from gendiff.shared import get_key, get_value
from gendiff.shared import get_children, get_status, is_leaf
from typing import Any


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
        return string.format(sign=('+' if status == 'added' else
                                   '-' if status == 'removed' else
                                   ' '),
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
