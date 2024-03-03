from gendiff.titles import PROPERTY, ADDED, REMOVED, UPDATED


def formatted(arg):
    alias = {
        type(None): 'null',
        dict: '[complex value]',
        bool: str(arg).lower(),
        str: f'\'{arg}\''
    }

    return alias[type(arg)] if type(arg) in alias else arg

# plain_rules = {
#     type(None): 'null',
#     dict: '[complex value]',
#     bool: lambda arg: str(arg).lower(),
#     str: lambda arg: f'\'{arg}\''
# }


def format(diff: list):
    """Formats the "diff" to be "plain\""""

    result = []

    def walk(value, path):
        for line in value:
            data, state = line.values()
            key, value = data.values()

            string_path = '.'.join(path + [key])

            match state:
                case 'changed':
                    old_value = formatted(value['old'])
                    new_value = formatted(value['new'])

                    result.append(' '.join((PROPERTY.format(string_path),
                                            UPDATED.format(old_value,
                                                           new_value)
                                            )))

                case 'unchanged':
                    if isinstance(value, list):
                        walk(value, path + [key])

                case _:
                    value = formatted(value)

                    alias = {
                        'added': [PROPERTY.format(string_path),
                                  ADDED.format(value)],
                        'removed': [PROPERTY.format(string_path),
                                    REMOVED]
                    }

                    if state in alias:
                        result.append(' '.join(alias[state]))

        return '\n'.join(result)

    return walk(diff, [])
