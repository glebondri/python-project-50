from gendiff.shared import get_key, get_value
from gendiff.shared import get_children, get_status, is_leaf
from gendiff.titles import PROPERTY, ADDED, REMOVED, UPDATED


# def formatted(arg):
#     alias = {
#         type(None): 'null',
#         dict: '[complex value]',
#         bool: str(arg).lower(),
#         str: f'\'{arg}\''
#     }
#
#     return alias[type(arg)] if type(arg) in alias else arg
#
# # plain_rules = {
# #     type(None): 'null',
# #     dict: '[complex value]',
# #     bool: lambda arg: str(arg).lower(),
# #     str: lambda arg: f'\'{arg}\''
# # }
#
#
# def format(diff: list):
#     """Formats the "diff" to be "plain\""""
#
#     result = []
#
#     def walk(value, path):
#         for line in value:
#             data, state = line.values()
#             key, value = data.values()
#
#             string_path = '.'.join(path + [key])
#
#             match state:
#                 case 'changed':
#                     old_value = formatted(value['old'])
#                     new_value = formatted(value['new'])
#
#                     result.append(' '.join((PROPERTY.format(string_path),
#                                             UPDATED.format(old_value,
#                                                            new_value)
#                                             )))
#
#                 case 'unchanged':
#                     if isinstance(value, list):
#                         walk(value, path + [key])
#
#                 case _:
#                     value = formatted(value)
#
#                     alias = {
#                         'added': [PROPERTY.format(string_path),
#                                   ADDED.format(value)],
#                         'removed': [PROPERTY.format(string_path),
#                                     REMOVED]
#                     }
#
#                     if state in alias:
#                         result.append(' '.join(alias[state]))
#
#         return '\n'.join(result)
#
#     return walk(diff, [])


def filter_line(line):
    return (get_status(line) != 'unchanged'
            or not is_leaf(line))


def format_value(value):
    if value is None:
        return 'null'

    elif isinstance(value, bool):
        return str(value).lower()

    elif isinstance(value, str):
        return f'\'{value}\''

    elif isinstance(value, dict):
        return '[complex value]'

    return value


def format_string(key, value, path, status=None):
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
#     if not isinstance(value, dict):
    #         if value is None:
    #             return 'null'
    #
    #         if isinstance(value, bool):
    #             return str(value).lower()
    #
    #         return value
    #
    #     sub_value = []
    #
    #     for line in value.items():
    #         sub_key, sub_value = line
    #
    #         sub_value.append(format_string(sub_key, sub_value,
    #                                        depth + 2))
    #
    #     return brace(''.join(sub_value), depth + 1)
    #
    # string = '  ' * depth + '{sign} {key}: {value}\n'
    #
    # if status != 'changed':
    #     return string.format(sign=('+' if status == 'added' else
    #                                '-' if status == 'removed' else
    #                                ' '),
    #                          key=key, value=format_value(value))
    #
    # old_value = format_value(value['old'])
    # new_value = format_value(value['new'])
    #
    # return (string.format(sign='-', key=key,
    #                       value=old_value) +
    #         string.format(sign='+', key=key,
    #                       value=new_value))


def format_line(line, path):
    key = get_key(line)
    status = get_status(line)

    if is_leaf(line):
        return format_string(key, get_value(line), path, status)

    children = filter(filter_line, get_children(line))
    return '\n'.join(map(lambda x: format_line(x, path + [key]), children))


def format(diff):
    filtered_diff = filter(filter_line, diff)
    result = map(lambda x: format_line(x, []), filtered_diff)
    return '\n'.join(result)
