from gendiff_package.parser import parsed


def walk(a, b):
    diff = []

    common_sequence = sorted((a | b).items())
    keys_a, keys_b = (list(a.keys()),
                      list(b.keys()))
    values_a, values_b = (list(a.values()),
                          list(b.values()))

    for line in common_sequence:
        key, value = line

        if line in a.items() and line in b.items():
            diff.append({'data': line, 'sign': '~'})

        elif key in keys_a and key in keys_b:
            index_a = keys_a.index(key)
            index_b = keys_b.index(key)

            value_a = values_a[index_a]
            value_b = values_b[index_b]

            if isinstance(value, dict):
                diff.append({'data': (key, walk(
                    value_a, value_b)), 'sign': '~'})
            else:
                diff.append({'data': (key, value_a, value_b),
                             'sign': '!'})  # aka. 'changed'

        else:
            diff.append({'data': line,
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


def generate_diff(path_a, path_b):
    data_a, data_b = (parsed(path_a),
                      parsed(path_b))
    if not data_a and not data_b:
        return []

    return walk(data_a, data_b)
