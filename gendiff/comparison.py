from gendiff import parser
from gendiff.formation import stylish, plain, jsonify


def compare(a: dict, b: dict) -> list:
    if not a and not b:
        return []

    common_sequence = sorted((a | b).items())
    keys_a, keys_b = (list(a.keys()),
                      list(b.keys()))
    values_a, values_b = (list(a.values()),
                          list(b.values()))

    diff = []

    for line in common_sequence:
        key, value = line

        if line in a.items() and line in b.items():
            diff.append({'name': key, 'value': value,
                         'status': 'unchanged'})

        elif key in keys_a and key in keys_b:
            index_a = keys_a.index(key)
            index_b = keys_b.index(key)

            value_a = values_a[index_a]
            value_b = values_b[index_b]

            if isinstance(value_a, dict) and isinstance(value_b, dict):
                diff.append({'name': key, 'children': compare(value_a, value_b),
                             'status': 'unchanged'})

            else:
                diff.append({'name': key, 'value': {'old': value_a,
                                                    'new': value_b},
                            'status': 'changed'})

        else:
            status = 'added' if key in keys_b else 'removed'

            diff.append({'name': key, 'value': value,
                         'status': status})

    return diff


def generate_diff(path_a: str, path_b: str, out_format='stylish') -> str:

    """Looks for a differences relatively of \'original\' file to \'new\'
    :arg path_a: Path to the \'original\' file
    :arg path_b: Path to the \'new\' file
    :arg out_format: Format of the output ("stylish", "plain" or "json")
    :returns: Comparison result in specified format"""

    file_a = open(path_a, 'r')
    file_b = open(path_b, 'r')

    data_a, data_b = (parser.parse(file_a),
                      parser.parse(file_b))
    diff = compare(data_a, data_b)

    formats = {
        'stylish': stylish.format,
        'plain': plain.format,
        'json': jsonify.format
    }

    if out_format in formats:
        return formats[out_format](diff)

    raise Exception(f'Unknown format \"{out_format}\"!')
