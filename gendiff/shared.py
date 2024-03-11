def get_key(line):
    return line['name']


def get_value(line):
    return line['value']


def get_status(line):
    return line['status']


def get_children(line):
    return line['children']


def is_leaf(line):
    return 'value' in line
