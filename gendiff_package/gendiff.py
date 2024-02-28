from gendiff_package.parser import parsed
from gendiff_package.formation import stylish
from gendiff_package.formation import plain


def compare(a: dict, b: dict) -> list:
    if not a and not b:
        return []

    diff = []

    common_sequence = sorted((a | b).items())
    keys_a, keys_b = (list(a.keys()),
                      list(b.keys()))
    values_a, values_b = (list(a.values()),
                          list(b.values()))

    for line in common_sequence:
        key, value = line

        if line in a.items() and line in b.items():
            diff.append({'data': {'key': key,
                                  'value': value}, 'sign': '~'})

        elif key in keys_a and key in keys_b:
            index_a = keys_a.index(key)
            index_b = keys_b.index(key)

            value_a = values_a[index_a]
            value_b = values_b[index_b]

            if isinstance(value, dict):
                diff.append({'data': {'key': key,
                                      'value': compare(value_a, value_b)},
                             'sign': '~'})
            else:
                diff.append({'data': {'key': key,
                                      'value': {
                                          'old': value_a,
                                          'new': value_b}},
                             'sign': '!'})  # aka. 'changed'

        else:
            diff.append({'data': {'key': key,
                                  'value': value},
                         'sign': ('+'
                                  if key not in keys_a else
                                  '-')})

        # elif key not in keys_a:
        #     diff.append({'data': line,
        #                  'sign': '+'})
        #
        # elif key not in keys_b:
        #     diff.append({'data': line,
        #                  'sign': '-'})

    return diff


def generate_diff(path_a: str, path_b: str, out_format: str) -> str:
    """Looks for differences in both given files
    :arg out_format: Format of the output ("stylish" or "plain")
    :returns: Comparison result of both files in two possible formats"""

    data_a, data_b = (parsed(path_a),
                      parsed(path_b))
    diff = compare(data_a, data_b)

    alias = {
        'stylish': stylish.format,
        'plain': plain.format
    }

    if out_format in alias:
        return alias[out_format](diff)
