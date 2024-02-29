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
    """Formats the difference to be "plain\""""

    result = []

    def walk(value, path):
        for line in value:
            data, state = line.values()
            key, value = data.values()

            string_path = '.'.join(path + [key])

            match state:
                case 'changed':
                    result.append(' '.join((PROPERTY.format(string_path),
                                            UPDATED.format(
                                                formatted(value['old']),
                                                formatted(value['new']))
                                            )))

                case 'unchanged':
                    if isinstance(value, list):
                        walk(value, path + [key])

                case _:
                    alias = {
                        'added': [PROPERTY.format(string_path),
                                  ADDED.format(formatted(value))],
                        'removed': [PROPERTY.format(string_path),
                                    REMOVED]
                    }

                    if state in alias:
                        result.append(' '.join(alias[state]))

        return '\n'.join(result)

    return walk(diff, [])
