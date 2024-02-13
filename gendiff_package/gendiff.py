from gendiff_package.formation import formatted, formatted_diff
from json import load


def differ(a, b):
    return a != b


def has_equal_keys(a, b):
    return a[0] == b[0]


def generate_diff(a, b):
    diff = []

    with (open(a, 'r') as file_a,
          open(b, 'r') as file_b):
        json_a = sorted(load(file_a).items())
        json_b = sorted(load(file_b).items())

        index = 0
        while True:
            if index >= len(json_a):
                if index < len(json_b):
                    diff.append(formatted(data=json_b.pop(index),
                                          sign='+'))

                else:
                    return formatted_diff(diff)

            else:
                if differ(json_a[index], json_b[index]):
                    diff.append(formatted(data=json_a[index],
                                          sign='-'))

                    if has_equal_keys(json_a[index], json_b[index]):
                        diff.append(formatted(data=json_b.pop(index),
                                              sign='+'))
                    json_a.pop(index)

                else:
                    diff.append(formatted(data=json_a[index]))
                    index += 1


# if __name__ == '__main__':
#     # there is a bug!
#     # comparing smaller 'a' to larger 'b' (which has key closer to the very beginning of alphabet...
#     # ...than 'a' does), breaks the comparison algorithm
#     # (e.g. in obsidian)
#
#     diff = generate_diff('../a.json', '../b.json')
#     print(diff)
#     # with open('../tests/fixtures/output.txt') as file:
#     #     print(file.read())
