import argparse


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.',
                                     add_help=True)

    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    # arguments = parser.parse_args()
    parser.parse_args()
