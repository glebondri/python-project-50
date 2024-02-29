# def stringify(key, value, depth, sign=' '):
#     return '  ' * depth + f'{sign} {key}: {formatted(value, depth + 1)}\n'
#
#
# def format_value(value, depth):
#     if not isinstance(value, dict):
#         return value
#
#     def walk(path, depth):
#         result = []
#
#         for key, value in path.items():
#             # if isinstance(value, dict):
#             #     value = walk(value, depth + 2)
#
#             result.append(stringify(key, value, depth))
#             # result.append('  ' * (depth + 2) + f'{key}: {value}\n')
#
#         return f"{{\n{''.join(result)}{'  ' * depth}}}"
#
#     return walk(value, depth + 1)
#
#
# def formatted(arg, depth=0):
#     alias = {
#         type(None): 'null',
#         bool: str(arg).lower(),
#         dict: format_value(arg, depth),
#         list: format(arg)
#     }
#
#     return alias[type(arg)] if type(arg) in alias else arg
#

# def format_line(line, depth=1):
#
#     data, sign = line.values()
#     key, value = data.values()
#
#     match sign:
#         case '!':
#             return (stringify(key, value['old'],
#                               depth=depth, sign='-') +
#                     stringify(key, value['new'],
#                               depth=depth, sign='+'))
#
#         case '~':
#             # if isinstance(value, list):
#             #     return stringify(key, format(value), depth=depth)
#
#             return stringify(key, value, depth=depth)
#
#         case _:
#             return stringify(key, value,
#                              depth=depth, sign=sign)
#
#     # if sign in alias:
#     #     return '\n'.join(alias[sign])
#
#
# def format(diff):
#     formatted_diff = list(map(format_line, diff))
#     return f'{{\n{"".join(formatted_diff)}}}'
#
#
# if __name__ == '__main__':
#     print(format(generate_diff('../../file1.json', '../../file2.json')))


def format_string(key, value, sign=' ', depth=0) -> str:
    return '  ' * depth + f'{sign} {key}: {value}\n'


def formatted(arg):
    alias = {
        type(None): 'null',
        bool: str(arg).lower(),
    }
    return alias[type(arg)] if type(arg) in alias else arg


def format_value(arg, depth) -> str:
    if not isinstance(arg, dict):
        return formatted(arg)

    def walk(path, depth):
        result = []

        for key, value in path.items():
            if isinstance(value, dict):
                value = walk(value, depth + 2)

            result.append('  ' * (depth + 2) + f'{key}: {value}\n')

        string = ''.join(result) + '  ' * depth
        return f'{{\n{string}}}'

    return walk(arg, depth + 1)


def format(diff: list):
    """Formats the difference to be "stylish\""""

    if not diff:
        return '{}'

    def walk(value, depth=0):
        result = []

        for line in value:
            data, state = line.values()
            key, value = data.values()

            match state:
                case 'changed':
                    result.append(
                        format_string(key,
                                      format_value(value['old'], depth),
                                      sign='-', depth=depth))
                    result.append(
                        format_string(key,
                                      format_value(value['new'], depth),
                                      sign='+', depth=depth))

                case 'unchanged':
                    if isinstance(value, list):
                        result.append(format_string(key,
                                                    walk(value, depth + 2),
                                                    depth=depth))
                    else:
                        result.append(format_string(key, format_value(value,
                                                                      depth),
                                                    depth=depth))

                case _:
                    alias = {
                        'added': '+',
                        'removed': '-'
                    }

                    if state in alias:
                        result.append(format_string(key, format_value(value,
                                                                      depth),
                                                    sign=alias[state],
                                                    depth=depth))

        string = ''.join(result) + '  ' * (depth - 1)
        return f'{{\n{string}}}'

    return walk(diff, 1)
