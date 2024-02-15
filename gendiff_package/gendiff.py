from gendiff_package.parser import parsed
from gendiff_package.formation import formatted, formatted_diff


def not_equal(a, b):
    return a != b


def has_equal_keys(a, b):
    return a[0] == b[0]


def generate_diff(a, b):
    diff = []

    file_a, file_b = (sorted(parsed(a).items()),
                      sorted(parsed(b).items()))

    index = 0
    while True:
        if index >= len(file_a):
            if index < len(file_b):
                diff.append(formatted(data=file_b.pop(index),
                                      sign='+'))

            else:
                return formatted_diff(diff)

        else:
            if not_equal(file_a[index], file_b[index]):
                diff.append(formatted(data=file_a[index],
                                      sign='-'))

                if has_equal_keys(file_a[index], file_b[index]):
                    diff.append(formatted(data=file_b.pop(index),
                                          sign='+'))
                file_a.pop(index)

            else:
                diff.append(formatted(data=file_a[index]))
                index += 1
