def formatted(arg):
    alias = {
        None: 'null',
        True: 'true',
        False: 'false'
    }

    if arg in alias:
        return alias[arg]

    return arg


def format_value(arg, depth=0):
    if not isinstance(arg, dict):
        return formatted(arg)

    def walk(path, depth):
        result = []

        for key, value in path.items():
            if isinstance(value, dict):
                value = walk(value, depth + 2)

            result.append('  ' * (depth + 2) + f'{key}: {value}\n')

        string = ''.join(result) + '  ' * depth
        return '{\n%s}' % string

    return walk(arg, depth + 1)


def format_stylish(diff):
    if not diff:
        return '{}'

    def format_string(key, value, sign=' ', depth=0):
        return '  ' * depth + '{} {}: {}\n'.format(sign, key, value)

    def walk(path, depth=0):
        result = []

        for line in path:
            data, sign = line.values()

            key, *values = data

            match sign:
                case '!':
                    old_value, new_value = (values[0],
                                            values[1])
                    result.append(format_string(key,
                                                format_value(old_value, depth),
                                                sign='-', depth=depth))
                    result.append(format_string(key,
                                                format_value(new_value, depth),
                                                sign='+', depth=depth))

                case '~':
                    if isinstance(values[0], list):
                        result.append(format_string(key,
                                                    walk(values[0], depth + 2),
                                                    depth=depth))
                    else:
                        result.append(format_string(key, format_value(values[0],
                                                                      depth),
                                                    depth=depth))

                case _:
                    result.append(format_string(key, format_value(values[0],
                                                                  depth),
                                                sign=sign, depth=depth))

        string = ''.join(result) + '  ' * (depth - 1)
        return '{\n%s}' % string

    return walk(diff, 1)
