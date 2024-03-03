# stylish_rules = {
#     type(None): 'null',
#     bool: lambda x: str(x).lower()
# }

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

        formatted_result = ''.join(result) + '  ' * depth
        return f'{{\n{formatted_result}}}'

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

        formatted_result = ''.join(result) + '  ' * (depth - 1)
        return f'{{\n{formatted_result}}}'

    return walk(diff, 1)
