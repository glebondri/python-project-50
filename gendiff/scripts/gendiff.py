import argparse
from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        add_help=True
    )

    parser.add_argument('-f', '--format', help='set format of output',
                        default='stylish')
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    arguments = parser.parse_args()
    path_a, path_b = arguments.first_file, arguments.second_file
    out_format = arguments.format

    diff = generate_diff(path_a, path_b, out_format)
    print(diff)
