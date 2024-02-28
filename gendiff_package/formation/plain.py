from gendiff_package.titles import PROPERTY, ADDED, REMOVED, UPDATED


def formatted(arg):
    alias = {
        type(None): 'null',
        dict: '[complex value]',
        bool: str(arg).lower(),
        str: f'\'{arg}\''
    }

    return alias[type(arg)] if type(arg) in alias else arg


def format(diff: list):
    """Formats the difference to be "plain"""

    result = []

    def walk(value, path):
        for line in value:
            data, sign = line.values()
            key, value = data.values()

            string_path = '.'.join(path + [key])

            match sign:
                case '!':
                    result.append(' '.join((PROPERTY.format(string_path),
                                            UPDATED.format(
                                                formatted(value['old']),
                                                formatted(value['new']))
                                            )))

                case '~':
                    if isinstance(value, list):
                        walk(value, path + [key])

                case _:
                    alias = {
                        '+': [PROPERTY.format(string_path),
                              ADDED.format(formatted(value))],
                        '-': [PROPERTY.format(string_path),
                              REMOVED]
                    }

                    if sign in alias:
                        result.append(' '.join(alias[sign]))

        return '\n'.join(result)

    return walk(diff, [])
