import sys
import re


def main(infile, outfile, pattern):
    with open(infile, 'r') as file:
        new_file = re.sub(pattern, '****', file.read())

    with open(outfile, 'w') as file:
        file.writelines(new_file)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])