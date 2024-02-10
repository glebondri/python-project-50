from json import load


def formatted(data, sign=' '):
    key, value = data
    string = f'{sign} {key}: {str(value).lower()}\n'
    return ' ' * 2 + string


def formatted_diff(diff):
    return '{\n' + ''.join(diff) + '}'


def generate_diff(a, b):
    with (open(a, 'r') as file_a,
          open(b, 'r') as file_b):
        json_a = sorted(load(file_a).items())
        json_b = sorted(load(file_b).items())

        diff = []

        index = 0
        while True:
            if index >= len(json_a):  # ain't current line deeper than 'a' yet?
                if index < len(json_b):  # can we go even further through 'b' by this index?
                    # (this line appears only in file 'b')
                    diff.append(formatted(data=json_b.pop(index),
                                          sign='+'))

                else:  # then returning the result!
                    return formatted_diff(diff)

            else:  # then the comparison goes!
                if json_a[index] != json_b[index]:  # does the data equals in both lines?
                    # then cuttin' out line from 'a'!
                    # (leveling out 'a' to 'b' until there's inequality in both lines)
                    # (this line appears only in file 'a')
                    diff.append(formatted(data=json_a.pop(index),
                                          sign='-'))

                else:  # then we're movin' to the next line!
                    # (this line appears in both 'a' & 'b')
                    diff.append(formatted(data=json_a[index]))
                    index += 1


if __name__ == '__main__':
    diff = generate_diff('file1.json', 'file2.json')
    print(diff)
    with open('../tests/fixtures/output.txt') as file:
        print(file.read())
