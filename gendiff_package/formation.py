def formatted(data, sign=' '):
    key, value = data
    string = f'{sign} {key}: {str(value).lower()}\n'
    return ' ' * 2 + string


def formatted_diff(diff):
    if not diff:
        return '{}'

    return '{\n%s}' % ''.join(diff)
